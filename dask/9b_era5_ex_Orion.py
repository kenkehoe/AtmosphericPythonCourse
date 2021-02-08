#!/usr/bin/env python3
# coding: utf-8

import pandas as pd
import numpy as np
import xarray as xr
import datetime as dt
import sys
import warnings
warnings.filterwarnings('ignore')
from dask.distributed import Client, progress
from dask_jobqueue import SLURMCluster

def main():
    e5path="/work/noaa/co2/kaushik/PVPRM/ERA5_PVPRM/"#orion
    csvpath="/home/jmund/dask/csv/"

    yr=2018
    sitelon = 40.02 #example for Boulder, CO
    sitelat = -105.27 #example for Boulder, CO

    print('time: ', dt.datetime.now().strftime("%H:%M:%S"))
    dsm = xr.open_mfdataset(e5path + 'era5_daily_pvprm_%s*' %(yr),parallel=True,chunks={'latitude': 10, 'longitude': 10})
    sitelon=sitelon%360

    # subset location, put into dataframe 
    dsmloc = dsm.sel(longitude=sitelon, latitude=sitelat, method ='nearest').compute()

    dfmloc=dsmloc.to_dataframe()

    # do some math/edit the arrays 
    # avg soil data, convert stl1+stl2 to avg and append
    soilt=(dfmloc.stl1+dfmloc.stl2)/2.
    dfmloc['Ts.ERA5']=soilt

    # drop stl1, stl2, lat, lon
    dfmloc2=dfmloc.drop(['ssrd','stl1','stl2','latitude','longitude'],axis=1)
    del dfmloc

    # rename t2m,par into new dataframe
    dfmloc3=dfmloc2.rename(columns={"t2m":"Ta.ERA5","par":"PAR.ERA5"})
    del dfmloc2

    # convert Ta and Ts to Celsius
    dfmloc3['Ta.ERA5']=dfmloc3['Ta.ERA5']-273.15
    dfmloc3['Ts.ERA5']=dfmloc3['Ts.ERA5']-273.15

    # new time index going up to 23:30 on 12/31 -- era5 data ends at 23:00
    t_index=pd.date_range(start='%s-01-01 00:00:00' %(yr), end='%s-12-31 23:30:00' %(yr), freq='30T')

    #resample on 30min timestep, interpolate (default linear?), reindex to t_index to go up to 23:30, /
    #forward fill last value, reset index so that time is one  of the columns
    dfmloc_rs=dfmloc3.resample('30T').interpolate().reindex(t_index).ffill().reset_index()

    # save to dataframe, rename index column to time
    dfm=dfmloc_rs.rename(columns={"index":"time"})
    del dfmloc_rs

    dfm.to_csv(r'%sdf_era5_%s.csv.j2' %(csvpath,yr),index=False)
    del dfm
    print('done: ', dt.datetime.now().strftime("%H:%M:%S"))

if __name__ == '__main__':
    #Create the jobqueue cluster
    slurmextra=['-p orion','-q batch','--mail-user=john.mund@noaa.gov','--time=00:05:00']
    cluster=SLURMCluster(project='co2', cores=6, processes=3, memory='1GB', log_directory='./logs', job_extra=slurmextra)
    cluster.scale(jobs=3)
    client = Client(cluster)
    print(cluster.job_script())
    main()