import xarray as xr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pint
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Read in one netCDF data file. Look at the default vs. optional for
# scalar variables.
if False:
    met_ds = xr.open_mfdataset('../data/sgpmetE13.b1/sgpmetE13.b1.20191101.000000.cdf',
                               combine='nested', concat_dim='time')
#    met_ds = xr.open_mfdataset('../data/sgpmetE13.b1/sgpmetE13.b1.20191101.000000.cdf',
#                               combine='nested', concat_dim='time', data_vars='minimal')

    print(met_ds)
    print(met_ds.data_vars)
    print(list(met_ds.data_vars))

# Read in netCDF data file and exclude some variables.
if False:
    drop_vars = ['base_time', 'time_offset', 'vapor_pressure_std', 'wspd_arith_mean',
                 'qc_wspd_arith_mean', 'wspd_vec_mean', 'qc_wspd_vec_mean',
                 'wdir_vec_mean', 'qc_wdir_vec_mean', 'wdir_vec_std', 'tbrg_precip_total',
                 'qc_tbrg_precip_total', 'tbrg_precip_total_corr', 'qc_tbrg_precip_total_corr',
                 'org_precip_rate_mean', 'qc_org_precip_rate_mean', 'pwd_err_code',
                 'pwd_mean_vis_1min', 'qc_pwd_mean_vis_1min', 'pwd_mean_vis_10min',
                 'qc_pwd_mean_vis_10min', 'pwd_pw_code_inst', 'qc_pwd_pw_code_inst',
                 'pwd_pw_code_15min', 'qc_pwd_pw_code_15min', 'pwd_pw_code_1hr',
                 'qc_pwd_pw_code_1hr', 'pwd_precip_rate_mean_1min',
                 'qc_pwd_precip_rate_mean_1min', 'pwd_cumul_rain', 'qc_pwd_cumul_rain',
                 'pwd_cumul_snow', 'qc_pwd_cumul_snow', 'logger_volt', 'qc_logger_volt',
                 'logger_temp', 'qc_logger_temp']
    met_ds = xr.open_mfdataset('../data/sgpmetE13.b1/sgpmetE13.b1.20191101.000000.cdf',
                               combine='nested', concat_dim='time', data_vars='minimal',
                               drop_variables=drop_vars)

    print(met_ds)

# Read in netCDF data files using command line syntax for regular expression.
if False:
    met_ds = xr.open_mfdataset('../data/sgpmetE13.b1/sgpmetE13.b1.*.cdf',
                               combine='nested', concat_dim='time')

    print(met_ds)

    del met_ds['atmos_pressure']
    del met_ds['qc_atmos_pressure']

    # Now that we have done somethign to the Xarray object lets write it to disk.
    # When you look at the file notice the number of time samples and missing
    # variables.
    met_ds.to_netcdf(path='our_written_file.nc')


if False:
    met_ds = xr.open_mfdataset('../data/sgpmetE13.b1/sgpmetE13.b1.20191101.000000.cdf',
                               combine='nested', concat_dim='time')

    met_ds['temp_mean'].plot()
    plt.show()


#    fig, axes = plt.subplots(nrows=2)
#    met_ds['temp_mean'].plot(ax=axes[0])
#
#    met_ds['rh_mean'].plot(ax=axes[1])
#    plt.show()

if False:
    ceil_ds = xr.open_mfdataset('../data/sgpceilC1.b1/sgpceilC1.b1.20191103.000012.nc',
                                combine='nested', concat_dim='time')

    # Make a plot. Things are not quite what you want. Where do we begin?
    # The plot is actually being made by pclormesh() call.
    ceil_ds['backscatter'].plot()
    plt.show()


# Lets pause with Xarray plotting and start with the true library that is making
# the plot, matplotlib. Once we understand what is going on underneath we can
# make the plots we want with the same/similar calls with Xarray.
if True:
    met_ds = xr.open_mfdataset('../data/sgpmetE13.b1/sgpmetE13.b1.20191104.000000.cdf',
                               combine='nested', concat_dim='time')

    var_name = 'temp_mean'
    var_name2 = 'rh_mean'

    if True:
        # Convert the units of the data
        desired_temp_unit = 'degF'
        ureg = pint.UnitRegistry()
        data = met_ds[var_name].values
        data = data * ureg[met_ds[var_name].attrs['units']]
        # Remember the data is in "pint" space now, not numpy only space. That means
        # the data is not going to work with the regular numpy or matplotlib functions.
        print('data.magnitude:', data.magnitude)
        print('data.units:', data.units)

        # Here we use a method to change the units from degC to degF.
        data = data.to(ureg[desired_temp_unit])
        print('\ndata:', data)
        print()

        # We changed the data but we have not put it back into the object yet.
        met_ds[var_name].values = data.magnitude
        # We changed the units but we need to update the attribute in the object
        # or else we will be very confused when we go to use the data.
        met_ds[var_name].attrs['units'] = desired_temp_unit
        # Deleting the data variable is not necessary but it does save space (not
        # really necessary) and stops us from using it incorrectly later.
        del data

    fig, axes = plt.subplots()
    line1 = axes.plot(met_ds['time'], met_ds[var_name], label='Temp')
    myFmt = mdates.DateFormatter('%H:%M')
    axes.xaxis.set_major_formatter(myFmt)

    # Get the first time value from the object
    first_time = met_ds['time'].values[0]
    print(first_time.astype('datetime64[ms]'))
    print(first_time.astype('datetime64[s]'))
    print(first_time.astype('datetime64[h]'))
    print(first_time.astype('datetime64[Y]'))
    print(first_time.astype('datetime64[D]'))

    # Change the precision of the time value from sub-second to day.
    # Then add one to that value to set the end of the range value.
    xrng = [first_time.astype('datetime64[D]'),
            first_time.astype('datetime64[D]') + 1]
    print(xrng)

    axes.set_xlim(xrng)  # Set the xrange for plot window

    # Now lets be a real scientist and add some axis labels
    y_label = met_ds[var_name].attrs['long_name']
    y_label = y_label + ' (' + met_ds[var_name].attrs['units'] + ')'
    axes.set_ylabel(y_label)

    # Set the x-axis label
    axes.set_xlabel('Time (UTC)')

    # But when you plot temperature you typically want to plot RH next.
    # How about on the same plot? (Wow mind blown!)
    axes_right = axes.twinx()
    line2 = axes_right.plot(met_ds['time'], met_ds[var_name2], color='green', label='RH')
    axes.legend()

    if False:
        # Add the two lines plotted to same list
        lines = line1+line2
        # Use list comprehension to get the label names we set in the plot
        # call and add them to a list to pass along to the legend call.
        labels = [l.get_label() for l in lines]
        # Now we make the legend with the list of lines plotted (gets color)
        # and the label names we want to display.
        axes.legend(lines, labels)

    y_label2 = met_ds[var_name2].attrs['long_name']
    y_label2 = y_label2 + ' (' + met_ds[var_name2].attrs['units'] + ')'
    axes_right.set_ylabel(y_label2)

    # The xaxis shares the same values but we updated the orginal format
    # of the axis. The right plot did not update the plot for the xaxis for us.
    # To get the axis to look correct just update the xaxis again.
    axes.xaxis.set_major_formatter(myFmt)

    # And the most important part of all, a title.
    axes.set_title(('An amazing plot of Temp. and RH. '
                    'on {}').format(first_time.astype('datetime64[D]')))

    if True:
        plt.show()  # Show the plot in a new window
    else:
        # Save the figure to a file
        plt.savefig('temperature_plot.jpg')
