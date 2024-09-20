# Here are some notes on making a Pythong package
There are many online resources to explain how to build a package. Some are good, some are bad and some are OK. Here are some I found useful. Unfortunately they often leave out critical steps because they assume you have created packages in the past. Many of the current websites are not explaining how but more likely how to do it now, as the technology has evolved. Sorry, there is no perfect example yet.
- [packaging-python-in-2023](https://robamu.github.io/posts/packaging-python-in-2023/)

## Flat vs. src
The first thing to think about with the Python package is will this code be installable. Chances are if it is good code then some day (or initially) you will want to make the package installable. So take the time to think about and build out the file/directory/module strucutre.

Remeber that when there are folders in a Python package they translate into sub-modules when importing the package. For example the datetime package has a typical import like this:

<pre>
from datetime import datetime, date
date.today()
</pre>

This means the top level directory is called _datetime_ with a file called _datetime_ and _date_. In those files there is a method called _today_. 

A flat structure has the importable files from the packge directly in the main folder of the package. The src layout has another level with a directory called /src. The recomended structure is to use the src layout for reasons listed [here](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/).

## Required and optional files
A package has a number of required and optional files/directories. Many of the files can be created automatically when using GitHub or GitLab to create the repository. There are options to create the standard files. I suggest letting GitHub/GitLab create these for you. They have options for the language and licenses type.

<pre>
  LICENSE
  README.md
  requirements.txt
  .gitignore
  setup.py
</pre>

If a package needs to be built there will need to be instructions. The currently suggested way is with a _pyproject.toml_ file. The syntax of the file is not Python, it is yet another metadata format (as if we need another one). The older style using setup.py will still work but will someday be deprecated and may not work into the future. It is best to follow current best practices.

The _pyproject.toml_ file contains metada needed by the _build_ command to build the package. You can just copy some other file or [read the documentation](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/). Because the new method needs to handle other established methods, and people are building new ones there are plenty of optoins. For now you can start with the example one in this repository. The metada in the file is used during the build process to populate some required and optional values. As you desire more automation or complexity the file will grow with options to work with other tools to set values for you (like version from _Git_ tags or fixing linting with _ruff_).

Depending on how you want to implement the additional feature you may also still want a _setup.py_ file. This is the older method to provide instructions to the package build process. Most of the instructions that were in the _setup.py_ file can now be put in the _pyproject.toml_ but if an instruction or metadata is not able to be put into _pyproject.toml_ the _setup.py_ file is still executed.

## Directory structure
For the flat directory structure you may only have one file that contains all the functions or methods. This is fine and will work. For the src structure there will be an additional directory called /src which will contain the folder of the package name.

For both of these structures you will need `__init__.py` files. These files signify that a directory should be included in the loading phase of the package. If you are not able to see a directory or file after importing the packge check to see if you are missing this file. It does not need to contain any text, but if it does the code will be executed when the package is imported. This allows for some additional actions or varibles to be set at the time the package is imported. This can be nice for some things which are used often and you do not want to force the user to execute them every time the package is used. For example during the package build phase the version metadata is provided in the _setup.py_ or _pyproject.toml_ file. This version number can then be retrieved with a Pyton method. We can use this code to set a variable that is common with Python packages  `__version__` .
<pre>
from importlib import metadata
__version__ = metadata.version('act-atmos')
</pre>

Then when the user wants to see the version number of their package they can print that package variable. It is common to expect the package to have a \__version__ variable. And depending on how it is set it may be the more correct way to get the current version number.
<pre>
import act
act.__version__
</pre>

There is an anoying thing about \__inti__.py files and /src or flat structure. The \__init__.py file will tell Python the folder contains code to be read in. But when the \__init__.py file is in the /src folder it will not be executed. This requires an addition directory layer. So if there is code in the \__init__.py file to be executed your directory strucure will require an additional layer. Here is the pacakge _wildcat_ with its directory structure.

<pre>
wildcat/
|-- LICENSE
|-- README.md
|-- pyproject.toml
|-- src/
|   +-- __init__.py
|   +-- wildcat/
|      +-- wildcat.py
|      +-- __init__.py
</pre>

## Building and installing
A file can be imported for use with Python by simply importing the file (assuming it is in the same directory or in the PATH or PYTHONPATH)
<pre>
import awesome_file
result = awesome_file.awesome_program(stuff, more stuff)
</pre>

or importing the function from the file (assuming it is in the same directory or in the PATH or PYTHONPATH).
<pre>
from awesome_file import awesome_program
result = awesome_program(stuff, more stuff)
</pre>

But since we are talking about building a package we will be building the package and installing it into the Python lib area we will be using. The safest and most reliabe way to use Python is by creating a virtual environment of some sort typical with a package manager. There are many differnt ways and types of virtual environments but they all perform the same basic function. We can control the environment and packages install including the versions. This gives us control over our own project so we are not dependent on another project's requirements for package or versions. Common package managers to create the virtual environment inclue conda or Python venv. We can create the base virtual environment and then add packages to that environment to our specifications including the version of Python.

For this example lets use Python venv. This will create a folder in the current directory that will use the Python we normally use and contain the libraries we want to use for this project. Since only the libraries we want to use must be installed we will notice that the normal libraries will not be present until we install them in the new venv.

First we create the virtual environment. Notice we are going to use the Python we are currently using to make the virtual environent and we are naming the newly created virtual environment _venv_.
<pre>
python -m venv venv
</pre>
Then we activate the newly create environment. This can be done at anytime and we do not need to create the environment every time we want to use it. Once the environment is create it will be available for use. When the environment is activated we should see some additional text at the start of the command line indicating the environment is acvive. When we no longer want to operate in that environment we can exit with _deactivate_.
<pre>
>
. venv/bin/activate
(venv) > deactivate
>
</pre>

Since we want to build the project into an installable packge we need to install the package that will read our commands and build the package. When we install the _build_ packge we should be in the _venv_ environment so the _pip_ install is done into that package manager. This allows us to control where it is installed, removing it when we want and the version.
<pre>
. venv/bin/activate
(venv) > pip install build
</pre>

Now that we have our package created, the virtual environment built and running, and needed python packages installed we can build the package.
<pre>
(venv) > python3 -m build .
</pre>

This will build the package into a new folder called _dist_. The files in that folder can be used to install the package we just built on this or another machine. But notice the install would come from a static file. So any future updates would not be realized. This would be helpful for a produciton system where we do not want and testing or development changes to be implemented until we install them. But for development this would be a pain to need to rebuild every time we make a single change. _pip_ understands this need and has the  -e _editable_ option for installing. Using this option we can make changes to our package and they will be relaized immediatly. Notice we are using "." to indicate what to install with pip. This means install the package in the current directory so you need to be in the correct directory when running this command.
<pre>
(venv) > pip install -e .
</pre>

Now that we have the package installed we can import it and call any of the functions.
<pre>
(venv) > python
>>> from awesome_file import awesome_program
>>> result = awesome_program(stuff, more stuff)
</pre>
