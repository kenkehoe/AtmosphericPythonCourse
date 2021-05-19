#! /usr/bin/env python3

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from act.io.noaagml import read_gml
from act.plotting import TimeSeriesDisplay

# Get MET data
met_obj = read_gml(Path('data', 'met_brw_insitu_1_obop_hour_2021.txt'), datatype='MET')

# Get Ozone data
ozone_obj = read_gml(Path('data', 'brw_2021_04_hour.dat'), datatype='OZONE')

# Get Radiation Data
rad_obj = read_gml(Path('data', 'brw21120.dat'), datatype='RADIATION')

# Average data from 1 minute to 1 hour using Xarray modifier.
rad_obj_new = rad_obj.resample(time='60min').mean()

# After Xarray averages all the variables in the object the variables attribute
# values are dropped. We can add them back with a simple loop and reassign the
# object name. Most likely a "feature" Xarray introduced. It may be fixed in the future.
for var_name in rad_obj_new:
    rad_obj_new[var_name].attrs = rad_obj[var_name].attrs

rad_obj = rad_obj_new

# Reduce met data from full month to one day
met_obj = met_obj.sel(time=slice(rad_obj['time'].values[0], rad_obj['time'].values[-1]))

# MET and Ozone do not have location variables in the file. Add location variables
# from rad_obj to allow day/night background plotting.
for var_name in ['lat', 'lon', 'alt']:
    ozone_obj[var_name] = rad_obj[var_name]
    met_obj[var_name] = rad_obj[var_name]

# Create dictionary of all data objects to allow plotting from different
# Xarray Datasets.
location = "Barrow"
plot_obj = {'met': met_obj, 'rad': rad_obj, 'ozone': ozone_obj}
my_disp = TimeSeriesDisplay(plot_obj, subplot_shape=(3, ), figsize=(10, 8))

# Create first plot of two variables from Radiation file.
my_disp.plot('downwelling_global_solar', dsname='rad', subplot_index=(0, ), label='Downwelling')
my_disp.plot('upwelling_global_solar', dsname='rad', subplot_index=(0, ), label='Upwelling',
             set_title=f"NOAA GML {location} Global Solar",
             day_night_background=True)

# Add second plot of Ozone. Use variable long name for plot axes title
# and add background color to indicate when sun is shining and solar noon.
var_name = 'ozone'
title = f"NOAA GML {location} {ozone_obj[var_name].attrs['long_name']}"
my_disp.plot(var_name,  dsname='ozone', subplot_index=(1, ),
             set_title=title, day_night_background=True)

# Add a wind barb plot from Met datastream. Because the wind speeds are low modify
# the barb thresholds. Currently there is no legend for barbs, that is something
# that will be added in the future.
title = f"NOAA GML {location} Wind Barbs"
axes = my_disp.plot_barbs_from_spd_dir('wind_direction', 'wind_speed',  dsname='met',
                                subplot_index=(2, ), set_title=title,
                                day_night_background=True,
                                barb_increments={'half': 1, 'full': 2, 'flag': 3})
axes.set_ylim(0, 2)

plt.subplots_adjust(hspace=0.4)
plt.show()
