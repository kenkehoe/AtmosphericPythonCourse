#! /usr/bin/env python3

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from act.io.csvfiles import read_csv
from act.plotting import TimeSeriesDisplay
import re

filename = Path('data', 'pocketLab_aqi_2021-05-18_082549.csv')
ds = read_csv(filename, parse_dates={'time': [0,1]})

ds['time'].values = ds['time'].values + np.timedelta64(5, 'h')
ds = ds.assign_coords(time=ds['time'])
ds = ds.swap_dims({'index': 'time'})
ds = ds.drop('index')
ds = ds.rename({'Latitude': 'latitude', 'Longitude': 'longitude'})

var_names = list(set(ds.keys()) - set(['time', 'Elapsed Seconds', 'latitude', 'longitude']))
var_names = [ii for ii in var_names if 'Avg.' not in ii]
var_names.sort()

my_disp = TimeSeriesDisplay({'pocketLab': ds}, subplot_shape=(int(len(var_names)/2), 2),
                            figsize=(8*2, 2*len(var_names)/2))

row=0
col=0
for plot_num, var_name in enumerate(var_names):
    match = re.match(r".+\(([\S]+)\).*", var_name)
    units = '(1)'
    if match is not None:
        units = f"({match.groups()[0]})"
    axes = my_disp.plot(var_name, subplot_index=(row, col), day_night_background=True)
    axes.set_ylabel(units)

    row += 1
    if plot_num == 4:
        col += 1
        row = 0

plt.tight_layout()
plt.subplots_adjust(hspace=0.4)
plt.show()
