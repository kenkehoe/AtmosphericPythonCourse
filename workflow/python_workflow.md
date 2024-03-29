# Building a larger project
This file attempts to explain how to build a larger project with dependencies on other repositories and other code written by you.

## First thoughts
We need to have a general idea of what we want to be in this repository vs. imported and used in this repository. Initially, we need an entry point. Typically we use a single entry point file that accepts arguments and keywords to allow driving the process. This folder contains a file _main_example.py_ that serves this purpose.

## Explaining the main program
The file uses _argparse_ to accept and understand arguments and keywords provided on the command line. We can see what options are available by using the _-h_ or _--help_ option. It will print a help menu and exit.

`./main_example.py -h`

Running this program will interpret the arguments and keywords and execute. For example:

<pre>
./main_example.py one -f 1.2 -l eggs spam

args: Namespace(argument='one', true_false_keyword=True, keyword=None, float_keyword=1.2, keyword_list=['eggs', 'spam'])
This is the keyword 'keyword' = 'None'. It has a value even when not set.

You set --float_keyword to '1.2'. Did you provide the number with decimal precision or did it get upconverted?

You set --keyword_list to ['eggs', 'spam']. Notice how it prints as a list even when you provide only one value. It expects and makes a list.
</pre>

Looking at _main_example.py_ we can see the file permissions are set to allow executing the code

`-rwxr-xr-x  1 Galahad  staff  6262 Feb 22 13:21 main_example.py`

and the first line of the file has a "shebang" line that tells the system this is a Python file and what Python executable to use to interpret the code. This is the Linux syntax but we can update for Windows if needed.

`line 1: #! /usr/bin/env python3`

When called, the _main_example.py_ file is read from top to bottom and parsed/compiled. The _def_ word indicates a definition of a function, but the function is not automatically executed. Nothing is executed until the end of file by using specific syntax. This syntax will look at the _\_\_name\_\__ Python variable to see if it is set to the string _\_\_main\_\__. If so the if statement is executed, which calls the _main()_ function defined previously.

<pre>
  if __name__ == '__main__':
    main()
</pre>

In _main()_ we call another predefined function that will handle command line input for arguments and keywords. The _parse_commandline()_ function defines the argument and keyword variable names, definitions, and help menu. The function returns _args_ which is an argparse Namespace object that we can access for variables provided from command line.

The values from the _args_ are used to see what other code/functions will be executed. A good practice is to separate the code into small parts to make it more useable and manageable. The functions can be imported from someone else's repository or functions you define in different files.

We have a file in the same directory called _library_example.py_. This file is recognized to be a Python file since it has the .py file extension. This means we can import variables or functions from that file.

`from library_example import argument_function`

This line will read _library_example.py_ and import the argument_function function. It is not executed, just read into memory and made available for use. In the _main()_ function we call 

`result, value1, value2 = argument_function(args.argument, 'spam and eggs', value2=args.true_false_keyword)`

We can write as many Python files in the current directory as we want to organize the variables or functions. If we want to better organize the structure we can put Python files in sub directories. We just need to provide the relative path (including sub directories) when we import the functions or variables.

<pre>
from sub_directory.more_complicated import more_complicated_function
from sub_directory.more_complicated import IMPORTED_VARIABLE
</pre>

While this example shows how a variable can be imported, this is not the preferred method. There are other ways to import and manage variables.

Look in the _sub_directory_. You will see the Python file we called to perform the import _sub_directory/more_complicated.py_ and you will also see an empty file _sub_directory/\_\_init\_\_.py_ . While not strictly needed for this folder to work, it is needed for other more advanced projects. A general rule of thumb is that each folder should have an _\_\_init\_\__.py file. The file does not need to contain anything.

Other than _argparse_ everything in _main_example.py_ is code written by us and imported for execution. As the program becomes more complicated, we will import libraries that are distributed with Python (like argparse) or some that need to be installed (like numpy, scipy, Xarray, Pandas). For a single project that does not share code, this example will be similar to what you build.

## Making Shared library functions
If you have a function that gets used often among multiple different projects, it may be best to separate it out into its own repository. Overall this is not much more difficult, but does require thinking about how Python knows what to read and from where.

So what does Python do to know where to look for programs? There are multiple places that set where Python will look for a file. The first is which Python is installed. Python comes with some libraries already installed (re, math, glob, copy, ...). You can see where those files are installed using the doubleunder syntax.

<pre>
python
>>> import copy
>>> copy.__file__
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/copy.py'
</pre>

This will show the full path to the file imported when _import copy_ is executed. In this instance you can see the version of Python used is installed in the miniconda area and is in python version 3.11. _copy_ came preinstalled.

Pandas does not come preinstalled with the Python version so I had to install it. The install put it in the _site-packages_ area which is where the packages I install are located.

<pre>
python
>>> import pandas
>>> pandas.__file__
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/site-packages/pandas/__init__.py'
</pre>

The reason this directory path is available is that the path is on my _PATH_ environment variable. The _PATH_ environment variable is how the system knows where to look. Python will look for a file that can be imported matching the module you request starting at the first path in PATH (left side) and continuing through each path (separated with :) until it finds the module. When found it quits looking. That means we can have the same module "installed" in multiple locations but *Python will always use the first one found*.

