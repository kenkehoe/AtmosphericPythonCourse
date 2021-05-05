#! /usr/bin/env python3

import numpy as np
import dask.array as da
import time

# from dask.distributed import Client, progress
# client = Client(processes=False, threads_per_worker=4,
#                n_workers=1, memory_limit='2GB')
# client


# Block 1
if True:

    # Create a data array with dask module, similar to Numpy.
    # We define chunks to help manage multiprocessing and allow for smaller
    # RAM memory footprint. We could process data larger than the space of
    # RAM memory we have available to us.

    # The chunks in this case are 100 (10x10) numpy arrays of size 1000x1000.
    x = da.random.random((10000, 10000), chunks=(1000, 1000))
    print('x:', x)

    # Perform math similar to Numpy.
    y = x + x.T  # .T means transpose the array

    # Here we calculate the mean along an axis.
    z = y[::2, 5000:].mean(axis=1)
    # But notice when we print z it does not show any values, just information
    # about the dask object. At this time no computation has occured, just the
    # information about what we want to do.
    print('z:', z)

    # We will need to computer the values and convert to Numpy before printing
    # the values to the screen. .compute() on the object will return a
    # Numpy array of the values.
    print('z.compute():', z.compute())

    # We can do normal Numpy comparisons to get boolean arrays for testing.
    # Here we are doing two operations. Neither of the operations are done
    # untile we tell it to perform the operations with a .compute() call.
    a = z > 0
    b = a.any()
    # The request of a Numpy comparison is a dask array are stored as operations
    # to perform, but the operations have not been perfoemd yet.
    print('b:', b)
    # So to see the values we need to perform operations and convert to Numpy array.
    print('b.compute():', b.compute())

# Block 2
if False:
    # Most of the Numpy operations are available in Dask computations.
    a = da.random.random(1000, chunks=100)
#    x = da.arange(1000, chunks=100)
    b = da.ones(1000, chunks=100)

    c = b - a
    c = da.nanmean(c)

    print('c:', c)
    print('c.compute():', c.compute())

# Block 3
# How much faster is dask than Numpy at some calculations?
if False:

    # Let's make a large array.
    num = 100000000
    # What if that array is smaller? Turns out the overhead of implementing Dask
    # can make it slower for smaller datasets.
#    num = 10000
    start_time = time.time()
    b = np.ones(num) - np.random.random(num)
    b[np.random.randint(0, num, int(num/10))] = np.nan
    b = np.nanmean(b)
    python_time_1 = time.time() - start_time
    print(f'\nNumpy Elapsed Time: {python_time_1} seconds\n')
    del b

    start_time = time.time()
    # What if we need to convert Numpy array to dask array to get
    # data in dask space first. Does this change the performance?
    chunks = int(num/10)
    if False:
        b = da.asarray(np.ones(num)) - da.random.random(num, chunks=chunks)
    else:
        b = da.ones(num, chunks=chunks) - da.random.random(num, chunks=chunks)
    b[da.random.randint(0, 1, num, chunks=chunks).astype(bool)] = np.nan
    b = da.nanmean(b)
    b = b.compute()
    python_time_2 = time.time() - start_time
    print(f'dask Elapsed Time: {python_time_2} seconds\n')

    print(f'numpy/dask: {python_time_1/python_time_2}\n')
