#! /usr/bin/env python3

import numpy as np
import numpy.ma as ma
import warnings
import time
import datetime
import pytz

print()

# Block 1
# What is the difference between regular Python and Numpy?
if True:
    print(type(1))  # Python integer
    print(type(1.))  # Python float
    print(type('Hello World'))  # Python string
    print()
    print('np.int8:', np.array(1, dtype=np.int8).dtype)  # Numpy integer of size 8 bytes
    print('np.int16:', np.array(1, dtype=np.int16).dtype)  # Numpy integer of size 16 bytes
    print('np.int32:', np.array(1, dtype=np.int32).dtype)  # Numpy integer of size 32 bytes
    print('np.int64:', np.array(1, dtype=np.int64).dtype)  # Numpy integer of size 64 bytes
    print('np.int:', np.array(1, dtype=int).dtype)  # Default Numpy integer of size 64 bytes
    print()
    print('np.float16:', np.array(1, dtype=np.float16).dtype)
    print('np.float32:',np.array(1, dtype=np.float32).dtype)
    print('np.float64:',np.array(1, dtype=np.float64).dtype)
    print('np.float:',np.array(1, dtype=float).dtype)
    print()
    print('np.bool:',np.array(1, dtype=np.bool_).dtype)
    print('np.int:',np.array(1, dtype=np.int_).dtype)
    print('np.foat:',np.array(1, dtype=np.float_).dtype)
    print('np.uint:',np.array(1, dtype=np.uint).dtype)
    print('np.complex:',np.array(1, dtype=complex).dtype)
    print('Hello World:', np.array('Hello World').dtype)  # <U11 means 11 charater Unicode String.
    print()

# Block 2
# Let's make some simple arrays
if False:
    a = [1, 2, 3]
    b = np.array([1, 2, 3])  # Create a 1-D array
    print('type(a):', type(a))  # Get type of a
    print('type(b):', type(b))  # Get type of b
    print('type(b[0]):', type(b[0]))  # Get type of index 0 of b
    print('b.dtype:', b.dtype)
#    print('a.dtype:', a.dtype)  # a.dtype will not work. dtype is numpy only.
    print('a:', a)
    print('b:', b)

# Block 3
# What's the difference between regular Python and numpy?
# The speed increase gets better with multidimentional data.
if False:
    num = 8000000
    print(f"Looping over {num} values using for loop with list")
    start_time = time.time()  # This is to get the time of execution

    # Here we create a list of value and add one to each 
    a = list(range(0, num))
    for ii in a:
        a[ii] = a[ii] + 1

    # We can do the same thing with list comprehension to be a little
    # faster but it's still no match for speed of Numpy.
#    a = [a[ii] + 1 for ii in a]

    python_time = time.time() - start_time
    print(f"Elapsed Time: {python_time}  seconds")
    print()
    del a

    print(f"Using numpy to do same operation using Numpy arrays with {num} values.")
    start_time = time.time()  # This is to get the time of execution

    # Here we create a new array and add 1 to each element
    a = np.arange(num, dtype=np.int16) + 1

    numpy_time = time.time() - start_time
    print(f'Elapsed Time: {numpy_time}  seconds')

    print(f"\nRation of native python/numpy: {python_time/numpy_time}")

# Block 4
# Can you swith between regular Python and numpy?
if False:
    num = 10000
    a = list(range(0, num))  # Defaults to integer values
    print('type(a):', type(a))
    print('len(a):', len(a))
    print()

    # Convert the python list into numpy array
    b = np.array(a)
    print('type(b):', type(b))
    print('b.size:', b.size)
    print('b.shape:', b.shape)
    print()

    # convert the numpy array back into python list
    c = list(b)
    print('type(c):', type(c))
    print('len(c):', len(c))

