#! /usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

if True:

    data = {
        'apples': [3, 2, 0, 1], 
        'oranges': [0, 3, 7, 2]
        }
    purchases = pd.DataFrame(data)

    print(type(purchases))
    print(type(purchases.apples))
    print()

    print(purchases)
    print()

    purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

    print(purchases)
    print()

    print(purchases.loc['June'])
    print()

if False:
    a = pd.Series([11, 28, 72, 3, 5, 8])

    print(a)
    print(a.index)
    print(a.values)
    print(type(a.values))
    print()

    fruits = ['apples', 'oranges', 'cherries', 'pears']
    quantities = [20, 33, 52, 10]
    b = pd.Series(quantities, index=fruits)
    print(b)
    print()

    c = pd.Series([17, 13, 31, 32], index=fruits)
    d = b + c
    print(d)
    print()

    fruits = ['peaches', 'oranges', 'cherries', 'pears']
    fruits2 = ['raspberries', 'oranges', 'cherries', 'pears']

    S = pd.Series([20, 33, 52, 10], index=fruits)
    S2 = pd.Series([17, 13, 31, 32], index=fruits2)
    print(S + S2)

if False:
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
#          "Boulder":   None, 
          "Milan":     1350680}

    city_series = pd.Series(cities)
    print(city_series)
    print()
    print(city_series.apply(np.log))

if False:
    data = pd.Series(range(10)) + 10
    print(data)
    print()
    data[[3, 6, 9]] = np.nan
    print(data)
    print()
    print(data.isnull())  # print(data.notnull())
    print()
    print(data.dropna())
    print()
    print(data.fillna(0))

if False:
    data = pd.read_csv('../data/sgpmetE13.b1/sgpmetE13.00.20191105.150801.raw.dat',
                       delimiter=',', header=0, skiprows=[0,2,3], parse_dates=[0])
    print(data[0:10])
    print()

    print(data.columns)
    print(len(data))
    print(type(data['TIMESTAMP'][0]))
    print()

    if True:
        data.plot(x='TIMESTAMP', y='Temp_C_Avg')
#        data.plot(x='TIMESTAMP', y='Temp_C_Std')
        plt.show()

    else:
        ax = plt.gca()
        data.plot(x='TIMESTAMP', y='Temp_C_Avg', ax=ax)
        data.plot(x='TIMESTAMP', y='Temp_C_Std', ax=ax)
        plt.show()

if False:
    data = pd.read_csv('../data/sgpmetE13.b1/sgpmetE13.00.20191105.150801.raw.dat',
                       delimiter=',', header=0, skiprows=[0,2,3], parse_dates=[0])

    pressure_sum = data['Pressure_kPa'].sum()
    print('pressure_sum:', pressure_sum)
    print()

    pressure_mean = data['Pressure_kPa'].mean()
    print('pressure_mean:', pressure_mean)
    print()

    pressure_describe = data['Pressure_kPa'].describe()
    print(pressure_describe)
    print()

#    print(data.corr())
#    print()
#    print(data.cov())

if False:
    data = pd.read_csv('../data/sgpmetE13.b1/sgpmetE13.00.20191105.150801.raw.dat',
                       delimiter=',', header=0, skiprows=[0,2,3], parse_dates=[0])

    rh = data['RH_Avg']
    rh_rolling_mean = rh.rolling(10).mean()
#    rh_rolling_mean = rh.rolling(10, min_periods=1).mean()

#    rh[20:30] = np.nan
#    rh_rolling_mean = rh.rolling(10, min_periods=1).mean()
    print(rh_rolling_mean)

#    plt.plot(data['TIMESTAMP'], rh)
#    plt.plot(data['TIMESTAMP'], rh_rolling_mean, color='red')
#    plt.show()


