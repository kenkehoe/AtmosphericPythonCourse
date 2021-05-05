#! /usr/bin/env python3

'''
This is contineuation of the Xarray module with some more advanced topics.

'''
import numpy as np
import xarray as xr
import copy
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Block 1
if True:
    # Create some data. data1 is integer type and data2 is float type just to show
    # we can do that. data2 is also multiplied by 3.
    num = 100
    data1 = np.arange(0, num, dtype=int)
    data2 = np.arange(0, num, dtype=float) * 3.

    # Make two additional arrays at half the size by stepping by 2.
    data3 = np.arange(0, num, 2, dtype=int)
    # Make the second additional array have some random noise on the data.
    data4 = (np.arange(0, num, 2, dtype=float) +
             np.random.uniform(low=-20, high=20, size=data3.size))

    # Create a datetime64 array with 1 minute time steps to match the size of data1 we created.
    time1 = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data1.size)
    time1 = time1.astype('datetime64[s]')  # Set precision to second.

    # Make time array to match data3 size over the same range (half the size of data1).
    time3 = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data3.size)
    # Add random seconds from 0 to 30 to each time value
    time3 = time3.astype('datetime64[s]') + np.random.randint(-30, 30, time3.size)

    if True:
        print(data1.size, data3.size)
        print(time1.size, time3.size)
        print()

    # Create Dataset 1
    xr_ds1 = xr.Dataset(
        data_vars={'data1': ('time', data1), 'data2': ('time', data2)},
        coords={'time': ('time', time1)})

    # Create Dataset 2
    xr_ds2 = xr.Dataset(
        data_vars={'data3': ('time', data3), 'data4': ('time', data4)},
        coords={'time': ('time', time3)})

    if False:
        # Using .loc will locate useing label based indexing along a dimension.
        # Here we look for datetimes that fall within the range. The xr_result
        # is a new DataArray with fewer time samples.
        xr_result = xr_ds1['time'].loc['2019-11-01T00:05:01':'2019-11-01T00:15:00']
        print(type(xr_result))
        print(xr_result)
        print()

        # Here we will make a copy of data1 DataArray and save under a different
        # name. This allows us to mess with it an not change the values in the Dataset.
        # Note even though we are not explicity extracting time as well we can still
        # perform operations on the time dimention.
        xr_da_data1 = copy.deepcopy(xr_ds1['data1'])

        # Now we can use label based indexing to determine locations in the DataArray
        # and change the values. We will use a time range to determine where to change
        # the data values to a new value.
        xr_da_data1.loc['2019-11-01T00:04:59':'2019-11-01T00:59:00'] = -9999
        print(xr_da_data1)

    if False:
        # Here we are going to match the times from Dataset 1 to Dataset 2.
        # We use the select [.sel()] method to indicate where we want to select values
        # from Dataset 1 using the times from Dataset 2. It will use the nearest value
        # in time for matching. Notice the magic of how all the variables in the
        # Dataset are selected. There are now 50 values.
        ds_result = xr_ds1.sel(time=xr_ds2['time'], method='nearest')
        print("\nds_result:\n", ds_result)
        print("\ntype(ds_result)\n:", type(ds_result))

    if False:
        # Or we can use .sel to perform a selection of a range
        # across the full Dataset with the slice() function.
        # Notice the magic of how all the variables in the
        # Dataset are selected. The time dimension is reduced to size 11 from 100.
        ds_result = xr_ds1.sel(time=slice('2019-11-01T00:04:59', '2019-11-01T00:15:00'))
        print("\nds_result:\n", ds_result)

    if False:
        # But what if we have a large gap and the nearest value falls outside
        # a tolerable range. We can use .reindex method with a toleracne to indicate
        # which values should be matched. The values that don't have a match are
        # set to NaN. We need to use timedelta64() to set the tolerance value which
        # includes a time unit. Remember we added a random 0 - 30 seconds to the
        # time values. Notice the magic of how all the variables in the
        # Dataset are updated. The size of the dataset is still 100 samples, just
        # where a match could not be found it inserts NaN for data. Time step
        # is still in the time coordinate.
        ds_result = xr_ds2.reindex(time=xr_ds1['time'], method='nearest',
                                   tolerance=np.timedelta64(20, 's'))

        # If no values match within tollerence it will still make
        # a new Dataset with all the time steps, but the data will all be set to
        # NaN. Also notice how the integer arrays have been upcasted to float
        # to allow setting the values to NaN.
        print("\nds_result:\n", ds_result)

    if False:
        # Here we are merging two Datasets into one. We need to be a bit more
        # careful about variable names. If the same variable name is used in
        # both Datasets it will cause an error.
        # First we use the inner join. Notice how few (if any) matches we find
        # because of the random times. Times need to match exactly.
        if True:
            result_merge = xr.merge((xr_ds1, xr_ds2), join='inner')

        # Here we use the outer join, so it will be all the unique times of the
        # combination of both Datasets. The length of the time dimenion is adjusted
        # to correctly match the results with locations where a time exists but no data
        # exists set to NaN. There is no tolerance. If they are slightly off
        # a new value is added. This is why this returned Dataset is larger
        # than either of the input Datasets.
        if False:
            result_merge = xr.merge((xr_ds1, xr_ds2), join='outer')

        # We need to understand what is being matched. It is not matching
        # times. It is matching indexes and expanding the dimension sizes
        # to allow statistis to be done on the data. If the statistics
        # don't need to have the time values matched but the dimentional sizes
        # need to match this is a good method to use. But if we need to match the
        # times this may not be the correct method.
        print("\nresult_merge:\n", result_merge)
