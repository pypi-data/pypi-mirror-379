import os
from datetime import datetime
from math import ceil, floor
from pathlib import Path
from typing import Literal, Optional

import cdsapi
import metpy.calc as metcalc
import metpy.units as metunits
import numpy as np
import numpy.typing as npt
import xarray as xr
from siphon.catalog import TDSCatalog
from xarray.backends import NetCDF4DataStore

from ..queryreport import print_text


class NetcdfMet:
    def __init__(self, file: str):
        self._file = file

        self._open = False

        self.altitude = np.empty((0), dtype=np.float64)
        self.wind_U = np.empty((0), dtype=np.float64)
        self.wind_V = np.empty((0), dtype=np.float64)
        self.wind_speed = np.empty((0), dtype=np.float64)
        self.wind_direction = np.empty((0), dtype=np.float64)
        self.temperature = np.empty((0), dtype=np.float64)
        self.pressure = np.empty((0), dtype=np.float64)
        self.density = np.empty((0), dtype=np.float64)

        self._time_coord = None


    def close(self):
        if self._open:
            self._data.close()
            self._open = False

    @property
    def file(self) -> str:
        return self._file
    
    @property
    def data(self) -> xr.Dataset:
        if not self._open:
            dat = xr.load_dataset(self._file, engine='netcdf4')
            dat = dat.metpy.parse_cf() # read metadata
            self._data = dat
            self._open = True
        return self._data

    def _get_time_coord(self):
        if 'valid_time' in self.data.coords:
            self._time_coord = 'valid_time'
        elif 'time' in self.data.coords:
            self._time_coord = 'time'
        else:
            self._time_coord = None
            Warning(f'time coordinate not recognized in {self._file}')
            

    @property
    def time_coord(self) -> str | None:
        if self._time_coord is None:
            self._get_time_coord()
        return self._time_coord

    @property
    def latitude(self) -> npt.NDArray:
        return self.data.latitude.values
    
    @property
    def longitude(self) -> npt.NDArray:
        return self.data.longitude.values
    
    @property
    def time(self) -> npt.NDArray:
        return self.data[self.time_coord].values
        
    @property
    def extent(self) -> list[float]:
        return [self.longitude.min(), self.longitude.max(), self.latitude.min(), self.latitude.max()]
    
    def _in_extent(self, lat: float, lon: float) -> bool:
        lon_min, lon_max, lat_min, lat_max = self.extent
        return (lon_min <= lon <= lon_max) and (lat_min <= lat <= lat_max)
    
    def _in_timespan(self, datetime: datetime) -> bool:
        return np.datetime64(datetime) in self.time
    
    def _check_file_exists(self, verbose: bool=True) -> bool:
        if os.path.isfile(self.file):
            if verbose:
                print_text(f"Met file {self.file} exists and will be overwritten")
            return True
        else:
            return False
        
    def _check_lat_lon(self, lat: float, lon: float, verbose: bool=True) -> bool:
        if not self._in_extent(lat, lon):
            if verbose:
                print_text(f"Location {lat}, {lon} not in extent of {self.file}")
            return False
        return True

    def _check_datetime(self, datetime: datetime, verbose: bool=True) -> bool:
        if not self._in_timespan(datetime):
            if verbose:
                print_text(f"Time {datetime} not in timespan of {self.file}")
            return False
        return True
    
    @staticmethod
    def _check_set_location( 
                        lat: float | None, 
                        lon: float | None, 
                        extent: list[float] | None) -> None:
        if (lat is None) and (lon is None):
            if extent is None:
                    raise ValueError('set either lat and lon, or extent')
        else:
            if (lat is None) or (lon is None):
                raise ValueError('set both lat and lon')
            
    @staticmethod
    def _make_extent_from_latlon(lat, lon) -> list[float]:
        extent = [0.25*floor(lon/0.25), 
                  0.25*ceil(lon/0.25), 
                  0.25*floor(lat/0.25),
                  0.25*ceil(lat/0.25)]
        return extent
    
    @staticmethod
    def _check_set_time( 
                    datetime: datetime | None,
                    year: list[int] | None,
                    month: list[int] | None,
                    day: list[int] | None,
                    hour: list[int] | None):
        if ((datetime is not None) and any([year, month, day, hour])):
                raise ValueError('set only datetime and none of year, month, day and hour')
        else:
            if not all([year, month, day, hour]):
                raise ValueError('set either datetime or all of year, month, day and hour')

    @staticmethod
    def _split_datetime_to_dict(datetime: datetime) -> dict[str, list[int]]:
        return {
            'year': [datetime.year],
            'month': [datetime.month],
            'day': [datetime.day],
            'hour': [datetime.hour],
        }
    
    @staticmethod
    def _build_ymdh_to_dict(year: list[int], 
                            month: list[int], 
                            day: list[int], 
                            hour: list[int]) -> dict[str, list[int]]:
        return {
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
        }

    def download(self, *,
                 lat: float | None = None, 
                 lon: float | None = None, 
                 datetime: datetime | list[datetime] | None = None,
                 extent: list[float] | None =None,
                 year: int | list[int] | None =None,
                 month: int | list[int] | None =None,
                 day: int | list[int] | None =None,
                 hour: int | list[int] | None =None) -> None:
        
        _ = self._check_file_exists(verbose=True)

        self._check_set_location(lat, lon, extent)

        self._check_set_time(datetime, year, month, day, hour)

        if datetime is not None:
            self._ymdh = self._split_datetime_to_dict(datetime)
        else:
            self._ymdh = self._build_ymdh_to_dict(year, month, day, hour)

        if not extent:
            self._extent = self._make_extent_from_latlon(lat, lon)

        if extent is None:
            self._extent = self._make_extent_from_latlon(lat, lon)

        # Extend download for each subclass
        self._download_custom()

    def _download_custom(self) -> None:
        """Hook download method.  Subclasses override this."""
        pass
        

    def extract(self, lat: float, lon: float, datetime: datetime, convention: Literal["to", "from"]="to"):
        
        if not self._check_lat_lon(lat, lon, verbose=True):
            return
        
        if not self._check_datetime(datetime, verbose=True):
            return

        # Extend extract for each subclass
        self._extract_custom(lat, lon, datetime, convention)
        
    def _extract_custom(self, lat: float, lon: float, datetime: datetime, convention: Literal["to", "from"]="to"):
        """Hook extract method.  Subclasses overide this."""
        pass
        

