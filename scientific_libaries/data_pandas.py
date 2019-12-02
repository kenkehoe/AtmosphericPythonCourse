#! /usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Block 1
if True:
    # Create some data in a dictionary.
    data = {'apples': [3, 2, 0, 1],
            'oranges': [0, 3, 7, 2]}
    # Use the dictionary to populate the new pandas data frame
    purchases = pd.DataFrame(data)

    print(type(purchases))  # Pandas DataFrame consisting of Series
    print(type(purchases.apples))  # Pandas Series
    print()

    print(purchases)
    print()

    # Add an index to label the rows of the DataFrame
    purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

    print(purchases)
    print()

    # Extract a row using the index name
    print(purchases.loc['June'])
    print()

# Block 2
if False:
    # Create a Pandas series using a list
    # Notice how the index is created automatically starting at 0.
    a = pd.Series([11, 28, 72, 3, 5, 8])

    print('\na:\n', a)
    print('a.index:', a.index)
    print('a.values:', a.values)
    print('type(a.values):', type(a.values))
    print()

    # Using two lists create a pandas Series
    fruits = ['apples', 'oranges', 'cherries', 'pears']
    quantities = [20, 33, 52, 10]
    b = pd.Series(quantities, index=fruits)
    print('b:')
    print(b)

    # Using one list create a new series but reuse the fruits list for the index.
    c = pd.Series([17, 13, 31, 32], index=fruits)
    d = b + c
    print('\nd:')
    print(d)

    fruits = ['peaches', 'oranges', 'cherries', 'pears']
    fruits2 = ['raspberries', 'oranges', 'cherries', 'pears']

    # Create two new series with new data and different indexes.
    S = pd.Series([20, 33, 52, 10], index=fruits)
    S2 = pd.Series([17, 13, 31, 32], index=fruits2)

    # Now add the two series together. Notice how it automagically adds in
    # NaN for spaces where data does not exist in both series. To do this 
    # it had to change the datatype from int to float.
    print('\nS + S2:')
    print(S + S2)

# Block 3
if False:
    # Create a dictionary to use for making the Series
    cities = {"London":    8615246,
              "Berlin":    3562166,
              "Madrid":    3165235,
              "Rome":      2874038,
              "Paris":     2273305,
              "Vienna":    1805681,
              "Bucharest": 1803425,
              "Hamburg":   1760433,
              "Budapest":  1754000,
              "Warsaw":    1740119,
              "Barcelona": 1602386,
              "Munich":    1493900,
#              "Boulder":   None,
              "Milan":     1350680}

    # The Series is of type int because all the values are int in the dictionary.
    # But once we set one of the data to None, the only way to store that state is
    # to use NaN, which changes the datatype to float.
    city_series = pd.Series(cities)
    print(city_series)
    print()
    # We can apply a math function to all values in the Series using .apply()
    print(city_series.apply(np.log))

# Block 4
if False:
    # Make a Seris of data by using the range function to make a list of values.
    # Then we add a value to every data in the Series.
    data = pd.Series(range(10)) + 10
    print(data)
    print()
    # We can set specific values by using the list/array index syntax.
    # Since we are setting the int value to a float value the entire Series
    # column is updated to float.
    data[[3, 6, 9]] = np.nan
    print(data)
    print()

    # We can use methods to return a boolean array indicating where that condition
    # is true/false.
    print(data.isnull())  
    # print(data.notnull())  # Same idea but get revers of the values.
    print()

    # Here we tell Pandas to look for instances of missing data and remove that row
    # from the Series.
    print(data.dropna())
    print()

    # Here we tell Pandas to look for instances of missing data and replace it with
    # a value of our choosing.
    print(data.fillna(0))

