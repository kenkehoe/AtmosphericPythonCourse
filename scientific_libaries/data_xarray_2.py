#! /usr/bin/env python3

'''
This is contineuation of the Xarray module with some more advanced topics.

'''
import numpy as np
import xarray as xr
import copy
import pandas as pd
# from pathlib import Path
import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Block 1
if True:
    # Create some data
    num = 100
    data1 = np.arange(0, num, dtype=int)
    data2 = np.arange(0, num, dtype=float) * 3.
    # Make two additional arrays at half the dimentional size by stepping by 2.
    data3 = np.arange(0, num, 2, dtype=int)
    data4 = (np.arange(0, num, 2, dtype=float) +
             np.random.uniform(low=-20, high=20, size=data3.size))

    # Create a datetime64 array with 1 minute time steps to match the size of data we created.
    time1 = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data1.size)
    time1 = time1.astype('datetime64[s]')

    # Make time array to match data3 size over the same range.
    time3 = np.array('2019-11-01T00:00:00', dtype='datetime64[m]') + np.arange(data3.size)
    # Add random seconds from 0 to 30 to each time value
    time3 = time3.astype('datetime64[s]') + np.random.randint(-30, 30, time3.size)

    if False:
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
        # Using .loc will locate useing label based indexing.
        # Here we look for datetimes that fall within the range.
        xr_result = xr_ds1['time'].loc['2019-11-01T00:04:59':'2019-11-01T00:15:00']
        print(xr_result)
        print()

        # Here we will make a copy of data1 DataArray and save under a different
        # name. This allows us to mess with it an not change the values in the Dataset.
        xr_da_data1 = copy.deepcopy(xr_ds1['data1'])

        # Now we can use label based indexing to determine locations in the DataArray
        # and change the values
        xr_da_data1.loc['2019-11-01T00:04:59':'2019-11-01T00:59:00'] = -1
        print(xr_da_data1)

    if False:
        # Here we are going to match the times from Dataset 1 to Dataset 2.
        # We use the select (.sel) method to indicate where we want to select values
        # from Dataset 1 using the times from Dataset 2. It will use the nearest value
        # in time for matching. Notice the magic of how all the variables in the
        # Dataset are selected.
        xr_result = xr_ds1.sel(time=xr_ds2['time'], method='nearest')
        print(xr_result)
        print()

        # Or we can use .sel to perform a selectoin of a range
        # across the full Dataset. Notice the magic of how all the variables in the
        # Dataset are selected.
        xr_result = xr_ds1.sel(time=slice('2019-11-01T00:04:59', '2019-11-01T00:15:00'))
        print(xr_result)
        print()

        # But what if we have a large gap and the nearest value falls outside
        # a tolerable range. We can use .reindex method with a toleracne to indicate
        # which values should be matched. The values that don't have a match are
        # set to NaN. We need to use timedelta64 to set the tolerance value which
        # includes a time unit. Remember we added a random 0 - 30 seconds to the
        # time values. Notice the magic of how all the variables in the
        # Dataset are updated.
        result = xr_ds2.reindex(time=xr_ds1['time'], method='nearest',
                                tolerance=np.timedelta64(20, 's'))

        # If no values match within tollerence it will still make
        # a new Dataset with all the time steps, but the data will all be set to
        # NaN. Also notice how the integer arrays have been upcasted to float
        # to allow setting the values to NaN.
        print(result)

    if False:
        # Here we are merging two Datasets into one. We need to be a bit more
        # careful about Variable names. If the same variable name is used in
        # both Datasets it will cause an error.
        # First we use the inner join. Notice how few matches we find.
        result_merge = xr.merge((xr_ds1, xr_ds2), join='inner')
        print(result_merge.dims)

        # Here we use the outer join, so it will be all the unique times of the
        # combination of both Datasets. The length of the time dimenion is adjusted
        # to correctly match the results with locations where a time exiss but no data
        # set to NaN. There is no tolerance. If they are slightly off
        # a new value is added. This is why this returned Dataset is larger
        # than either of the input Datasets.
        result_merge = xr.merge((xr_ds1, xr_ds2), join='outer')

        # We need to understand what is being matched. It is not matching
        # times. It is matching indexes and expanding the dimension sizes
        # to allow statistis to be done on the data. If the statistics
        # don't need to have the time values matched but the dimentional sizes
        # need to match this is a good
        # method to use. But if we need to match the times this may not
        # be the correct method.
        print(result_merge)
#        print(result_merge['time'])

    if False:
        # Here we use .align to get the two Datasets to match but not merge
        # them into the same Dataset. The returned value is a tuple of two
        # new Datasets.
        result_align = xr.align(xr_ds1, xr_ds2, join='inner')
        print(result_align[0].dims, result_align[1].dims)
        result_align = xr.align(xr_ds1, xr_ds2, join='outer')
        print(result_align[0].dims, result_align[1].dims)
        print()

        # We need to understand what is being matched. It is not matching
        # times. It is matching indexs and expanding the dimension sizes
        # to allow statistis to be done on the data. If the statistics
        # don't need to have the time values matched this is a good
        # method to use. But if we need to match the times this may not
        # be the correct method.
        print(result_align[0]['data1'])
        print(result_align[1]['data3'])
        if False:
            print(result_align[0]['time'][0:10])
            print(result_align[1]['time'][0:10])
            print("result_align[0]['time'].size:", result_align[0]['time'].size)
            print("result_align[1]['time'].size:", result_align[1]['time'].size)

        diff = result_align[0]['data1'].values - result_align[1]['data3'].values
        print(np.nanmean(diff))

# Block 2
# If we use some of the functions of other libraries we can pull them into
# Xarray to make it easier to initialize the Dataset.
if False:

    # Here we use pandas to make a time array with a 6 hour time step
    # for four years.
    time = pd.date_range('2000-01-01', freq='6H', periods=365 * 4)
    # The pandas time is used to initialize the xarray Dataset. Because
    # pandas and xarray play well together it jus works.
    ds = xr.Dataset({'data': ('time', np.arange(len(time))), 'time': time})

    # To create this same time step with numpy we can do this. Both get the same result
    # but pandas may be more intutive?
    np_time = np.array('2000-01-01', dtype='datetime64[h]') + np.arange(365 * 4) * 6
    ds_np_time = xr.Dataset({'data': ('time', np.arange(len(np_time))), 'time': np_time})

    print("time == np_time:", (time == np_time).all())
    print("\nds == ds_np_time:\n", (ds == ds_np_time).all())

# Block 3
# Lest start changing the values to meet our needs.
if False:

    # First the orginal data size
    print(xr_ds1['time'].size)

    # Now let's calculate the mean for a day by grouping the data.
    # This works for all time worded groups, hour, minute, year, month, ...
    ds1_mean = xr_ds1.groupby('time.day').mean()
    print('time.day mean:\n', ds1_mean)

    # But what about a group that is not a standard group.
    # Here we resample the data by an arbitray size and then make a of those groups.
    ds1_mean = xr_ds1.resample(time='8min').reduce(np.mean)
    print("time='8min\n': ", ds1_mean)

# Block 4
if True:
    # The bet way to understand what is going on is to plot the data.
    xr_ds2['data3'].plot(label='data3')
    xr_ds2['data4'].plot(label='data4')

    ds2_mean = xr_ds2.resample(time='8min').reduce(np.mean)
    ds2_mean['data4'].plot(label="ds2_mean.data4")
    plt.legend()
    plt.show()