class ERA5(NetcdfMet):
    def __init__(self, file: str):

        super().__init__(file)

    def _extract_custom(self, lat: float, lon: float, datetime: datetime, convention: Literal["to", "from"]="to"):
        
        data0 = self.data.sel(valid_time=datetime).interp(latitude=lat, longitude=lon, method='linear').metpy.quantify()

        geopot = data0['z']
        Z = metcalc.geopotential_to_height(geopot)
        Z = Z.metpy.convert_units("m")

        self.altitude = np.float64(Z.values)

        U = data0['u'].metpy.convert_units("m/s")
        V = data0['v'].metpy.convert_units("m/s")
        T = data0['t'].metpy.convert_units("K")
        RH = data0['r'].metpy.convert_units("%")
        P = data0['pressure_level']
        spd = metcalc.wind_speed(U,V)
        dir = metcalc.wind_direction(U,V, convention=convention)

        self.wind_U = np.float64(U.values)
        self.wind_V = np.float64(V.values)
        self.wind_speed = np.float64(spd.values)
        self.wind_direction = np.float64(dir.values)
        self.temperature = np.float64(T.values)
        self.relhum = np.float64(RH.values)
        self.pressure = np.float64(P.metpy.convert_units("Pa").values)

        mixing_ratio = metcalc.mixing_ratio_from_relative_humidity(P,T,RH)
        rho = metcalc.density(P,T,mixing_ratio)
        rho = rho.metpy.convert_units("kg/m^3")
        self.density = rho.values

    def _download_custom(self):
        
        # Check .cdsapi exists in $HOME
        home_dir = Path.home()
        cdsapirc = home_dir / ".cdsapirc"
        if not cdsapirc.exists():
            raise FileNotFoundError(f"Cannot find {cdsapirc} -- see https://cds.climate.copernicus.eu/how-to-api")

        cds_dataset = "reanalysis-era5-pressure-levels"
        cds_request = {
            "product_type": "reanalysis",
            "format": "netcdf",
            "variable": [
                "geopotential",
                "temperature",
                "relative_humidity",
                "u_component_of_wind",
                "v_component_of_wind",
            ],
            "pressure_level": [
                "1","2","3","5","7","10","20","30","50","70",
                "100","125","150","175","200","225","250","300",
                "350","400","450","500","550","600","650","700","750",
                "775","800","825","850","875","900","925","950","975","1000",
            ],
            "year": [str(yr) for yr in self._ymdh['year']],
            "month": ["{:02d}".format(mnth) for mnth in self._ymdh['month']],
            "day": ["{:02d}".format(d) for d in self._ymdh['day']],
            "time": ["{:02d}:00".format(hr) for hr in self._ymdh['hour']],
            "area": [
                self._extent[3], # max lat
                self._extent[0], # min lon
                self._extent[2], # min lat
                self._extent[1], # max lon
            ],
            "data_format": "netcdf",
            "download_format": "unarchived",
        }

        try:
            cds = cdsapi.Client()
            cds.retrieve(cds_dataset, cds_request).download(self.file)
        except:
            raise UserWarning(f"Failed to download ERA5 data.  Check the Climate Data Store at https://cds.climate.copernicus.eu/")


class GFSForecast(NetcdfMet):

    def __init__(self, file: str):

        super().__init__(file)

    def _download_custom(self) -> None:
        
        gfs = TDSCatalog(
            "http://thredds.ucar.edu/thredds/catalog/grib/NCEP/GFS/Global_0p25deg/catalog.xml"
            "?dataset=grib/NCEP/GFS/Global_0p25deg/Best"
        )
        gfs_ds = gfs.datasets[0]
        ncss = gfs_ds.subset()
        query = ncss.query()
    
        query.lonlat_box(east=self._extent[0], west=self._extent[1], south=self._extent[2], north=self._extent[3])
        query.time(met_datetime)