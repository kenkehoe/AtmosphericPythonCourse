#! /usr/bin/env python3

import numpy as np
import dask.array as da
from datetime import datetime as dt

# from dask.distributed import Client, progress
# client = Client(processes=False, threads_per_worker=4,
#                n_workers=1, memory_limit='2GB')
# client

if True:

    # Create a data array with dask module, similar to Numpy.
    # We define chunks to help manage multiprocessing and allow for smaller
    # RAM memory footprint. We could process data larger than the space of
    # memory we have available to us.

    # The chunks in this case are 100 (10x10) numpy arrays of size 1000x1000.
    x = da.random.random((10000, 10000), chunks=(1000, 1000))
    print(x)

    # Perform math similar to Numpy.
    y = x + x.T  # .T means transpose the array

    # Here we calculate the mean along an axis.
    z = y[::2, 5000:].mean(axis=1)
    # But notice when we print z it does not show any values, just information
    # about the dask object.
    print(z)

    # We will need to convert to Numpy before printing the values to the screen.
    # .compute() on the object will return a Numpy array of the values.
    print(z.compute())

    # We can do normal Numpy comparisons to get boolean arrays for testing.
    a = z > 0
    b = a.any()
    # The results of a Numpy comparison is a dask array.
    print(b)
    # So to see the values we need to convert to Numpy array.
    print(b.compute())

    # But many functions will work on the dask array as if it is a numpy array.
    if b:
        print('  Passed if statement as dask array')
    if b.compute():
        print('  Passed if statement as dask array converted to Numpy array.')

if False:
    a = da.random.random(1000, chunks=100)
#    x = da.arange(1000, chunks=100)
    b = da.ones(1000, chunks=100)

    c = b - a
    c = da.nanmean(c)

    print(c)
    print(c.compute())

# How much faster is dask than Numpy at some calculations?
if False:

    # Let's make a large array.
    num = 100000000
    # What if that array is smaller?
#    num = 10000
    start_datetime = dt.now()
    b = np.ones(num) - np.random.random(num)
    b[np.random.randint(0, num, int(num/10))] = np.nan
    b = np.nanmean(b)
    python_time_microseconds = (dt.now() - start_datetime).microseconds
    python_time_seconds = (dt.now() - start_datetime).seconds
    python_time_1 = python_time_seconds + python_time_microseconds/1000000.
    print('\nNumpy Elapsed Time: {}  seconds'.format(python_time_1))
    print()

    del b
    start_datetime = dt.now()
    # What if we need to convert Numpy array to dask array to get
    # data in dask space first. Does this change the performance?
    chunks = int(num/10)
    if True:
        b = da.asarray(np.ones(num)) - da.random.random(num, chunks=chunks)
    else:
        b = da.ones(num, chunks=chunks) - da.random.random(num, chunks=chunks)
    b[da.random.randint(0, 1, num).astype(bool)] = np.nan
    b = da.nanmean(b)
    b = b.compute()
    python_time_microseconds = (dt.now() - start_datetime).microseconds
    python_time_seconds= (dt.now() - start_datetime).seconds
    python_time_2 = python_time_seconds + python_time_microseconds/1000000.
    print('dask Elapsed Time: {}  seconds'.format(python_time_2))
    print()

    print('numpy/dask: ', python_time_1/python_time_2, '\n')