# Block 5
# Let's make an array but of type float
if False:
    a = np.array([1, 2, 3.0])  # Will be set as float because 3.0 is a float value.
    print('a.dtype:', a.dtype)
    print('a:', a)  # Notice all values are floats
    print()

    b = np.array([1, 2, 3], dtype=float)
    print('b.dtype:', b.dtype)
    print('b:', b)
    print()

    # Create an integer array
    c = np.array([4, 5, 6])  # This is type int because all values are int
    c = c.astype(float)  # Convert the type from int to float
    print('c.dtype:', c.dtype)
    print('c:', c)
    print()

# Block 6
# Let's start making larger arrays without needing to type all the values
if False:
    a = np.array(range(10))  # Converts the list range function to numpy array
    b = np.arange(10)  # Creates the numpy array directly and faster
    c = np.arange(1, 10, 2)  # Creates array counting by two
    d = np.arange(10, 1, -1)  # Creates array decending by one
    e = np.flip(a)  # Reverses the array a from increasing to decreasing
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('d:', d)
    print('e:', e)

# Block 7
# Let's select values from our arrays
if False:
    a = np.arange(10)
    print('a:', a)
    print('a[0:5]:', a[0:5])  # selects upto but not including index 5
    print('a[0:]:', a[3:])  # selects everthing from 3 to end of array
    print('a[:5]:', a[:5])  # selects to upto but not including index 5
    print('a[3:5]:', a[3:5])  # selects from 3 upto but not including index 5
    print('a[0:-1]:', a[:-1])  # selects upto but not including index 5
    print('a[0:100]:', a[0:100])  # index is past end of array?!?

# Block 8
# Let's get metadata about our arrays.
if False:
    a = np.arange(10)
    print('a', a, sep=": ", end="\n\n")
    print('a.shape:', a.shape)
    print('a.size:', a.size)
    print('len(a):', len(a))
    print()

    b = np.array([[1, 2, 3], [4, 5, 6]])
    print('b', b, sep=":\n")
    print('b.shape:', b.shape)
    print('b.size:', b.size)
    print('len(b):', len(b))  # Wait what is going on? Not true?
    print()

    c = np.arange(10)  # Create a 1-D array
    c = c.reshape((2, 5))  # Change to a 2-D array
    print('c:\n', c)
    print('c.shape:', c.shape)
    print('c.size:', c.size)
    print()

    print('c[1, 4]:', c[1, 4])
    print('c[1, 2:4]:', c[1, 2:4])
    print('c[:, 2:4]:\n', c[:, 2:4])
    print('c[0, :]:', c[0, :])
    print('c[1, 2:100]:', c[1, 2:100])  # over index handled OK? Maybe works?

# Block 9
# Let's create some more complicated arrays
if False:
    a = np.zeros((2, 2))    # Create an array of all zeros
    print('a:\n', a)

    b = np.ones((2, 2))    # Create an array of all ones
    print('\nb:\n', b)

    c = np.full((2, 2), 7, dtype=int)   # Create a constant array
    print('\nc:\n', c)

    d = np.eye(3)           # Create a 3x3 identity matrix
    print('\nd:\n', d)

    e = np.random.random((2, 4))  # Create an array filled with random values
    print('\ne:', e)

# Block 10
# Let's play with broadcasting
if False:
    a = np.zeros(20, dtype=int)
    print('a:', a)

    a = a + 1.0  # Note how it upconverted from int to float
    print('\na:', a)

    a = a.astype(int)
    print('\na:', a)

    a[3:8] = a[3:8] + 10
    print('\na:', a)

    a = a + np.arange(a.size)
    print('\na:', a)

    a += 1000
    print('\na:', a)

