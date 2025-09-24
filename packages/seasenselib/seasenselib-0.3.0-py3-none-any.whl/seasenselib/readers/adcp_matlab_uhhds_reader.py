"""Module for reading ADCP data from MATLAB .mat files converted from binaries recorded from UHH during DS cruises."""

from __future__ import annotations
import numpy as np
import xarray as xr
import scipy.io
import pandas as pd
from datetime import datetime, timedelta
import re
import seasenselib.parameters as ctdparams
from seasenselib.readers.base import AbstractReader

class AdcpMatlabUhhdsReader(AbstractReader):
    """ Reads ADCP data from a matlab (.mat) file into a xarray Dataset. 

        This class is used to read ADCP files, which are stored in .mat files.
        The provided data is expected to be in a matlab format, and this reader
        is designed to detect the format, rename the variables under CF standards and create an xarra Dataset.
        As there are various versions of variable names and file structures,
        the reader will detect the version and parse accordingly.

        Attributes:
        ---------- 
        data : xr.Dataset
            The xarray Dataset containing the ADCP data previously stored in a .mat file.
        input_file : str
            The path to the input ADCP file containing the sensor data stored in MATLAB .mat file.

        Methods:
        -------
        __init__(input_file):
            Initializes the AdcpMatlabReader with the input file.
        __read():
            Reads the ADCP file and processes the data into an xarray Dataset.
        get_data():
            Returns the xarray Dataset containing the sensor data.
        _detect_format():
            Detects the format of the ADCP -mat input file and redirects accordingly.
        _parse_time():
            Handles different time formats in the ADCP .mat files.
        _add_time():
            Adds time coordinates to the dataset based on the detected format.
        _add_data_and_coords():
            Adds data variables and coordinates to the dataset based on the detected format.
        _add_metadata():
            Adds common metadata attributes to the dataset.
        """

    def __init__(self, input_file, mapping=None):
        super().__init__(input_file, mapping)
        self.dataset = None
        self.format = None
        self._read()

    def _read(self):
        self.data = scipy.io.loadmat(self.input_file, struct_as_record=False)
        self.format = self._detect_format()
        if not self.format:
            raise ValueError(f"Could not detect ADCP format in {self.input_file}.")
        data_vars, coords = self._add_data_and_coords()
        self.dataset = xr.Dataset(data_vars=data_vars, coords=coords)
        # Assign meta information for all attributes of the xarray Dataset
        for key in (list(self.dataset.data_vars.keys()) + list(self.dataset.coords.keys())):
            super()._assign_metadata_for_key_to_xarray_dataset(self.dataset, key)

    def get_data(self):
        return self.dataset

    def _detect_format(self):
        keys = self.data.keys()
        if "dat_u" in keys and "dat_timesteps" in keys:
            return "v17"
        elif "SerYear" in keys and "RDIBin1Mid" in keys:
            return "v13"
        elif "DS_19_12_ndaysens" in keys and "DS_19_12_v" in keys:
            return "v12"
        elif "sens" in keys and "wt" in keys:
            return "v11"
        return None
    
    def _parse_time(self, arr, fmt):
        if fmt in ("v12", "v17"):
            time_raw = arr
            return pd.to_datetime(time_raw - 719529, unit="D")
        
        elif fmt == "v11":
            sens_struct = self.data['sens']
            if isinstance(sens_struct, np.ndarray):
                sens_struct = sens_struct[0, 0]

            time_raw = sens_struct.time
            if hasattr(time_raw, 'flatten'):
                time_raw = time_raw.flatten()
    
            return pd.to_datetime(time_raw, unit='s', errors='coerce')
        elif fmt == "v13":
            year = self.data['SerYear'].astype(np.int32).flatten()
            year = np.where(year > 50, year + 1900, year + 2000)
            month = self.data['SerMon'].flatten()
            day = self.data['SerDay'].flatten()
            hour = self.data['SerHour'].flatten()
            minute = self.data['SerMin'].flatten()
            second =  self.data['SerSec'].flatten() + self.data['SerHund'].flatten() / 100
            return pd.to_datetime({
                'year': year,
                'month': month,
                'day': day,
                'hour': hour,
                'minute': minute,
                'second': second
            })
    def _add_time(self):
        fmt = self.format
        if fmt == "v17":
            time = self._parse_time(self.data["dat_timesteps"].flatten(), fmt)

        elif fmt == "v12":
            time = self._parse_time(self.data["DS_19_12_ndaysens"].flatten(), fmt)
        
        elif fmt == "v13":
            time = self._parse_time(None, fmt)

        elif fmt == "v11":
            time = self._parse_time(self.data['sens'], fmt)

        else:
            raise ValueError(f"Unsupported format {fmt} for time parsing.")
        return time
    
    def _add_data_and_coords(self):
        fmt = self.format
        data_vars = {}
        coords = {}
        time = self._add_time()

        if fmt == "v17":
            depth_bins = self.data['dat_binrange'].flatten()
            coords = {
            "time": time,
            "bin": depth_bins,
        }
            data_vars = {
                ctdparams.EAST_VELOCITY: (("time", "bin"), self.data["dat_u"]),
                ctdparams.NORTH_VELOCITY: (("time", "bin"), self.data["dat_v"]),
                ctdparams.UP_VELOCITY: (("time", "bin"), self.data["dat_w"]),
                ctdparams.TEMPERATURE: (("time"), self.data['dat_t'].flatten()),
                ctdparams.ECHO_INTENSITY: (("time", "bin"), self.data['dat_echoa']),
                ctdparams.CORRELATION: (("time", "bin"), self.data['dat_corra']), 
                ctdparams.PITCH: (("time"), self.data['dat_pitch'].flatten()),
                ctdparams.ROLL: (("time"), self.data['dat_roll'].flatten()),
                ctdparams.HEADING: (("time"), self.data['dat_head'].flatten()),
                ctdparams.BATTERY_VOLTAGE: (("time"), self.data['dat_batt'].flatten()),
            }
        
        elif fmt == "v13":
            
            bin1_mid = np.squeeze(self.data.get("RDIBin1Mid", [np.nan]))
            bin_size = np.squeeze(self.data.get("RDIBinSize", [np.nan]))
            num_bins = self.data['SerBins'].shape[1]
            depth = bin1_mid + bin_size * np.arange(num_bins)
            
            coords = {
            "time": time,
            "bin": depth,
        }
            
            data_vars = {
                ctdparams.EAST_VELOCITY: (("time", "bin"), self.data['SerEmmpersec'] / 1000),  # mm/s to m/s
                ctdparams.NORTH_VELOCITY: (("time", "bin"), self.data['SerNmmpersec'] / 1000),
                ctdparams.UP_VELOCITY: (("time", "bin"), self.data['SerVmmpersec'] / 1000),
                ctdparams.TEMPERATURE: (("time"), self.data['AnT100thDeg'].flatten() / 100),
                ctdparams.ECHO_INTENSITY: (("time", "bin"), self.data['SerEA1cnt']),
                ctdparams.CORRELATION: (("time", "bin"), self.data['SerC1cnt']),
                ctdparams.DIRECTION: (("time", "bin"), self.data['SerDir10thDeg'] / 10),  # 10th degrees to degrees
                ctdparams.MAGNITUDE: (("time", "bin"), self.data['SerMagmmpersec'] / 1000),
                ctdparams.PITCH: (("time"), self.data['AnP100thDeg'].flatten() / 100),
                ctdparams.ROLL: (("time"), self.data['AnR100thDeg'].flatten() / 100),
                ctdparams.HEADING: (("time"), self.data['AnH100thDeg'].flatten() / 100),
                ctdparams.BATTERY_VOLTAGE: (("time"), self.data['AnBatt'].flatten() / 10),  # Tenths of volts
        }
            
    
        elif fmt == "v12":

            depth_bins = self.data['DS_19_12_binrange'].flatten()
            coords = {
            "time": time,
            "bin": depth_bins,
        }
            
            data_vars = {
                ctdparams.EAST_VELOCITY: (("time", "bin"), self.data['DS_19_12_u']),
                ctdparams.NORTH_VELOCITY: (("time", "bin"), self.data['DS_19_12_v']),
                ctdparams.UP_VELOCITY: (("time", "bin"), self.data['DS_19_12_w']),
                ctdparams.TEMPERATURE: (("time"), self.data['DS_19_12_t'].flatten()),
                ctdparams.ECHO_INTENSITY: (("time", "bin"), self.data['DS_19_12_echoa']),
                ctdparams.CORRELATION: (("time", "bin"), self.data['DS_19_12_corra']),
                ctdparams.PITCH: (("time"), self.data['DS_19_12_pitch'].flatten()),
                ctdparams.ROLL: (("time"), self.data['DS_19_12_roll'].flatten()),
                ctdparams.HEADING: (("time"), self.data['DS_19_12_head'].flatten()),
                ctdparams.BATTERY_VOLTAGE: (("time"), self.data['DS_19_12_batt'].flatten()),
        }

        elif fmt == "v11":
            
            sens_struct = self.data['sens']
            if isinstance(sens_struct, np.ndarray):
                sens_struct = sens_struct[0, 0]  # unwrap from ndarray container
            wt_struct = self.data['wt']
            if isinstance(wt_struct, np.ndarray):
                wt_struct = wt_struct[0, 0]

            # Extract data from 'sens' and 'wt'
            salinity = sens_struct.s.flatten()
            temperature = sens_struct.t.flatten()
            pitch = sens_struct.p.flatten()
            roll = sens_struct.r.flatten()
            heading = sens_struct.h.flatten()
            battery_voltage = sens_struct.v.flatten()
            east_velocity_raw = wt_struct.vel
            
            # Reshape the data to (n_time, total_depth)
            n_time, n_depth, n_velocity_components = east_velocity_raw.shape
            total_depth = n_depth * n_velocity_components 
            east_velocity = east_velocity_raw.reshape(-1, total_depth)

            depth_bins = wt_struct.r.flatten()
            coords = {
                "time": time,
                "depth_bin": depth_bins[:east_velocity.shape[1]],
            }

            # Organize data variables to return
            data_vars = {
                ctdparams.EAST_VELOCITY: (("time", "depth_bin"), east_velocity),
                ctdparams.TEMPERATURE: (("time"), temperature),
                ctdparams.SALINITY: (("time"), salinity),
                ctdparams.PITCH: (("time"), pitch),
                ctdparams.ROLL: (("time"), roll),
                ctdparams.HEADING: (("time"), heading),
                ctdparams.BATTERY_VOLTAGE: (("time"), battery_voltage),
            }

        return data_vars, coords
    
    def _add_metadata(self):
        # Add common metadata attributes
        self.dataset.attrs.update({
            "Conventions": "CF-1.8",
            "title": "ADCP Data",
            "source": "Acoustic Doppler Current Profiler",
        })

    @staticmethod
    def format_key() -> str:
        return 'adcp-matlab-uhhds'

    @staticmethod
    def format_name() -> str:
        return 'ADCP Matlab UHH DS'

    @staticmethod
    def file_extension() -> str | None:
        return None