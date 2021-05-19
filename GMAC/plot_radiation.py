#! /usr/bin/env python3

from pathlib import Path
import matplotlib.pyplot as plt
from act.io.noaagml import read_gml
from act.plotting import TimeSeriesDisplay

# Here is an example of plotting GML radiation data. The data were downloaded and
# put localally for reading. The data are in CSV format with no variable
# header information. The information about each variable is listed in another
# metadata file avaialbe from NOAA GML website. This informaiton is encoded in
# the reading routine to add important attributes to the variables.
#
# Notice that we need to provide the full or relative path to data files as a
# list but the reading will read multiple files and concatinate together into
# a single Xarray Dataset with updated variable attributes.
#
# Then we can use the ACT plotting methods to set up the matplotlib plotting object
# and add some cool additinal features. The x-axis is correctly formatted to time
# with good looking labels, y-axis shows the units of the data plotted, and 
# we add a day/night/noon background using the location infomation provided in
# the data file. Coding this up from scratch will be a lot of additional programming.

# Get the data filenames for two days.
files = list(Path('data').glob('brw21[0-9][0-9][0-9].dat'))

# Sort filenames to ensure data is read in correct order
files.sort()

# Read in data. This will read in one or more files and do a bit of work
# updating the variable attributes with units, long_name and quality
# control variables.
ds_obj = read_gml(files)

# Change variable units from degree C to degree F. Can specify specific variables.
# Or list no variables and will attempt to change all variables to the desired
# unit if the units are conicially matching.
ds_obj = ds_obj.utils.change_units(variables='air_temperature_10m', desired_unit='degF')

# Set up plotting ACT object to contain data to plot and other configurations
my_disp = TimeSeriesDisplay({'noaa_gml_brw': ds_obj}, subplot_shape=(2, ), figsize=(15, 10))

# Plot two variables on one plot and set the plot axes title. Also color
# background to indicate when sun is shining and local solar noon time.
my_disp.plot('downwelling_global_solar', subplot_index=(0, ), label='Downwelling')
my_disp.plot('upwelling_global_solar', subplot_index=(0, ), label='Upwelling',
             set_title=f"NOAA GML {ds_obj.attrs['location']} Global Solar",
             day_night_background=True)

# Add second plot of air temperature. Use variable long name for plot axes title
# and add background color to indicate when sun is shining and solar noon.
var_name = 'air_temperature_10m'
title = f"NOAA GML {ds_obj.attrs['location']} {ds_obj[var_name].attrs['long_name']}"
my_disp.plot(var_name, subplot_index=(1, ), set_title=title, day_night_background=True)
plt.show()
