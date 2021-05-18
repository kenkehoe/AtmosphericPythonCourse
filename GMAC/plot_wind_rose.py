#! /usr/bin/env python3

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from act.io.noaagml import read_gml
from act.plotting import WindRoseDisplay

# Read in data. This will read in one or more files and do a bit of work
# updating the variable attributes with units, long_name and quality
# control variables.
ds_obj = read_gml(Path('data', 'brw21120.dat'))

# Create a date string for plot title
timestring = pd.to_datetime(ds_obj['time'].values[0]).strftime('%Y-%m-%d')

WindDisplay = WindRoseDisplay({'noaa_gml_brw': ds_obj}, figsize=(8, 8))
WindDisplay.plot('wind_direction', 'wind_speed',
                 set_title=(f"NOAA GML {ds_obj.attrs['location']} Wind Rose for {timestring}"),
                 spd_bins=np.linspace(0, 25, 5), num_dirs=20,
                 tick_interval=4)

plt.show()
