# Managing librareis and versions
Python is just like all software, every evolving and imporving. So how do we manage making updates? And if there are updates does everything else just work? Well, unfortunately no. Updating a library will often have requirements to update other libraries. And when your project becomes larger this can become quite difficult to manualy manage. This is where we stop trying to manually mangae and use some other software to do that for us. We can always install packages using _pip_ and we can set the version to install but this can become difficult.

A common software package manager is called _conda_. This is software that is used to install Python and libraries you choose. It has the ability to pull from different source locations of your choosing, but most importantly it performs the version compability search to give the best chance of all your code working correctly.

## Installing Python of your choosing.
Chances are you have Python installed on your computer. The system actually uses Python for some of its processes. But you will not want to use that version. Updating will require root privlages and if you make a mistake it can cause major problems. It is best to install a different Python and manage that. I currently recomend _conda_ for installing Python and the dependencies.

The other reason we will use _conda_ is that we can have multiple Python instalations with different dependencies for different projects. This allows us to try out some new package or a new version without breaking other code we have running. The differnt Python installations will be in an _environment_ and we can switch to different environments at any time.

### Create a new environment
First we will use conda to create a new empty environment. The environment should have a name to make it easy to switch to different environment and know which environment you are currently using. There is another method that uses the path to the environment but we will talk about that later. This will create a new environment called _my_env_ and we will enter that environment.

<pre>
which python
  /Users/Galahad/miniconda3/envs/dqo-base/bin/python
  
conda create --name my_env
conda activate my_env
which python
</pre>

Here we searched for which Python is installed and will be used when called. The system finds _/Users/Galahad/miniconda3/envs/dqo-base/bin/python_. Then we create a new envrionment called _my_env_ and activate that environment. When we search for Python it does not find one. That is because the previous python we found was in a different environment. When we switch environments the old environment is not accessable. This is a good thing because it means each environment is separate. If we want to install a Python we need to tell conda to install Python when we create the environment. Since we are creating a new environment with the same name it will ask if I want to remove it before creating a new environment with the same name. Notice I needed to exit the environment before replacing it with _conda deactivate_.

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

After the environment is created we run _conda env list_ to get a list of all currently available conda environments. We activate the environment with _conda activate my_env_. If we start Python and import a module we can see that the module lives in a path exclusive to the new environment call _my_env_. Importing Pandas will not work because we have not installed it yet.
