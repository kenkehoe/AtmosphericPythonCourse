#! /usr/bin/env python3

import numpy as np
import xarray as xr
from pathlib import Path
import act
import matplotlib.pyplot as plt
import matplotlib


# First things first. Let's read some data
if True:
    # Make a file path to data file to read. Notice how we create the path using
    # pathlib but need to convert it to a standard string using str(). Xarray
    # does not currently work with pathlib.
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.*.cdf'))

    if True:
        # Using Xarray we can read one file using .open_dataset() method or if there is
        # more than one file to read the .open_mfdataset() method. Instead of needing to
        # know the details of xarray reading methods, we can just use the ACT method which
        # is a wrapper arround .open_mcdataset(). Notice how the filename uses a * character
        # to allow us to read all files matching in the directory. This is a feature of xarray
        # open_mfdataset().

        # Notice that this met_ds object is just an Xarray object with a few extra global
        # attributes added. These are used for plotting lables and titles. All the Xarray
        # methods will work on this object.
        met_ds = act.io.armfiles.read_netcdf(filename)
        print(met_ds)

    if False:
        # If the file does not exist xarray will through an error. But ACT can be told to
        # not throw an error, return None instead.
        filename2 = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.cdf'))
        met_ds = act.io.armfiles.read_netcdf(filename2, return_None=True)
        print(met_ds)

    if False:
        # All the keywords accepted by .open_mfdataset() can be passed into the ACT
        # reader.
        drop_vars = ['base_time', 'time_offset', 'temp_mean', 'qc_temp_mean',
                     'temp_std', 'rh_mean', 'qc_rh_mean', 'rh_std', 'vapor_pressure_mean',
                     'qc_vapor_pressure_mean', 'vapor_pressure_std', 'wspd_arith_mean',
                     'qc_wspd_arith_mean', 'wspd_vec_mean', 'qc_wspd_vec_mean', 'wdir_vec_mean',
                     'qc_wdir_vec_mean', 'wdir_vec_std', 'tbrg_precip_total',
                     'qc_tbrg_precip_total', 'tbrg_precip_total_corr',
                     'qc_tbrg_precip_total_corr', 'org_precip_rate_mean',
                     'qc_org_precip_rate_mean', 'pwd_err_code', 'pwd_mean_vis_1min',
                     'qc_pwd_mean_vis_1min', 'pwd_mean_vis_10min', 'qc_pwd_mean_vis_10min',
                     'pwd_pw_code_inst', 'qc_pwd_pw_code_inst', 'pwd_pw_code_15min',
                     'qc_pwd_pw_code_15min', 'pwd_pw_code_1hr', 'qc_pwd_pw_code_1hr',
                     'pwd_precip_rate_mean_1min', 'qc_pwd_precip_rate_mean_1min',
                     'pwd_cumul_rain', 'qc_pwd_cumul_rain', 'pwd_cumul_snow',
                     'qc_pwd_cumul_snow', 'logger_volt', 'qc_logger_volt', 'logger_temp',
                     'qc_logger_temp']
        met_ds = act.io.armfiles.read_netcdf(filename, drop_variables=drop_vars)
        print(met_ds)