<pre>
echo $PATH
/opt/local/bin:/opt/local/sbin:/Users/Galahad/miniconda3/envs/dqo-base/bin:/Users/Galahad/miniconda3/condabin:/Users/Galahad/.local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin: ... and some more ...
</pre>

We can see this by looking at the list of paths Python has ready to search. Python has used the PATH environment variable to search for locations that contain Python packages/files. Paths that do not have Python related files are ignored. We can use the _sys_ Python module to see what paths are loaded and ready to use. The '' path is the current working directory.

<pre>
python
>>> import sys
>>> sys.path
['',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/lib-dynload',
  '/Users/Galahad/.local/lib/python3.11/site-packages',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/site-packages']
</pre>

We can add paths to files by appending them to PATH, but that's a little strange since we are adding a path to Python files in the system environment variable that is shared by all other programs. It would be better if we could add paths to Python stuff with just a Python thing. Well we can with the PYTHONPATH environment variable. Here I will use Bash shell to create the PYTHONPATH environment variable and set it to two paths.

<pre>
export PYTHONPATH="/path/to/a/python/directory:/second/python/directory"
python
>>> import sys
>>> sys.path
['', '/path/to/a/python/directory',
  '/second/python/directory',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/lib-dynload',
  '/Users/Galahad/.local/lib/python3.11/site-packages',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/site-packages']
</pre>

Notice how the two paths set in PYTHONPATH are prepended to the Python path listings. It knows that if I set PYTHONPATH those are most likely to contain files I am interested in using and should be used first. So I could use multiple locations to better organize my code.

It's not recommended, but for some projects you may want to add a path after the Python interpreter is started or in your Python program. You can edit the sys.path directly so the program knows where to search. It is not recommended because the added path is not global to the system (it is global to this instance of Python) and will cause you to bang your head against the wall some day.

<pre>
python
>>> import sys
>>> sys.path.append("/home/me/mypy")
>>> sys.path
  ['', '/path/to/a/python/directory', '/second/python/directory',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/lib-dynload',
  '/Users/Galahad/.local/lib/python3.11/site-packages',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/site-packages',
  '/home/me/mypy']
</pre>

Notice how the path is added to the end of the list. If there is a copy in one of the other paths it will use that version.

So what does this mean? Well we can create a single location to put our library module that contains functions that will be used by multiple projects. We can then set PYTHONPATH in our .bashrc or .bash_profile file to always point to that directory. Then no matter which project we are working on, the library functions are available to Python for import. And, since there is only one copy of the code in the library area, all of our updates/fixes only need to be done once to be updated for all of our projects. The general rule of thumb is to copy/paste code as few times as possible. If you don't follow this rule, you will spend hours trying to understand why.

## Other path setting information
As you add more libraries through other directories you may run into some confusing results. There are a few other ways Python will update the _sys.path_, so here is a list to help explain them in case you need to understand to solve some problem.

### PYTHONUSERBASE
The PYTHONUSERBASE environment variable is used to set the user base directory. This is a directory for a specific user's code, often the location to put paths to code you develop elsewhere and install with _pip_ editable installation. You can think of this as a symbolic link to the code you edit so your changes take effect immediately without needing to reinstall. Following our example above, if the PYTHONUSERBASE environment variable is set, the sys.path will be updated.

<pre>
export PYTHONUSERBASE="/Users/Galahad/.py_rh9"
python
>>> import sys
>>> sys.path.append("/home/me/mypy")
>>> sys.path
  ['', '/path/to/a/python/directory', '/second/python/directory',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/lib-dynload',
  '/Users/Galahad/.local/lib/python3.11/site-packages',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/site-packages',
  '/Users/Galahad/.py_rh7/lib/python3.11/site-packages',
  '/home/me/mypy']
</pre>

Notice that the PYTHONPATH paths are set first just after the current directory. Then the PYTHONUSERBASE paths expanded to the directory containing Python files. Finally the path appended with sys.path.append().

### .local directory
On Linux and Mac systems a hidden directory in the user's home directory called _.local_ contains files and paths to application specific information. Often this will contain installations of executables in the _/bin_ directory and library modules in _/lib_ directory. Python will typically separate different major.minor versions of Python installation into different folders. For example, your home directory .local folder could contain multiple Python version library folders.

<pre>
> ls /Users/Galahad/.local
  LICENSE.txt bin         lib         setup.cfg   share
> ls /Users/Galahad/.local/lib
  python3.11 python3.6  python3.7  python3.8  python3.9
> ls /Users/Galahad/.local/lib/python3.11/site-packages/
__pycache__
act_atmos-1.0.4.post377.dev0+g4bf0e1e6a.dist-info
dqlib.egg-link
easy-install.pth
</pre>

The ~/.local directory is not typically added to the $PATH environment variable as default, but may be set up to be added on your system. If so, the library you import could be read from this directory or this directory may redirect the import to another path on your system.

If you do not want Python to read in ~/.local as a default, you can turn this off by setting an environment variable. Setting this variable (to basically anything) will tell Python to not import any libraries found in the ~/.local directory paths.
<pre>
> export PYTHONNOUSERSITE=1
> echo $PYTHONNOUSERSITE
1
> python
  import sys
  sys.path
  ['',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python311.zip',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/lib-dynload',
  '/Users/Galahad/miniconda3/envs/dqo-base/lib/python3.11/site-packages']
</pre>