# Block 11
# Let's start to work with booleans
if False:

    a = [False, True]
    b = np.array([False, True])
    print('a:', a, type(a))
    print('b:', b, type(b))
    print()

    c = np.arange(10, dtype=int)
    print('c:', c)
    print()

    bool_idx = c > 4  # Make a boolean array where c is greater than 4 set to True
    print('bool_idx:', bool_idx)
    print('type(bool_idx):', type(bool_idx))
    print('bool_idx.dtype:', bool_idx.dtype)
    print('c[bool_idx]: ', c[bool_idx])
    print('c[c > 4]:    ', c[c > 4])
    print()

    # Finde where c is great than 6 and set to -1
    print('c:', c)
    c[c > 6] = -1
    print('c:', c)
    print()

    d = np.arange(c.size, dtype=int) + 10
    print('d:', d)
    d[c > 3] = -2
    print('d:', d)
    print()

    # Find index numbers where c is great than or equal to 2
    e = np.where(c >= 2)
    print('e:', e)
    print('c >= 2:', c >= 2)
    print('type(e):', type(e))
    print('e[0]:', e[0])
    print('c[e]:', c[e])
    print()

    # What about testing all the values in the array?
    f = np.zeros(10, dtype=bool)  # Create an array of all False
    f[3:8] = True  # Set values at index 3 to 7 to True
    print('f:', f)
    print('f.all():', f.all())  # Check if all values are True
    print('f.any():', f.any())  # Check if any values are True
    print()

# Block 12
# Let's play with IEEE Not a Number (NaN) for missing data
if False:

    print(np.nan)
    print(type(np.nan))
    print(10.0 * np.nan)
    print(11 + np.nan, 12 - np.nan, 13 * np.nan, 14 / np.nan)

    # Initially create an integer array. But we will see that it needs to be a float.
    if True:
        a = np.arange(10, dtype=float)
    else:
        a = np.arange(10)
    print('\na:', a)

    a[a == 9] = np.nan  # This will fail if array is int because NaN is a float
    a[3:7] = np.nan
    print('a:', a)

    # Now we will try to find where the values are set to NaN
    b = (a == np.nan)  # This does not work because can not equate with NaN
    print('\nb:', b)

    b = np.isnan(a)  # Need to use methods to find the locations of NaN
    print('\nb:', b)

# Block 13
# Let's calculate some statistics with NaNs! Whew finally!
if False:
    a = np.arange(10, dtype=float)
    print('a:', a)
    print('a.min():', a.min())  # This is Python min method, not numpy. Maybe slower?
    print('np.min(a):', np.min(a))  # This is numpy min function

    a[0] = np.nan
    print('\na', a)

    # Calculate the mean. Notice how it returns NaN. The NaNs are tainting
    # all the operations.
    print('\nnp.min(a):', np.min(a))

    # This is telling Numpy to ignore the NaN values in the calculations.
    print('\nnp.nanmin(a):', np.nanmin(a))
    print()

    # This will work but it will create a warning message.
    if True:
        b = np.array([np.nan, np.nan])  # Array of all NaNs
        print('\nnp.nanmean(b):', np.nanmean(b))
    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=RuntimeWarning)
            b = np.array([np.nan, np.nan])  # Array of all NaNs
            print('\nnp.nanmean(b):', np.nanmean(b))

# Block 14
# Let's calculate some statistics of multi dimentional data!
if False:
    a = np.arange(20)  # This is a 1-D array
    a = a.reshape((4, 5))  # This is now a 2-D array (or matrix)
    print('a:\n', a)

    b = np.max(a)
    print('\nb:', b)

    c = np.max(a, axis=0)
    print('\nc:', c)  # Note how the returned array is orientated.
    print()

    a = a.astype(float)  # Converting to float to use NaNs
    a[1, 3] = np.nan
    print('a:\n', a)
    print()

    print('np.nansum(a):', np.nansum(a))
    print()

    d = np.nansum(a, axis=1)
    print('d:', d)

    d = np.nansum(a, axis=-1)
    print('d:', d)


# Block 15
# Now let's play with matrix addition, subtraction, division, ...
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