# Block 5
# Now we can start doing some real stuff!
if False:
    # Create a pathlib file path to some ASCII data. It's actually real data!!!
    filename = Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.00.20191105.150801.raw.dat')

    # Using the path to a specific file we read the data into a Pandas Data Frame.
    # This is something you will use
    # very often if you have data in ASCII column files. Get to know this method well.
    data = pd.read_csv(filename, delimiter=',', header=0, skiprows=[0, 2, 3], parse_dates=[0])
    print(data[0:10])
    print()

    # We can get a Pandas Index (similar to list) of the column names 
    print(data.columns)
    print('len(data):', len(data))  # How many data samples do we have
    print('TIMESTAMP:', type(data['TIMESTAMP'][0]))  # What type is the time column data?
    print('PTemp:', type(data['PTemp'][0]))  # What type is the time column data?
    print()

    if False:
        # Without importing or calling the matplotlib library we can make a plot
        # usig matplotlib directoy with pandas. Notice we are calling the same
        # method called .plot but on the data object. This is very common in Python.
        # It's a wrapper around matplotlib using Pandas.
        data.plot(x='TIMESTAMP', y='Temp_C_Avg')

        # We can make two different plots with another call to plot. But notice how
        # this creats a whole new plot, not adding to the existing plot. This is how
        # using the same call is different when called from matplotlib vs. pandas.
        if False:
            data.plot(x='TIMESTAMP', y='Temp_C_Std')
        plt.show()

    if False:
        # To get the two data seris plotted on the same plot we need to follow
        # the pandas plotting rules.
        axes = plt.gca()  # Set up the plottin axes
        # Now plot the data and tell pandas to put the plot on the existing axes.
        # Also notice how there is a legend, but we did't say make a legend.
        data.plot(x='TIMESTAMP', y='Temp_C_Avg', ax=axes)
        data.plot(x='TIMESTAMP', y='Temp_C_Std', ax=axes)
        plt.show()

# Block 6
if False:
    # Read data from data file.
    filename = Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.00.20191105.150801.raw.dat')
    data = pd.read_csv(filename, delimiter=',', header=0, skiprows=[0, 2, 3], parse_dates=[0])
    print(type(data))

    # Get the pressure Series from the DataFrame and sum it up to one value.
    pressure_sum = data['Pressure_kPa'].sum()
    print('\npressure_sum:', pressure_sum)
    print()

    # Get the pressure Series from the DataFrame and calculate the mean.
    pressure_mean = data['Pressure_kPa'].mean()
    print('pressure_mean:', pressure_mean)
    print()

    # Get the pressure Series from the DataFrame and use a special method to summarize
    # the values in the Series using what Pandas things is most helpful.
    pressure_describe = data['Pressure_kPa'].describe()
    print(pressure_describe)
    print()

    if False:
        # Calculate the correlation coefficients of the DataSet on each Series
        print(data.corr())
        print()
        # Calculate the covariance coefficients of the DataSet on each Series
        print(data.cov())

# Block 7
if False:
    # Read data
    filename = Path('..', 'data', 'sgpmetE13.b1', 'sgpmetE13.00.20191105.150801.raw.dat')
    data = pd.read_csv(filename, delimiter=',', header=0, skiprows=[0, 2, 3], parse_dates=[0])

    # Extract the RH series from the DataFrame. This is a copy of the Series in the 
    # DataFrame so changing the values will not change the values in the DataFrame.
    rh = data['RH_Avg']
    # print(type(rh))

    # Calculate a rolling mean over the Series using 10 points.
    # Notice the first 8 values are NaN. There is a default number of values to use
    # to calculate a value. Else it is set to NaN.
    if False:
        rh_rolling_mean = rh.rolling(10).mean()
        print(rh_rolling_mean)
    if False:
        # By specifically stating the minimum number of points to use when calculating
        # the mean we force it to not fill in so many NaNs. There is at least one value
        # to use in the rollig window so not NaNs. What happens when you change 
        # min_periods to a larger number?
        rh_rolling_mean = rh.rolling(10, min_periods=1).mean()
        print(rh_rolling_mean)

    if False:
        # Set a range of values in our extracted to NaN to represent missing data.
        rh[20:30] = np.nan
        # Calculate a rolling mean.
        rh_rolling_mean = rh.rolling(10, min_periods=2).mean()
        print(rh_rolling_mean)

        # And once again we can make a plot but this time we can use matplotlib
        # directory but extracting the time and data from the Pandas DataFrame.
        # Notice that the two data we are plotting are Pandas Datasets. Matplotlib
        # handles those just fine.
        if False:
            plt.plot(data['TIMESTAMP'], rh)
            plt.plot(data['TIMESTAMP'], rh_rolling_mean, color='red')
            plt.show()
