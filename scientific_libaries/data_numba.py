#! /usr/bin/env python3

import numpy as np
# import numba
from numba import jit
import time

x = np.arange(10000000).reshape(1000, 10000)


def go_fast(a):
    trace = 0
    for i in range(a.shape[0]):
        trace += np.tanh(a[i, i])
    return a + trace


# Called and run normally
start = time.time()
go_fast(x)
normal_diff = time.time() - start
print("Elapsed normal function call = %s" % (normal_diff))


@jit(nopython=True, parallel=True, fastmath=True)
def go_fast(a):  # Function is compiled and runs in machine code
    trace = 0
    for i in range(a.shape[0]):    # A regular loop in python works with numba
        trace += np.tanh(a[i, i])  # A numpy operation works with numba
    return a + trace               # A numpy broadcast works with numba


# DO NOT REPORT THIS... COMPILATION TIME IS INCLUDED IN THE EXECUTION TIME!
go_fast(x)

# NOW THE FUNCTION IS COMPILED, RE-TIME IT EXECUTING FROM CACHE
start = time.time()
go_fast(x)
without_diff = time.time() - start
print("Elapsed (after compilation) = %s" % (without_diff))

print("\nWith normal function / without compilation:", normal_diff/without_diff)

# This is hard to correctly measure but after doing a few trials it appears to
# be about 50% faster with this code over not useing numba. Is this worth it,
# I don't know. Maybe, maybe not? It is also dependent on array sizes. Unlike
# dask, the performance increase goes down with larger arrays. Maybe we can
# combine dask and numba?