# Block 16
# Now some more broadcasting fun
if False:
    x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    v = np.array([1, 0, 1])
    y = x + v  # Add v to each row of x using broadcasting
    print('x:\n', x)
    print('v:\n', v)
    print('y:\n', y)
    print()

    a = np.arange(12)
    a = a.reshape((3, 4))
    print('a.shape:', a.shape)
    print('a:\n', a)

    b = np.array([1, 0, 1])
    print('b.shape:', b.shape)
    print('b:', b)
    print()

    # Reshape the array to be in correct orientation
    if False:
        b = b.reshape((3, 1))
        print('b.shape:', b.shape)
        print('b:\n', b)

    c = a + b  # Add v to each row of x using broadcasting
    print('\nc:\n', c)

# Block 17
# Now lets look at Numpy masked arrays and why they are awesome!
if False:
    # First create a numpy array
    a = np.array([0, 1, 2, 3, 4, 5])
    # Next create a numpy masked array and set the mask values.
    # A 0 = False and 1 = True
    masked_a = ma.masked_array(a, mask=[False, False, True, False, True, True])
    print('masked_a:', masked_a)
    # Calculate the mean not using the masked values
    masked_a_mean = masked_a.mean()
    print('masked_a_mean:', masked_a_mean)
    print()

    # Create a masked array and set all the mask values to False
    # and set a fill_value other than the default.
    masked_b = ma.masked_array(a, mask=False, fill_value=-99999)
    print('masked_b:', masked_b)
    print('masked_b.data:', masked_b.data)
    print('masked_b.mask:', masked_b.mask)
    print('masked_b.fill_value:', masked_b.fill_value)
    print()

    # Create a masked array where all values less than or equal to
    # 1 are masked
    masked_c = ma.masked_less_equal(a, 1)
    print('masked_c:', masked_c)
    print('masked_c.data:', masked_c.data)
    print('masked_c.mask:', masked_c.mask)
    print('masked_c.mean():', masked_c.mean())
    print('np.mean(masked_c.data):', np.mean(masked_c.data))
    print()

    # Create a masked arra where all values less than or equal to
    # 1 are masked. Same as above but with different syntax.
    masked_d = ma.masked_where(a <= 1, a)
    print('masked_d:', masked_d)

    # Create a masked array with no mask set, yet.
    masked_d = ma.masked_array(a)
    print('\nmasked_d:', masked_d)
    print('masked_d.mask:', masked_d.mask)

    # Set the mask to True for all indexes less than 3.
    # Notice that we never create a mask, all that is done automatically.
    masked_d[:3] = ma.masked
    print('\nmasked_d:', masked_d)
    print('masked_d.mask:', masked_d.mask)
    print()

    # Reset the mask to all False
    masked_d.mask = ma.nomask
    print('\nmasked_d:', masked_d)
    print('masked_d.mask:', masked_d.mask)

# Block 18
# Some of the nuances of performance with masked arrays
if False:
    num = 5000000  # The size of the array we are going to play with
    # We can create an array of all ones with type integer 16 bit
    masked_a = ma.ones(num, dtype=np.int16)
    print('masked_a.dtype:', masked_a.dtype)
    print('masked_a.size:', masked_a.size)
    print()

    # Now we will set most of the values to be masked
    masked_a[:num-1000] = ma.masked
    # Now lets print the sum of the mased array using default masked array
    # methods and then we will sum using numpy of just the data stored in
    # the masked array without using the mask.
    print('masked_a.sum():', masked_a.sum())
    print('np.sum(masked_a.data):', np.sum(masked_a.data))
    print()

    # Create a new clean masked array with mask not set yet.
    # Since the mask array is the same size as data array this can be
    # large and take longer.
    masked_a = ma.ones(num, dtype=np.int16)

    # Now we will add a random number to the masked array of ones.
    masked_a = masked_a + np.random.random(num)

    # Next we calculate the standard deviation of the masked array
    masked_a_std = ma.std(masked_a)
    print('masked_a_std:', masked_a_std)
    print()

    # Here we add some random noise spikes
    masked_a[np.random.randint(0, high=num, size=10000)] = 20

    # Here we mask out the values that are great than one standard deviation.
    # Now the mask is created, since it did not exist before this.
    masked_b = ma.masked_outside(masked_a, 1 - masked_a_std, 1 + masked_a_std)

    # Here we mask out some random values. Notice we are not using
    # masked_b.mask. That is slower and not correct. If the mask did not
    # already exist it would have an error. This way will create the mask
    # if it was not already created.
    masked_b[np.random.randint(0, high=num, size=1000)] = ma.masked

    # This is the sum of the data with all masked values excluded
    print('np.sum(masked_a):', np.sum(masked_b))

    # This is the sum of the data without excluding any values.
    print('np.sum(masked_b.data):', np.sum(masked_b.data))
    print()

    # Now lets convert everything back to a regular numpy array
    # but set the masked values to NaNs in the numpy array
    masked_b.fill_value = np.nan
    b = ma.filled(masked_b)
    print('type(masked_b):', type(masked_b))
    print('b.dtype:', b.dtype)
    # Notice the value is NaN because we are not using np.nanmax(). This means
    # there is at least one NaN in the array.
    print('np.max(b):', np.max(b))

