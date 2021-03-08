# AtmosphericPythonCourse
This is a simple and evolving class for learning Python 3.\* for use with data analysis, plotting and some other more scientific processing.

To use Python for this class you will need to use Python3.7 or greater and some additional libraries. Getting these libraries installed can be trivial or sometimes can be confusing. We suggest installing Anaconda python on your computer and use Anaconda python or to use the slimmed down versin Conda. This will also set you up to use Python on your personal machine right away after class to start doing work.

## Computer Setup
### Anaconda
We suggest you install Anaconda python on your machine. This is software that installs the latest version of Python (currently 3.8) and includes the most used additional libraries in the install so you don’t need to install them. 

Go to [Anaconda](https://www.anaconda.com/distribution/) and download the latest version. Follow your normal install steps to install Anaconda on your laptop. If you have an option to also install Git please select that as well.

### Conda
Conda is the trimmed down version of Anaconda that does not automatically install the additional libraries. This is sometimes better as only the libraries you desire are installed. It will correctly handle the library versioning. Using Conda correctly is a little more advanced, but worth the effort in the end.

## Clone the repo
You will need to use the revision control software Git to download the class materials. This should be an optional install as part of Anaconda or you may need to install it separately. 

All the teaching programs are in a GitHub repo. To get them enter the following commands on the terminal: 
(Mac users may be prompted to install xcode command line tools, choose install)
```
> cd (or change into a different directory to clone files)
> git clone https://github.com/kenkehoe/AtmosphericPythonCourse.git
> cd  AtmosphericPythonCourse
> ls (Windows: dir)
```

## Checking if everything is installed
As a last check to ensure everything is ready, run one script from the GitHub repo you just cloned. This will check if all the libraries you need for the class are installed.
```
> python test_requirements.py
```

Most of the libraries we will use are in the Anaconda suite. But there are some that we will use for this class you may need to install. Anaconda makes installing very simple. Just type this on the command line.
```
> pip install xarray pint
```

If nothing is printed after running this script then you are all set to go. If any libraries are printed to the screen use the pip install <missing library name> to install.
```
> pip install <missing library name>
```
  
## Text Editing
Finally you will need some way to edit the files. You can use your text editor of your choosing. Some options include VI (or [MacVIM](https://www.macupdate.com/app/mac/25988/macvim) for Mac), Emacs, TextEdit (Mac), [TextWrangler](https://apps.apple.com/us/app/textwrangler/id404010395?mt=12) (Mac), Notepad (Windows), [Notepad++](https://notepad-plus-plus.org/) (Windows), … It does not matter which one you choose but don’t use something like MicrosoftWord. It will not make you happy.

Enjoy and happy coding.


# Class Notes
## Intro Section
You should start with the *intro_pyton/* folder, specifically the [README](https://github.com/kenkehoe/AtmosphericPythonCourse/blob/master/intro_python/README.md) page. After going through the introl PDF you should go through the three python example files (files ending in \*.py) in the *intro_python/* folder.

## Advanced Section
Once you have a basic start to Python you can start working through the advanced libraries. Here is a suggestion for which files to review and the order. The files are designed to work by calling the python script from the command line (exampel = *> python data_numpy.py*). Each example file has blocks of code to process controld by an if statement. Just change "False" to "True" to execute those blocks of code. It is suggested to also change the previous "True" to "False" to limit the amount of information printed to the screen.

If you want to revert any of these codes back to orginal state just use the git command
```
> git checkout <name of file to revert back>
```
This will overwrite your current file with any changes to the one stored in the Git repo. If you have a file that is no longer working and you can't figure out why, you can copy that file to a different name and then checkout the orginal. This will allow comparing to see how they differ to find the error.

* [Numpy](https://docs.scipy.org/doc/numpy/reference/), (which is a subset of [SciPy](https://www.quora.com/What-is-the-difference-between-NumPy-and-SciPy)) - To work with arrays of data efficiently = **scientific_libaries/data_numpy.py**
* Plotting with [matplotlib](https://matplotlib.org/)  = **plotting/make_plot.py**
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - To store/read data and use some powerful tools with the data = **scientific_libaries/data_pandas.py**
* [Xarray](http://xarray.pydata.org/en/stable/) - To store/read data and use some powerful tools with the data over 1-D dimensionality = **scientific_libaries/data_xarray.py**
* Advanced plotting with matplotlib (also use Pandas and Xarray wrapper around matplotlib) = **scientific_libaries/make_plot_real_data.py**
* Advanced Xarray to start working with data and perform analysis = **scientific_libaries/data_xarray_2.py**
* Metadata with [JSON](https://developers.squarespace.com/what-is-json) and [YAML](https://blog.stackpath.com/yaml/) = **metadata/use_json.py** & **metadata/use_yaml.py**
* Advanced [pathlib.Path](https://realpython.com/python-pathlib/) = **cool_stuff/path_stuff.py**
* [Saving data with Numpy](https://www.geeksforgeeks.org/numpy-save/) = **cool_stuff/data_save.py**
* Using Python Collections extension for basic data structures = **cool_stuff/collections.py**
* Multiprocessing larger data blocks with [dask](https://docs.dask.org/en/latest/) = **scientific_libraries/data_data.py**
* Creating multiprocessing child processes for faster concurrentcy = **cool_stuff/data_multiprocessing.py**
* Tip of the iceberg with regular expressions = **cool_stuff/regular_expression.py**

## Standard Style
It is not required but we will encourage using a standard syntax for our code. All the example codes will use [pep8](https://www.python.org/dev/peps/pep-0008/). Your code will run without following this formatting standard, but for sharing the code with others getting used to a standard format will make everyone’s life better.

A nice way to see if your code is following the standard style is to use the [flake8](https://pypi.org/project/flake8/) command line tool. 
```
> flake8 --max-line-length=115 my_python_program.py
```

If something does not meet the standards it will give you the line number and short description of the issue. It just takes practice to understand the style and codes.