#        print("\nresult_merge.dims:", result_merge.dims)
#        print(result_merge['time'])

    if False:
        # Here we use .align() to get the two Datasets to match but not merge
        # them into the same Dataset. The returned value is a tuple of two
        # new Datasets.
        result_align = xr.align(xr_ds1, xr_ds2, join='inner')
        result_align = xr.align(xr_ds1, xr_ds2, join='outer')

        if True:
            print('inner:\n', result_align[0].dims, result_align[1].dims)
            print('outer:\n', result_align[0].dims, result_align[1].dims)
            print()

        # We need to understand what is being matched. It is not matching
        # times. It is matching indexes and expanding the dimension sizes
        # to allow statistis to be done on the data. If the statistics
        # don't need to have the time values matched this is a good
        # method to use. But if we need to match the times this may not
        # be the correct method.
        if False:
            print(result_align[0]['data1'][0:10])
            print(result_align[1]['data3'][0:10])

        if False:
            print(result_align[0]['time'][0:10])
            print(result_align[1]['time'][0:10])
            print("result_align[0]['time'].size:", result_align[0]['time'].size)
            print("result_align[1]['time'].size:", result_align[1]['time'].size)

        if False:
            diff = result_align[0]['data1'].values - result_align[1]['data3'].values
            print("\nnp.nanmean(diff):", np.nanmean(diff))

# Block 2
# If we use some of the functions of other libraries we can pull them into
# Xarray to make it easier to initialize the Dataset.
if False:

    # Here we use pandas to make a time array with a 6 hour time step
    # for four years.
    pd_time = pd.date_range('2000-01-01', freq='6H', periods=365 * 4)

    # We will create a new Xarray Dataset with a range of numbers matching
    # the number of time samples we created.
    # The pandas time is used to initialize the xarray Dataset. Because
    # pandas and xarray play well together it just works.
    ds_pd_time = xr.Dataset({'data': ('time', np.arange(len(pd_time))), 'time': pd_time})

    # To create this same time step with numpy we can do this. Both get the same result
    # but pandas may be more intutive?
    np_time = np.array('2000-01-01', dtype='datetime64[h]') + np.arange(365 * 4) * 6
    ds_np_time = xr.Dataset({'data': ('time', np.arange(len(np_time))), 'time': np_time})

    # Print if the all the time steps created by Pandas and Numpy are the same
    print("\npd_time == np_time:", (pd_time == np_time).all())
    print("\nds_pd_time == ds_np_time:\n", (ds_pd_time == ds_np_time).all())
    print()

# Block 3
# Lest start changing the values to meet our needs.
# !!!! Need to change first block to True for us to use that data !!!!
if False:

    # First the orginal data size
    print("\nxr_ds1['time'].size:", xr_ds1['time'].size)

    # Now let's calculate the mean for a day by grouping the data.
    # This works for all time worded groups, hour, minute, year, month, ...
    ds1_mean = xr_ds1.groupby('time.day').mean()
    print('\ntime.day mean:\n', ds1_mean)

    # But what about a group that is not a standard group.
    # Here we resample the data by an arbitray size and then make a of those groups.
    ds1_mean = xr_ds1.resample(time='8min').reduce(np.mean)
    print("\ntime='8min\n': ", ds1_mean)

# Block 4
if False:
    # The best way to understand what is going on is to plot the data.

    # Using methods attached to the Xarray Dataset we can call a matplotlib
    # function to plot the data. We will also add a lable to use in next step
    # to populate the legend.
    xr_ds2['data3'].plot(label='data3')
    xr_ds2['data4'].plot(label='data4')

    # We can add more plots to the graph including a mean.
    # Fisrt we calcualte the resampled data mean in a new Dataset.
    # The mean is a little strange because we are calculating the mean but the
    # time location of the calculated value is placed at start of the bin time
    # not the middle.
    ds2_mean = xr_ds2.resample(time='5min').reduce(np.mean)
    # Then plot the new resampled mean data on the existing graph. Notice
    # how we are making plot calls on two different Datasets. How this works
    # I have no idea.
    ds2_mean['data4'].plot(label="ds2_mean.data4")
    # To lable the different lines we add a legend.
    plt.legend()
    # Now we tell matplotlib to draw the plot. Up until this point
    # no plot was actually created. Notice how the xaxis is already formatted
    # nicely for time. Xarray knows the axis is time and makes a guess as to
    # the correct formatting. Since data4 does not have a long_name attribute
    # it uses the variable name in the Xarray Dataset.
    plt.show()