# Block 19
# Because we will work with time series data let's learn about Python datetime objects.
# This is so we understand how the native time works with Python. We will then
# learn about Numpy dates and times.
if False:
    a = datetime.datetime.now()
    print('datetime.datetime.now():', a)

    a = datetime.date.today()
    print('datetime.date.today():', a)

    a = datetime.date(2019, 4, 13)
    print('datetime.date(2019, 4, 13):', a)

    # timestamp is number of seconds from 1970-01-01 00:00:00 or epoch.
    timestamp = datetime.date.fromtimestamp(1326244364)
    print("\ntimestamp:", timestamp)
    timestamp = datetime.datetime.fromtimestamp(1326244364)
    print("timestamp:", timestamp)

    # date object of today's date
    today = datetime.date.today()
    print("\ntoday.year:", today.year)
    print("today.month:", today.month)
    print("today.day:", today.day)

    # time(hour = 0, minute = 0, second = 0)
    a = datetime.time()
    print("\ndatetime.time():", a)
    # time(hour, minute and second)
    b = datetime.time(11, 34, 56)
    print("datetime.time(11, 34, 56):", b)
    # time(hour, minute and second)
    c = datetime.time(hour=11, minute=34, second=56)
    print("c:", c)
    # time(hour, minute, second, microsecond)
    d = datetime.time(11, 34, 56, 234566)
    print("d:", d)

    # datetime(year, month, day)
    e = datetime.datetime(2018, 11, 28)
    print("\ne:", e)
    # datetime(year, month, day, hour, minute, second, microsecond)
    f = datetime.datetime(2017, 11, 28, 23, 55, 59, 342380)
    print("f:", f)

    # current date and time
    now = datetime.datetime.now()
    g = now.strftime("%Y-%m-%d %H:%M:%S")
    print("\ng:", g)
    h = now.strftime("%m/%d/%Y, %H:%M:%S")
    print("h:", h)

    date_string = "21 June, 2018"
    print("\ndate_string =", date_string)
    date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
    print("date_object =", date_object)

    local = datetime.datetime.now()
    print("\nLocal:", local.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_NY = pytz.timezone('America/New_York')
    datetime_NY = datetime.datetime.now(tz_NY)
    print("New York:", datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_Paris = pytz.timezone('Europe/Paris')
    datetime_Paris = datetime.datetime.now(tz_Paris)
    print("Paris:", datetime_Paris.strftime("%m/%d/%Y, %H:%M:%S"))
    tz_utc = pytz.timezone('UTC')
    datetime_utc = datetime.datetime.now(tz_utc)
    print("UTC:", datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"))
    datetime_utc = datetime.datetime.utcnow()
    print("utcnow():", datetime_utc.strftime("%m/%d/%Y, %H:%M:%S"))

# Block 20
# Because we will work with time series data let's learn about Numpy datetime objects.
# Initially all datetimes were in UTC. Now the datatime is timezone naive. You can use
# a timezone offset from UTC but that feature is being phased out.
if False:
    date = np.datetime64('2005-02-25')
    print('date:', date)
    print('date.dtype:', date.dtype)

    dt1 = np.datetime64('2005-02-25T03:30:55')
    print('\ndt1:', dt1)
    print('dt1.dtype:', dt1.dtype)

    dt2 = np.datetime64('2012-03', 's')
    print('\ndt2:', dt2)
    print("dt2.astype('datetime64[h]'):", dt2.astype('datetime64[h]'))

    # OK so what you can set precisoin. Why do I care?
    # Because you can use the precision to indicate what step size to use.
    # Notice I didn't give the starting day nor the end day. This helps
    # with not needing to know length of months.
    dt3 = np.arange('2005-02', '2005-03', dtype='datetime64[D]')
    print('\ndt3:', dt3)

    # I can perform rular arithmitic as well. The restult comes back
    # as difference in days not a datetime64 value.
    dt_diff1 = np.datetime64('2009-01-01') - np.datetime64('2008-01-01')
    print('\ndt_diff1:', dt_diff1)

    # I can add to a value with a timedelta64
    dt_diff2 = np.datetime64('2011-06-15T00:00') + np.timedelta64(12, 'h')
    print('\ndt_diff2:', dt_diff2)

    # It has the equivlant of NaN with Not a Time (NaT)
    print("\nnp.datetime64('nat'):", np.datetime64('nat'))
    print("np.datetime64():", np.datetime64())

    # And maybe most importantly if I have the precision set correctly I can
    # make arrays and add to them to get the time ranges I want. Notice
    # I gave start and end times in different precision and then set the
    # precions I want to make the range step how I want.
    dt4 = np.arange('2005-02-01T00:00:00', '2005-02-05T00', dtype='datetime64[D]')
    print('\ndt4:', dt4)
    print("\ndt4 + 23:", dt4 + 23)

    # Since dt4 is in Day precision adding an int to it adds a that in Days
    print("\ndt4:", dt4)
    dt4 = dt4 + 23
    print("\ndt4 + 23:", dt4)

    print("\nnp.datetime64('today'):", np.datetime64('today'))
    print("np.datetime64('now'):", np.datetime64('now'))
    # Notice when I change the precision it's the precision the value is
    # store in, not the precision used to get the time.
    print("np.datetime64('now'):", np.datetime64('now', 'ns'))

# Block 21
# How do we convert from python datetime to numpy datetime64 and vice a versa?
if False:

    dt = datetime.datetime.utcnow()  # Get current date and time with python datetime
    # Get current date and time with in Numpy using same date and time
    # from python datetime
    dt64 = np.datetime64(dt)
    if False:
        # This is how we can get current date and time with just Numpy datetime.
        # Notice the precision is only down to second.
        dt64 = np.datetime64('now', 'us')
    print('dt:  ', dt)
    print('dt64:', dt64)

    # To convert from numpy datetime64 to python datetime
    # set precision to seconds and convert to integer. This will
    # give number of seconds since epoch, or timestamp.
    ts = dt64.astype('datetime64[s]').astype(int)
    print("\nts:", ts)
    # Use the timestamp with datetime timestamp method in UTC.
    dt64_to_dt = datetime.datetime.utcfromtimestamp(ts)
    print('dt64_to_dt:', dt64_to_dt)

    # To convert from python datetime to numpy datetime64 put the
    # python datetime into numpy datetime64. You can set the
    # numpy precision to seconds to match for printing.
    dt_to_dt64 = np.datetime64(dt)
    dt_to_dt64 = dt_to_dt64.astype('datetime64[s]')
    print("dt_to_dt64:", dt_to_dt64)

print()
