#!/usr/bin/env python3
"""Create maps for obspack nc files"""

import sys
import os
import subprocess
#from dask.distributed import Client, progress, SSHCluster
#from dask import delayed

def main():
    #Loop through obspack output directory and create a map file for each dataset
    sdir='/ccg/obspacks/obspack_co2_1_GLOBALVIEWplus_v6.0_2020-09-11/'
    ddir='/home/ccg/mund/dev/python_class/AtmosphericPythonCourse/dask/output/maps/'
    cmd='/ccg/ftp/obspack/src/python/obspack/op/qc/op_map.py sdir='+sdir+' ddir='+ddir
    output='';t='';

    file_list=os.listdir(sdir+"/data/nc")
    print("Processing ",len(file_list)," files")

    for fn in file_list:
        c=cmd+" filename="+fn
        output+=run_shell_cmd(c)
#        t+=delayed(run_shell_cmd)(c)
#    output=t.compute()

    print(output)
        
        

#    client.shutdown()

    
    
def run_shell_cmd(cmd,printOutput=True,quitOnError=True,stdin=None):
    """Run passed command and handle errors"""
    try:
        if stdin : cmd=stdin+"|"+cmd
        p=subprocess.run(cmd,text=True,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        if printOutput : print(p.stdout)
        return p.stdout

    except subprocess.CalledProcessError as e:
        print("Error: ",e.output)
        if quitOnError : sys.exit()
            
    return None




if __name__ == '__main__':
#    cluster = SSHCluster(['nimbus4','nimbus','nimbus2','nimbus3','nimbus4'],
#                         scheduler_options={"dashboard_address": ":8884"},
#                         worker_options={'nprocs': 2,'nthreads': 2})
#    client = Client(cluster)
    
    main()
    


