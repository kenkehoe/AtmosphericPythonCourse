This class was presented using Jupyter Notebooks run in Jupyter lab.  
See below for instructions on how to view interactively.
To just view the contents of each file, follow links in Contents.html


--How to get these course files--

All files are included in Ken Kehoe's github for our initial python class:

https://github.com/kenkehoe/AtmosphericPythonCourse

or by using git:

git clone https://github.com/kenkehoe/AtmosphericPythonCourse.git


--Jupyter Lab--
Jupyter lab is installed as part of the Anaconda python distribution 
or can be installed using mini-conda:

Download and install mini-conda:

https://docs.conda.io/en/latest/miniconda.html

Open a new terminal window and create a new environment with required packages:

>conda create -n AtmosphericPython -c conda-forge python=3.7 jupyterlab dask distributed dask-labextension --yes

or install into an existing environment:

>conda install -c conda-forge jupyterlab dask distributed dask-labextension --yes

Jupyter lab can be run locally from terminal window with:
>jupyter lab


--To access Jupyter Lab on GML servers--

Running Jupyter Lab on a GML server allows you to browse your home directory and run 
code on GML servers.  GML IT and I are in the process of setting up a Jupyter Hub server
that will simplfy access and login, but you can easily run a Jupyter Lab now using ssh with 
a local port redirect.

*Choose a port to avoid conflicts with other users
    1[dsrc office phone ext]
example for me whose phone is 303-497-5472

    15472
    
*Connect to the GML network vpn in normal way

*Open a terminal window and connect to GML server with a local redirect.  
Enter port number from above in all 3 locations:
(Windows users can create a configuration in Putty with a local redirect (ask for details if needed).)

>ssh nimbus4 -L [port #]:localhost:[port #] jupyter lab --no-browser --ip="*" --port=[port #]
ex:
>ssh nimbus4 -L 15472:localhost:15472 jupyter lab --no-browser --ip="*" --port=15472

On macs, you can put this into your .bash_profile as an alias:
alias jlab='ssh nimbus4 -L 15472:localhost:15472 jupyter lab --no-browser --ip="*" --port=15472'

and then just enter,
>jlab
to start.

In the terminal window, note the 'token' at the end of the start up text.  Copy it to clipboard.

*In a browser window on your laptop, goto this url:
http://localhost:15472/lab

Paste the token in to the token field at the bottom of the page and enter a new password.
Navigate to dask folder an open notebook files.  Shift+enter will execute code blocks.

