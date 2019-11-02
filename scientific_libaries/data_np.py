#! /usr/bin/env python3

# import standard libraries
import numpy as np
# import warnings
# from sys import exit as sysexit

print()
# Let's make some simple arrays
if True:
    a = [1, 2, 3]
    b = np.array([1, 2, 3])  # Create a rank 1 array
    print('type(a):', type(a))
    print('type(b):', type(b))
    print('type(b[0]):', type(b[0]))
    print('a:', a)
    print('b:', b)

# Let's make an array but of type float
if False:
    a = np.array([1, 2, 3.])
    print('type(a[0]):', type(a[0]))
    print('a:', a)
    print()

    b = np.array([1, 2, 3], dtype=float)
    print('type(b[0]):', type(b[0]))
    print('b:', b)

# Let's make an array and set the type to what we want after.
if False:
    b = np.array([4, 5, 6])
    b = b.astype(float)
    print('type(b[0]):', type(b[0]))
    print('b:', b)


# Let's start making larger arrays without needing to type all the values
if False:
    a = np.array(range(10))
    b = np.arange(10)
    c = np.arange(1, 10, 2)
    d = np.arange(10, 1, -1)
    e = np.flip(a)
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('e:', e)

# Let's select values from our arrays
if False:
    a = np.arange(10)
    print('a:', a)
    print('a[0:5]:', a[0:5])  # selects upto but not including index 5
    print('a[0:]:', a[0:])  # selects everthing to end of array
    print('a[:5]:', a[:5])  # selects to upto but not including index 5
    print('a[3:5]:', a[3:5])  # selects from 3 upto but not including index 5
    print('a[0:-1]:', a[0:-1])  # selects upto but not including index 5
    print('a[0:100]:', a[0:100])  # index is past end of array?!?

# Let's get metadata about our arrays.
if False:
    a = np.arange(10)
    print('a:\n', a)
    print('a.shape:', a.shape)
    print('a.size:', a.size)
    print('len(a):', len(a))
    print()

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print('b:\n', b)
    print('b.shape:', b.shape)
    print('b.size:', b.size)
    print('len(b):', len(b))
    print()

    c = np.arange(10)
    c = c.reshape((2, 5))
    print('c:\n', c)
    print('c.shape:', b.shape)
    print('c.size:', b.size)
    print()

    print('c[1, 4]:', c[1, 4])
    print('c[1, 2:4]:', c[1, 2:4])
    print('c[:, 2:4]:\n', c[:, 2:4])
    print('c[0, :]:', c[0, :])
    print('c[1, 2:100]:', c[1, 2:100])  # over index handled OK? Maybe works

# Let's create some more complicated arrays
if False:
    a = np.zeros((2, 2))    # Create an array of all zeros
    print('a:\n', a)

    b = np.ones((2, 2))    # Create an array of all ones
    print('b:\n', b)

    c = np.full((2, 2), 7, dtype=int)   # Create a constant array
    print('c:\n', c)

    d = np.eye(2)           # Create a 2x2 identity matrix
    print('d:\n', d)

    e = np.random.random((2, 2))  # Create an array filled with random values
    print(e)

# Let's play with broadcasting
if False:
    a = np.zeros(20, dtype=int)
    print('a:', a)

    a = a + 1.
    print('a:', a)

    a = a.astype(int)
    a[0:9] = a[0:9] + 10
    print('a:', a)

    a = a + np.arange(a.size)
    print('a:', a)

    a += 100
    print(a)

# Let's start to work with booleans
if False:

    a = [False, True]
    b = np.array([False, True])
    print('a:', a, type(a))
    print('b:', b, type(b))
    print()

    c = np.arange(10, dtype=int)
    print('c:', c)

    bool_idx = c > 4
    print('bool_idx:', bool_idx)
    print('type(bool_idx):', type(bool_idx))
    print('type(bool_idx[0]):', type(bool_idx[0]))
    print('c[bool_idx]: ', c[bool_idx])

    c[c > 6] = -1
    print('c:', c)
    print()

    d = np.where(c >= 2)
    print('d:', d)

# Let's play with IEEE NaN for missing data
if False:
    a = np.arange(10)  # dtype=float)
    print('a:', a)

    a[a == 9] = np.nan  # This will initially fail because NaN is a float
    a[3:5] = np.nan
    print('a:', a)

    b = (a == np.nan)
    print('b:', b)

    b = np.isnan(a)
    print('b:', b)
    print()


