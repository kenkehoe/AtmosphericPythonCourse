# Table of Contents
* [Managing libraries and versions](#introduction)
  * [Installing Python of your choosing](#install)
  * [Create a new environment](#create)
  * [Solving issues with conda](#solving)
* [Summary](#summary) 


# Managing libraries and versions <a name="introduction"></a>
Python is just like all software, ever evolving and improving. So how do we manage making updates? And if there are updates, does everything else just work? Well, unfortunately no. Updating a library will often have requirements to update other libraries. And when your project becomes larger, this can become quite difficult to manually manage. This is where we stop trying to manually manage and use some other software to do that for us. We can always install packages using _pip_ and we can set the version to install, but this can become difficult.

A common software package manager is called _conda_. This is software that is used to install Python and libraries you choose. It has the ability to pull from different source locations of your choosing, but most importantly it performs the version compatibility search to give the best chance of all your code working correctly.

## Installing Python of your choosing <a name="install"></a>
Chances are you have Python installed on your computer. The system actually uses Python for some of its processes. But you will not want to use that version. Updating will require root privileges and if you make a mistake it can cause major problems. It is best to install a different Python and manage that. I currently recommend _conda_ for installing Python and the dependencies.

The other reason we will use _conda_ is that we can have multiple Python installations with different dependencies for different projects. This allows us to try out some new packages or a new version without breaking other code we have running. The different Python installations will be in an _environment_ and we can switch to different environments at any time.

## Create a new environment <a name="create"></a>
First we will use conda to create a new empty environment. The environment should have a name to make it easy to switch to a different environment and know which environment you are currently using. There is another method that uses the path to the environment, but we will talk about that later. This will create a new environment called _my_env_ and we will enter that environment.

<pre>
which python
  /Users/Galahad/miniconda3/envs/dqo-base/bin/python
  
conda create --name my_env
conda activate my_env
which python
</pre>

Here we searched for which Python is installed and will be used when called. The system finds _/Users/Galahad/miniconda3/envs/dqo-base/bin/python_. Then we create a new envrionment called _my_env_ and activate that environment. When we search for Python it does not find one. That is because the previous Python we found was in a different environment. When we switch environments the old environment is not accessible. This is a good thing because it means each environment is independent. If we want to install Python we need to tell conda to install Python when we create the environment. In this example, we state which version of Python to install with "=3.11" appended to python. Since we are creating a new environment with the same name it will ask if I want to remove it before creating a new environment with the same name. Notice I needed to exit the environment with _conda deactivate_ before replacing it.

<pre>
conda deactivate
conda create -n my_env python=3.11
WARNING: A conda environment already exists at '/Users/Galahad/miniconda3/envs/my_env'
Remove existing environment (y/[n])? y
  
  ... stuff ...

conda env list
  # conda environments:
  #
  base                     /Users/Galahad/miniconda3
  class                    /Users/Galahad/miniconda3/envs/class
  dqo-base              *  /Users/Galahad/miniconda3/envs/dqo-base
  my_env                   /Users/Galahad/miniconda3/envs/my_env

conda activate my_env
python
>>> import copy
>>> copy.__file__
  '/Users/Galahad/miniconda3/envs/my_env/lib/python3.11/copy.py'
>>> import pandas
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'pandas'
</pre>

After the environment is created, we run _conda env list_ to get a list of all currently available conda environments. We activate the environment with _conda activate my_env_. If we start Python and import a module we can see that the module lives in a path exclusive to the new environment called _my_env_. Importing Pandas will not work because we have not installed it yet.

We can install libraries with a simple request to conda. We can provide specific versions to install or just let it install the latest version that is going to work. Conda will search all the different libraries installed and to be installed to ensure they are compatible. If the library version needs to change to work, it will ask if we want to change/update a library to be compatible.

<pre>
conda install pandas xarray
python
>>> import xarray, pandas
</pre>

As we add more and more libraries we can see what is installed with _conda list_. This will list all the libraries currently installed in the current conda environment and the version installed. Notice that we asked for python 3.11 and it installed 3.11.7. If we leave a level of the version off it will use the most current version at that level. Since we didn't specify which Pandas to install it installed the latest version compatible with all other libraries.

<pre>
conda list
  
# packages in environment at /Users/kehoe/miniconda3/envs/my_env:
#
# Name                    Version                   Build  Channel
blas                      1.0                    openblas  
bottleneck                1.3.7           py311hb9f6ed7_0  
bzip2                     1.0.8                h620ffc9_4  
ca-certificates           2023.12.12           hca03da5_0  
libcxx                    14.0.6               h848a8c0_0  
libffi                    3.4.4                hca03da5_0  
libgfortran               5.0.0           11_3_0_hca03da5_28  
libgfortran5              11.3.0              h009349e_28  
libopenblas               0.3.21               h269037a_0  
llvm-openmp               14.0.6               hc6e5704_0  
ncurses                   6.4                  h313beb8_0  
numexpr                   2.8.7           py311h6dc990b_0  
numpy                     1.26.3          py311he598dae_0  
numpy-base                1.26.3          py311hfbfe69c_0  
openssl                   3.0.13               h1a28f6b_0  
packaging                 23.1            py311hca03da5_0  
pandas                    2.1.4           py311h7aedaa7_0  
pip                       23.3.1          py311hca03da5_0  
python                    3.11.7               hb885b13_0

  ... more libraries
</pre>

It may become important to create environments on different systems, or it may be important to keep track of which libraries we need for each project. Conda makes this easy with the concept of an environment file. This is a YAML file that directs conda on how to create a new environment. The file can be used to direct the environment building or to document the current environment of an existing environment. Let's have conda create an environment file describing my_env.

<pre>
conda env export > environment.yaml
</pre>

If we look at this file, we will see the name of the environment and all the installed libraries with the currently installed version. We can take this file and provide it to the conda create command to generate a new environment using all the libraries and the versions listed. But normally we do not need to list every package since many of the libraries installed are dependent and will be installed anyway. All we need to recreate this is to list the three packages we requested. And if we don't care about versions we can leave that off and let conda figure it out. Most of the time we can ignore versions. At some point we will need to fix an issue by manually listing what version we want installed, but we will cross that bridge another day.

So we can take the file created by conda and edit it to only list what we need to reproduce the current environment to the specific level for our needs. If we edit the file it will look something like this:

<pre>
name: my_env

channels:
  - defaults

dependencies:
  - pandas
  - python=3.11
  - xarray
</pre>

We can now take this file and create a new environment from scratch by pointing to this _environment.yaml_ file for all configuration needs. Since the environment _my_env_ already exist we will need to add the _--force_ keyword. If the environment did not exist we could ignore that keyword.

<pre>
conda env create -f environment.yaml --force
Collecting package metadata (repodata.json): done
Solving environment: done

  ... stuff ...

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
</pre>


## Solving issues with conda <a name="solving"></a>
Sometimes the package we want will not be available in the default location (channel). Then we need to do a little work to go find it and tell conda where to download from. For example _pint_ is not located in conda's default location. So when we try to install, it will fail.

<pre>
conda install pint

Collecting package metadata (current_repodata.json): done
Solving environment: unsuccessful initial attempt using frozen solve. Retrying with flexible solve.
Collecting package metadata (repodata.json): done
Solving environment: unsuccessful initial attempt using frozen solve. Retrying with flexible solve.

PackagesNotFoundError: The following packages are not available from current channels:

  - pint

Current channels:

  - https://repo.anaconda.com/pkgs/main/osx-arm64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/osx-arm64
  - https://repo.anaconda.com/pkgs/r/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.
</pre>

We need to do a little digging to see where the package exists. We can start by searching using conda defaults

<pre>
conda search pint
  
Loading channels: done
No match found for: pint. Search: *pint*
</pre>

If we tell conda where to look we can find it at a different host.
<pre>
conda search -c conda-forge pint
Loading channels: done
# Name                       Version           Build  Channel             
pint                           0.8.1            py_1  conda-forge         

 ... more stuff ...
  
pint                            0.23    pyhd8ed1ab_0  conda-forge 
</pre>

This means if we tell conda to install _pint_ from a different channel (conda-forge), it will find the package and install. We perform this on the command line
<pre>
conda install -c conda-forge pint
</pre>

or we can update the _environment.yaml_ file to have a list of places to look for packages. It will try to install the package with the first channel and if that fails it will go _down the list until it is successful. So if we update our _environment.yaml_ file to look like this we can run the same command above and it will install _pint_ from _conda-forge.
<pre>
name: my_env

channels:
  - defaults
  - conda-forge

dependencies:
  - pandas
  - python=3.11
  - xarray
  - pint
</pre>

But what if the package does not exist in any conda channels and is only installable through _pip_? We can tell conda to install some packages using _pip_ by editing the _environment.yaml_ file to list _pip_ as a dependency and then use _pip_ to install _pint_.
<pre>
name: my_env

channels:
  - defaults

dependencies:
  - pip
  - pandas
  - python=3.11
  - xarray
  
  # This part allows install using pip
  - pip:
    - pint
</pre>

# Summary <a name="summary"></a>
Managing versions and dependencies for a small number of libraries is manageable by hand, but as the project scales it is best to use something else to do the work for you.

Conda can install Python and the libraries you want and put them into a separate environment so different projects do not interfere with each other if they have conflicts.

Using environment.yaml files to manage the libraries and dependencies can simplify your work. Typically it is best practice to erase an environment and start from new when making changes to more complex projects. There can be unknown issues that are resolved by starting from scratch. The environment.yaml file can be part of the project.

If each project uses a different conda environment you will need to remember to activate that environment before running. If everything fits into a single environment you can set that to be a default in the startup file for your shell (e.g. .bashrc or .bash_profile file)