# Units are an under appreciated aspect of data. All netCDF files should use 'units' attribute
# under each variable to correctly describe the data. Xarray does not have methods to update
# units directly, but there is a library extension being developed to work with units. It has some issues
# and does not preserve attribute order. To keep attributes more similar to CF ACT has its own
# units method. It can also update units on a coordinate variable which is a litte more difficult
# with Xarray due to the way coordinate values are modified.
#
# https://github.com/ARM-DOE/ACT/blob/master/examples/change_units.py
#
if False:
    drop_vars = ['base_time', 'time_offset', 'qc_temp_mean', 'lat', 'lon', 'alt',
                 'qc_rh_mean', 'vapor_pressure_mean',
                 'qc_vapor_pressure_mean', 'vapor_pressure_std', 'wspd_arith_mean',
                 'qc_wspd_arith_mean', 'wspd_vec_mean', 'qc_wspd_vec_mean', 'wdir_vec_mean',
                 'qc_wdir_vec_mean', 'wdir_vec_std', 'tbrg_precip_total',
                 'qc_tbrg_precip_total', 'tbrg_precip_total_corr',
                 'qc_tbrg_precip_total_corr', 'org_precip_rate_mean',
                 'qc_org_precip_rate_mean', 'pwd_err_code', 'pwd_mean_vis_1min',
                 'qc_pwd_mean_vis_1min', 'pwd_mean_vis_10min', 'qc_pwd_mean_vis_10min',
                 'pwd_pw_code_inst', 'qc_pwd_pw_code_inst', 'pwd_pw_code_15min',
                 'qc_pwd_pw_code_15min', 'pwd_pw_code_1hr', 'qc_pwd_pw_code_1hr',
                 'pwd_precip_rate_mean_1min', 'qc_pwd_precip_rate_mean_1min',
                 'pwd_cumul_rain', 'qc_pwd_cumul_rain', 'pwd_cumul_snow',
                 'qc_pwd_cumul_snow', 'logger_volt', 'qc_logger_volt',
                 'qc_logger_temp', 'atmos_pressure', 'qc_atmos_pressure']
    filename = Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.000000.cdf')
    met_ds = act.io.armfiles.read_netcdf(str(filename), drop_variables=drop_vars)
    print('\nInitial variables:')
    for var_name in met_ds:
        print('   ', var_name, met_ds[var_name].attrs['units'])

    # A single variable can be updated with a method call and the variable name
    var_name = 'temp_mean'
    met_ds.utils.change_units(variables=var_name, desired_unit='degK')
    print('\nUpdated variable:\n  ', var_name, met_ds[var_name].attrs['units'])

    # Or all the variabls in the dataset can be updated if the units are compatible
    # by ommiting the varible name. Notice how the relative humidity variables are not
    # affected because the desired unit is a temperature which is not a compatible
    # update.
    met_ds.utils.change_units(desired_unit='degK')
    print('\nAll units updated:')
    for var_name in met_ds:
        print('  ', var_name, met_ds[var_name].attrs['units'])


# ARM uses an older format for embedded quality control. We can convert the embedded QC to follow
# CF format for use with other tools.
if False:
    # Make a file path to data file to read.
    filename = Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.000000.cdf')
    met_ds = act.io.armfiles.read_netcdf(str(filename), drop_variables=['base_time', 'time_offset'])
    print(met_ds['qc_atmos_pressure'])

    # Call the cleanup method to go through each quality control variable and update
    # to CF standards. Other datasets can be added in the future. This also fixes the units
    # since uduints does not recognize "unitless" as a unit. Will also create a linkage
    # from the data variable to the quality control varible using CF standard linking.
    met_ds.clean.cleanup()
    print("\n", met_ds['qc_atmos_pressure'])

    # After cleaning up the quality control variables we can write the file to a
    # netCDF file. We can call the Xarray to_netcdf() method directly, or use the ACT
    # method which will cleanup a few things to make the file match CF and add the
    # CF-1.8 string to the Conventions global attribute.
    print(f"Writing file: {filename.name}")
    met_ds.write.write_netcdf(path=str(filename.name))


if False:
    # One of the drivers for ACT is making plotting easier. It has methods to work with
    # matplotlib to plot the data stored in the xarray dataset to correctly plot the data
    # based on data shape. From our plotting examples we needed to know what matplotlib
    # function to call for 1-D or 2-D data. ACT will guess what you want and make the
    # plot for you, including axes labels, units, coordinate variable and a day/night
    # background with local solar noon.
    filename = str(Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.b1.20191101.000000.cdf'))
    met_ds = act.io.armfiles.read_netcdf(filename)
    display = act.plotting.TimeSeriesDisplay(met_ds, figsize=(15, 10))
    display.plot('temp_mean', linestyle='solid', day_night_background=True)
    plt.show()


if False:
    # 2D plots can be a bit more difficult so ACT has done much of the heavy work
    # for you. The set up is the same to create the display object and the timeseries
    # method to plot is the same .plot(). This will also allow for passing pcolormesh
    # specific keywords to plot in log values. The x and y axis show units in correct
    # format and a colorbar is added.
    filename = str(Path('..', 'data', 'sgpceilC1.b1', 'sgpceilC1.b1.20191103.000012.nc'))
    ceil_ds = act.io.armfiles.read_netcdf(filename)

    # We can change the data to a log scale for better plotting.
    var_name = 'backscatter'
    display = act.plotting.TimeSeriesDisplay(ceil_ds, figsize=(15, 10))
    title = (r"Plot of $\log_{10}$ " f"{var_name} from {ceil_ds.attrs['datastream']} on "
             f"{ceil_ds.attrs['_file_dates'][0]}")
    colorbar_label = r"$\log_{10}$" + ceil_ds[var_name].attrs['units']
    display.plot(var_name, norm=matplotlib.colors.LogNorm(), set_title=title,
                 cbar_label=colorbar_label)
    plt.show()
