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
A package has a number of required and optional files/directories. Many of the files can be created automatically when using GitHub or GitLab to create the repository. There are options to create the standard files. I suggest letting GitHub/GitLab create these for you. They have options for the language adn licenses type.

<pre>
  LICENSE
  README.md
  requirements.txt
</pre>

If a package needs to be built there will need to be instructions. The currently suggested way is with a _pyproject.toml_ file. The syntax of the file is not Python, it is yet another metadata format (as if we need another one). The older style using setup.py will still work but will someday be deprecated and may not work into the future. It is best to follow current best practices.

The _pyproject.toml_ file contains metada needed by the _build_ command to build the package. You can just copy some other file or [read the documentation](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/). Because the new method needs to handle other established methods, and people are building new ones there are plenty of optoins. For now you can start with the example one in this repository. The metada in the file is used during the build process to populate some required and optional values. As you desire more automation or complexity the file will grow with options to work with other tools to set values for you (like version from _Git_ tags or fixing linting with _ruff_).

