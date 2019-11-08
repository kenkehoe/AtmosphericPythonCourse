#! /usr/bin/env python3

'''
Xarry is a class of objects added to the regular python system that allows
storing data in a more organized method. The format is very similar to netCDF
classic model (netCDF3). It can read netCDF files very efficiently and handle
some issues associated with incorrectly designed netCDF files.

Xarray also has extetions to use the Numpy, Pandas, and SciPy libaries directly.
Think of Xarry as a tool for orgnaizing data in a way that other libaries can
be used on the data efficiently.

The primary difference between Xarray and Pandas is that Pandas can only
handle 1-D data while Xarray can handle n-D data.

The one downside is that Xarry has very powerful functions with
less than great documentation. May need to dig a bit to get the best
way to perform a task.

'''

import numpy as np
import xarray as xr
# import warnings
import pint

# Let's look at a simple instance of a Xarray object.
if True:
    # Here we create some data
    data = np.arange(10000, dtype=float)
    # Now we create the Xarray DataArray and add the data. The rest of the
    # stuff is automatically created in the DataArray.
    xr_da = xr.DataArray(data)
    print("\nxr_da:\n", xr_da)

if False:
    # Create some data
    data = np.arange(10000, dtype=float)
    # Create a time data array to match the data we created.
    time = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data.size)
    time = time.astype('datetime64[s]')  # This just addes :00 seconds to make it look correct.

    # Now we make the DataArray and tell it what is the coordinate dimention,
    # in this case time.
    xr_da = xr.DataArray(data, dims=['time'], coords=[time])
    print("\nxr_da:", xr_da, "\n")

    # Even better we can add attributes describing the data after we create the DataArray
    xr_da.attrs['long_name'] = 'Amazing data that will win me a Nobel prize.'
    xr_da.attrs['units'] = 'degK'
    xr_da.attrs['missing_value'] = np.nan
    xr_da.attrs['valid_min'] = 0.
    xr_da.attrs['valid_max'] = 10000.
    print("\nxr_da:", xr_da, "\n")

# The full power of Xarry comes from using Datasets. A Dataset is a collection of
# DataArrays. The beauty of Datasets is holding all the corresoponding data together
# and performing functions on multiple DataArrays in the Datasets all at once.
# This becomes very powerful and very fast!
if False:

    # Create some data
    data1 = np.arange(10000, dtype=float)
    data2 = np.arange(10000, dtype=float) + 123.456
    # Create a time data array to match the data we created.
    time = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data1.size)
    time = time.astype('datetime64[s]')  # This just addes :00 seconds to make it look correct.

    # Now we make the DataArray and tell it what is the coordinate dimention,
    # in this case time.
    da1 = xr.DataArray(data1, dims=['time'], coords=[time])
    # We are reuing the same coordinate dimention so we don't need to provide it
    # when we add the second variable. But we could, it would not hurt anything.
    da2 = xr.DataArray(data2, dims=['time'])

    # Create a new empty Xarary Dataset
    xr_ds = xr.Dataset()
    # Add the two DataArrays
    xr_ds['data1'] = da1
    xr_ds['data2'] = da2
    print("\nxr_da:", xr_ds, "\n")

    # Or we can create the Dataset from scratch. The DataArrays are created
    # automatically.
    xr_ds = xr.Dataset(
        # This is the data section.
        # Notice all data is wrappted in a dictionary. In that dict the key
        # is the variable name followed by a tuple. The first value of the tuple
        # is the dimension(s), folloed by the data values, followed by optional
        # dictionary of attributes as key:value pairs.
        data_vars={'data1': ('time', data1, {'long_name': 'Data 1 values', 'units': 'degC'}),
                   'data2': ('time', data2, {'long_name': 'Data 2 values', 'units': 'degF'})
                   },
        # This is the coordinate section following the same format. Since this
        # comes next it is intepreted as coordinates. But we are using keywords
        # to make it easier to understand.
        coords={'time': ('time', time, {'long_name': 'Time in UTC'})}
    )

    print("\nxr_da:", xr_ds, "\n")

if False:
    # Create some data
    data1 = np.arange(10000, dtype=float) + 32.
    data2 = np.arange(10000, dtype=float)
    # Create a time data array to match the data we created.
    time = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data1.size)
    time = time.astype('datetime64[s]')  # This just addes :00 seconds to make it look correct.

    # Create Dataset same as above.
    xr_ds = xr.Dataset(
        data_vars={'data1': ('time', data1, {'long_name': 'Data 1 values', 'units': 'degF'}),
                   'data2': ('time', data2, {'long_name': 'Data 2 values', 'units': 'degC'})},
        coords={'time': ('time', time, {'long_name': 'Time in UTC'})}
    )

    # But we need the units of the two data variables to be the same. Let's use Pint to fix that.
    desired_temp_unit = 'degK'  # The units we want
    ureg = pint.UnitRegistry()  # Set up the regestry object.

    # We can just get a list of all variables in the object instead of
    # typing their names. Notice the first print is more than the names.
    variables = xr_ds.data_vars
    print('variables:', variables, '\n')

    # When we convet to a list it automatically just has variable names.
    variables = list(xr_ds.data_vars)
    print('variables:', variables, '\n')

    # We loop over all the variables in the Dataset
    for var_name in variables:
        data = xr_ds[var_name].values  # Get the data from Xarray object.
#        print(type(data))

        # Now we use the units registry with the units in the Xarray objct
        # to tell Pint what units is the data in.
        xarry_units = xr_ds[var_name].attrs['units']
        data = data * ureg[xarry_units]
#        print(type(data))

        # Here we use a Pint method to change the units from to degK.
        data = data.to(ureg[desired_temp_unit])

        # We changed the data but we have not put it back into the Xarray object yet.
        # We don't want to put the Pint object back in, we need to extract
        # just the numerical values without the units attached.
        data = data.magnitude  # Get just the numerical part of the Pint object
        xr_ds[var_name].values = data

        # We changed the units but we need to update the attribute in the Xarray object
        # or else we will be very confused when we go to use the data.
        xr_ds[var_name].attrs['units'] = desired_temp_unit

    # Here we loop over each variable in the Dataset and print it.
    # Notice how the loop knows how to handle getting the variable name from the
    # the object when use .data_vars. I don't know how just condider it Python magic.
    if True:
        for var_name in xr_ds.data_vars:
            print(xr_ds[var_name])
            print()