# Let's calculate some statistics with NaNs! Whew finally!
if False:
    a = np.arange(10, dtype=float)
    print('a:', a)
    print('a.min():', a.min())  # This is Python min method, not numpy
    print('np.min(a):', np.min(a))  # This is numpy min function

    a[0] = np.nan
    print()

    print('np.mean(a):', np.mean(a))
    print('np.nanmean(a):', np.nanmean(a))
    print('np.nanmean(np.array([np.nan, np.nan])):',
          np.nanmean(np.array([np.nan, np.nan])))
    print()

    # Have we imported warnings?
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        b = np.array([np.nan, np.nan])
        print('with np.nanmean():', np.nanmean(b))

# Let's calculate some statistics of multi dimentional data!
if False:
    a = np.arange(20)  # This is a 1-D array
    a = a.reshape((4, 5))  # This is now a 2-D array (or matrix)
    print('a:\n', a)

    b = np.max(a, axis=1)
    print('b:', b)

    c = np.mean(a, axis=0)
    print('c:', c)  # Note how the returned array is orientated.
    print()

    a = a.astype(float)  # Converting to float to use NaNs
    a[1, 3] = np.nan
    print('a:\n', a)
    print()

    print('np.nansum(a):', np.nansum(a))
    print()

    d = np.nansum(a, axis=-1)
    print('d:', d)

    d = np.nansum(a, axis=1)
    print('d:', d)


# Now let's paly with matrix addition, subtraction, division, ...
if False:
    x = np.array([[1, 2], [3, 4]], dtype=np.float64)
    y = np.array([[5, 6], [7, 8]], dtype=np.float64)

    print('x:\n', x)
    print('y:\n', y)

    v = np.array([9, 10])
    w = np.array([11, 12])

    print('v:\n', v)
    print('w:\n', w)
    print()

    # Elementwise sum; both produce the array
    # [[ 6.0  8.0]
    #  [10.0 12.0]]
    print('x + y:\n', x + y)
    print('np.add(x, y):\n', np.add(x, y))
    print()

    # Elementwise difference; both produce the array
    # [[-4.0 -4.0]
    #  [-4.0 -4.0]]
    print('x - y:\n', x - y)
    print('np.subtract(x, y):\n', np.subtract(x, y))
    print()

    # Elementwise product; both produce the array
    # [[ 5.0 12.0]
    #  [21.0 32.0]]
    print('x * y:\n', x * y)
    print('np.multiply(x, y):\n', np.multiply(x, y))
    print()

    # Elementwise division; both produce the array
    # [[ 0.2         0.33333333]
    #  [ 0.42857143  0.5       ]]
    print('x / y:\n', x / y)
    print('np.divide(x, y):\n', np.divide(x, y))
    print()

    # Elementwise square root; produces the array
    # [[ 1.          1.41421356]
    #  [ 1.73205081  2.        ]]
    print('np.sqrt(x):\n', np.sqrt(x))  # Notice there is no x.sqrt() option
    print()

    # Inner product of vectors; both produce 219
    print('v.dot(w):\n', v.dot(w))
    print('np.dot(v, w):\n', np.dot(v, w))
    print()

    # Matrix / vector product; both produce the rank 1 array [29 67]
    print('x.dot(v):\n', x.dot(v))
    print('np.dot(x, v):\n', np.dot(x, v))
    print()

    # Matrix / matrix product; both produce the rank 2 array
    # [[19 22]
    #  [43 50]]
    print('x.dot(y):\n', x.dot(y))
    print('np.dot(x, y):\n', np.dot(x, y))

# Now some more broadcasting fun
if False:
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x + v  # Add v to each row of x using broadcasting
    print('y:\n', y)
    print()

    a = np.arange(12)
    a = a.reshape((3, 4))
    print('a:\n', a)

    b = np.array([1, 0, 1])
    print('b.shape:', b.shape)
    print('b:', b)
    print()

    # Reshape the array to be in correct orientation
#    b = b.reshape((3, 1))
#    print('b.shape:', b.shape)
#    print('b:\n', b)

    c = a + b  # Add v to each row of x using broadcasting
    print('\nc:\n', c)


print()
