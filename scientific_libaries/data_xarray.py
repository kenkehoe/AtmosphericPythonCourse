#! /usr/bin/env python3

'''
Xarry is a class of objects added to the regular python system that allows
storing data in a more organized method. The format is very similar to netCDF
classic model (netCDF3). It can read netCDF files efficiently and handle
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
import pint

# Block 1
# Let's look at a simple instance of a Xarray object. This is the simplest
# form of a DataArray just data values. The data in these examples are
# stored as numpy arrays.
if True:
    # Here we create some data.
    data = np.arange(10000)  # This is a numpy array
    data = range(10000)  # This is a python list
    # Now we create the Xarray DataArray and add the data.
    xr_da = xr.DataArray(data)
    print("\nxr_da:\n", xr_da)
    print("\ntype(xr_da):\n", type(xr_da))
    print("\ntype(xr_da.values):\n", type(xr_da.values))

# Block 2
if False:
    # Create some data
    data = np.arange(10000, dtype=int)
    # Create a time data array to match the data we created.
    # This will be one minute time steps.
    time = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data.size)
    time = time.astype('datetime64[s]')  # This just addes :00 seconds to make it look correct.

    # Now we make the DataArray and tell it what is the coordinate dimention,
    # in this case time. Note that the time coords must be entered as a container
    # eiter tuple or list.
    xr_da = xr.DataArray(data, dims=['time'], coords=[time])
    print("\nxr_da 1:", xr_da, "\n")

    # We can add attributes describing the data after we create the DataArray
    xr_da.attrs['long_name'] = 'Amazing data that will win me a Nobel prize.'
    xr_da.attrs['units'] = 'degK'
    xr_da.attrs['missing_value'] = -9999
    xr_da.attrs['valid_min'] = 0.
    xr_da.attrs['valid_max'] = 10000.

    # Print the DataArray
    print("\nxr_da 2:", xr_da, "\n")

    print("\nxr_da.values:", xr_da.values)
    # Print the attributes of the DataArray. Notice that it is returned
    # as a dictionary with the attribute names as the dictionary keys.

    print("\nxr_da.attrs:", xr_da.attrs)
    # Print a single attribute value

    print("\nxr_da.attrs['long_name']:", xr_da.attrs['long_name'])

    print()


# Block 3
# The full power of Xarry comes from using Datasets. A Dataset is a collection of
# DataArrays. The beauty of Datasets is holding all the corresoponding data together
# and performing functions on multiple DataArrays in the Datasets all at once.
# This becomes very powerful and very fast!
if False:

    # Create some data
    data1 = np.arange(10000, dtype=float)
    data2 = np.arange(10000, dtype=float) + 123.456
    # Create a time data array to match the data we created with minute time steps.
    time = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data1.size)
    time = time.astype('datetime64[s]')  # This just addes :00 seconds to make it look correct.

    # Now we make the DataArray and tell it what is the coordinate dimention,
    # in this case time.
    da1 = xr.DataArray(data1, dims=['time'], coords=[time])
    # We are reusing the same coordinate dimention so we don't need to provide the values
    # when we add the second variable. But we could, it would not hurt anything.
    da2 = xr.DataArray(data2, dims=['time'])

    # Create a new empty Xarary Dataset
    xr_ds = xr.Dataset()
    # Add the two DataArrays
    xr_ds['data1'] = da1
    xr_ds['data2'] = da2
    if True:
        print("\nxr_da:\n", xr_ds, "\n")

    # Or we can create the Dataset from scratch all at once. The DataArrays inside the
    # Dataset are created automatically.
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
        # comes next it could be interpredted as positional as coordinates.
        # But we are using keywords to make it easier to understand.
        coords={'time': ('time', time, {'long_name': 'Time in UTC'})}
    )

    if False:
        # Print out the full Dataset
        print("\nxr_da:\n", xr_ds)

        # Print out one DataArray from the Dataset
        print("\nxr_da['data1']:\n", xr_ds['data1'])

        # Print out one attribute from one DataArray
        print("\nxr_ds['data1'].attrs['units']:", xr_ds['data1'].attrs['units'])

# Block 4
# Let's look at an example of using the organization of Datasets to fix a problem with
# differing units. This will also show us how we will extract the data data to perform
# some operation on it and put the updated data and attribures back into the Dataset.
if False:
    # Create some data
    data1 = np.arange(10, dtype=float) + 32.
    data2 = np.arange(10, dtype=float)
    # Create a time data array to match the data we created.
    time = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data1.size)
    time = time.astype('datetime64[s]')  # This just addes :00 seconds to make it look correct.

    # Create Dataset same as above.
    xr_ds = xr.Dataset(
        data_vars={'data1': ('time', data1, {'long_name': 'Data 1 values', 'units': 'degF'}),
                   'data2': ('time', data2, {'long_name': 'Data 2 values', 'units': 'degC'})},
        coords={'time': ('time', time, {'long_name': 'Time in UTC'})}
    )

    # But we need the units of the two data variables to be the same.
    # Let's use Pint to fix that.
    desired_temp_unit = 'degK'  # The units we want
    unit_registry = pint.UnitRegistry()  # Set up the regestry object.

    if True:
        # Using the .data_vars method on the Dataset we can get a list of all
        # variables in the object instead of typing their names.
        # Notice the print out is more than the names.
        print('\nxr_ds.data_vars:\n', xr_ds.data_vars)

        # When we convet it to a list it automatically just has variable names.
        print('\nlist(xr_ds.data_vars):\n', list(xr_ds.data_vars))
        print()

    # We loop over all the variables in the Dataset. Notice some magic here
    # where the loop knows how to extract the variable names only and sets
    # the var_name for each itteration to the variable name not the full
    # DataArray.
    for var_name in xr_ds.data_vars:
        data = xr_ds[var_name].values  # Get the data as numpy arrays from Xarray object.
#        print(var_name, type(data))

        # Now we use the units registry with the units in the Xarray objct
        # to tell Pint what units the data are in. This is following the CF
        # netCDF data file standard for units as the attribute name.
        xarry_units = xr_ds[var_name].attrs['units']
        data = data * unit_registry.parse_expression(xarry_units)
#        print(var_name, data)
#        print(var_name, type(data))
#        print()

        # Here we use a Pint .to method to change the units from the current units
        # stored in the pint.quantity to units of degK.
        desired_unit_registry = unit_registry.parse_expression(desired_temp_unit)
        data = data.to(desired_unit_registry)

        # We changed the data but we have not put it back into the Xarray object yet.
        # We don't want to put the pint.quantity back in, we need to extract
        # just the numerical values without the units attached.
        data = data.magnitude  # Get just the numerical part of the Pint object
        xr_ds[var_name].values = data

        # We changed the units but we need to update the attribute in the DataArray 
        # or else we will be very confused when we go to use the data.
        xr_ds[var_name].attrs['units'] = desired_temp_unit

    # Here we loop over each variable in the Dataset and print it.
    # Notice how the loop knows how to handle getting the variable name from the
    # the object when use .data_vars. The first value of data1 was 32 degF and the
    # first value of data2 was 0 degC. Both have been convereted into 273.15 degK.
    if False:
        for var_name in xr_ds.data_vars:
            print(xr_ds[var_name])
            print()
