# AtmosphericPythonCourse
This is a simple and evolving class for learning Python 3.\* for use with data analysis, plotting and some other more scientific processing.

To use Python for this class you will need to use Python3.7 or greater and some additional libraries. Getting these libraries installed can be trivial or sometimes can be confusing. Hopefully we can walk though getting you set up with little effort.

This course is designed to work with Jupyter Notbooks. You can run a Jupter notebook locally or through a JupyterHub website. But the Jupyter Notebook is stored in the repo with the cells executed. This will let you use this repo as a reference as well as a training tool. There is no need to memorize the specific syntax. Just come back here an look it up. It will come eventually with use.

## Computer Setup
### Jupyter Notebooks
Jupyter Notebooks are an interactive method to run Python code and have rich text mixed together to provide the best experience.

## Clone the repo
You will need to use the revision control software Git to download the class materials. 

All the teaching Notebooks are in a GitHub repo. To get them enter the following commands on the terminal: 
(Mac users may be prompted to install xcode command line tools, choose install)
```
> cd (or change into a different directory to clone files)
> git clone https://github.com/kenkehoe/AtmosphericPythonCourse.git
> cd  AtmosphericPythonCourse
> ls (Windows: dir)
```

## Checking if everything is installed
As a last check to ensure everything is ready, run one Notebook from the GitHub repo you just cloned. This will check if all the libraries you need for the class are installed. Open _test_requirements.ipynb_ and execute the code block to check if you have all the necessary libraries installed. If not follow the instructions.
  
## Text Editing
Eventually you will want some way to edit the Python files you develop. For now you can ignore this section and come back to this when you want to write a Python script file and execute from the command line. You can use your text editor of your choosing. Some options include VI (or [MacVIM](https://www.macupdate.com/app/mac/25988/macvim) for Mac), Emacs, TextEdit (Mac), [TextWrangler](https://apps.apple.com/us/app/textwrangler/id404010395?mt=12) (Mac), Notepad (Windows), [Notepad++](https://notepad-plus-plus.org/) (Windows), [Sublime Text](https://www.sublimetext.com/), … It does not matter which one you choose but don’t use something like MicrosoftWord. It will not make you happy.

# Class Notes
Once you have a basic start to Python you can start working through the advanced libraries. Below is a suggestion for which files to review and the order. You should not save the files after editing, or if you do want to save a change save to a different name. If you do make a change and accidentally save the Notebook files you can revert any of the files back to orginal state by using the git command
```
> git checkout <name of file to revert back>
```
This will overwrite your current file with any changes to the one stored in the Git repo. If you have a file that is no longer working and you can't figure out why, you can copy that file to a different name and then checkout the orginal. This will allow comparing to see how they differ to find the error.

# Class syllabus
There is no required order to go throgh this class but this list is pretty good order. You are free to skip over the sections that do not pertain right now, but you should be exposed to all thse topics at some point so you understand the suggested Python solutions. 

* Introduction to Python
  * [Intro to Python.pdf](/intro_python/Intro%20to%20Python.pdf)
  * [interactiveDemos_01.ipynb](intro_python/interactiveDemos_01.ipynb)
  * [interactiveDemos_02.ipynb](intro_python/interactiveDemos_02.ipynb)
* [Numpy](https://docs.scipy.org/doc/numpy/reference/), (which is a subset of [SciPy](https://www.quora.com/What-is-the-difference-between-NumPy-and-SciPy)) - To work with arrays of data efficiently = [Scientific_Libraries_Numpy.ipynb](scientific_libraries/Scientific_Libraries_Numpy.ipynb)
* Plotting with [matplotlib](https://matplotlib.org/)  = [make_plot.ipynb](plotting/make_plot.ipynb)
* [Pandas](https://pandas.pydata.org/pandas-docs/stable/) - To store/read data and use some powerful tools with the data = [scientific_libraries/Scientific_Libraries_Pandas.ipynb](Scientific_Libraries_Pandas.ipynb)
* [Xarray](http://xarray.pydata.org/en/stable/) - To store/read data and use some powerful tools with the data over 1-D dimensionality = [Scientific_Libraries_Xarray.ipynb](scientific_libraries/Scientific_Libraries_Xarray.ipynb)
* Advanced plotting with matplotlib (also use Pandas and Xarray wrapper around matplotlib) = [make_plot_real_data.ipynb](plotting/make_plot_real_data.ipynb)
* Advanced Xarray to start working with data and perform analysis = [Scientific_Libraries_Xarray_2.ipynb](scientific_libraries/Scientific_Libraries_Xarray_2.ipynb)
* Metadata with [JSON](https://developers.squarespace.com/what-is-json) and [YAML](https://blog.stackpath.com/yaml/) = [use_json.ipynb](metadata/use_json.ipynb) & [use_yaml.ipynb](metadata/use_yaml.ipynb)
* Handling paths and filepaths [pathlib.Path](https://realpython.com/python-pathlib/) = [path_stuff.ipynb](cool_stuff/path_stuff.ipynb)
* [Saving data with Numpy](https://www.geeksforgeeks.org/numpy-save/) = [data_save.ipynb](cool_stuff/data_save.ipynb)
* [Atmospheric data Community Toolkit (ACT)](https://github.com/ARM-DOE/ACT)
  * [ACT Examples](https://github.com/ARM-DOE/ACT/tree/main/examples)
  * [Download data](third_party_libraries/ACT_download_data.ipynb)
  * [Plot Data](https://github.com/ARM-DOE/ACT/blob/main/examples/plotting/plot_ceil.py)
  * Reading, QC, formatting, plotting with [ACT](third_party_libraries/ACT.py)
  * [Plot with preprocessing](https://github.com/ARM-DOE/ACT/blob/main/examples/plotting/plot_daytime_averages.py)
  * Intro to QC and ACT = [ACT_QC.ipynb](third_party_libraries/ACT_QC.ipynb)
  * Work with and Plot QC = [plot_arm_qc.py](https://github.com/ARM-DOE/ACT/blob/main/examples/qc/plot_arm_qc.py)
  * Building your own QC = [plot_qc_example.py](https://github.com/ARM-DOE/ACT/blob/main/examples/qc/plot_qc_example.py)
  * Download, read and plot NOAA SurfRad data = [plot_surfrad.py](https://github.com/ARM-DOE/ACT/blob/main/examples/io/plot_surfrad.py)
  * Download, read and plot ANL Sodar data - [plot_sodar.py](https://github.com/ARM-DOE/ACT/blob/main/examples/io/plot_sodar.py)
  * [Retrieve stability indicies from a sounding](https://github.com/ARM-DOE/ACT/blob/main/examples/retrievals/plot_get_stability_indices_example.py)
  * [Cloud Base Height Retrievals](https://github.com/ARM-DOE/ACT/blob/main/examples/retrievals/plot_cbh_sobel.py)
  * [Example to merge multiple data products into one using ACT.](https://github.com/ARM-DOE/ACT/blob/main/examples/workflows/plot_merged_product.py)
  * [ARM Tutorials](https://github.com/ARM-Development/ARM-Notebooks/tree/main/Tutorials/arm-asr-pi-meeting-2023/ACT_tutorial)
* Requested Examples
  * [CSV to netCDF](examples/csv_to_netcdf.ipynb)
  * [Xarray time matching Examples](examples/Examples.ipynb)
* Using Python Collections extension for basic data structures = [collections.ipynb](cool_stuff/collections.ipynb)
* Multiprocessing larger data blocks with [dask](https://docs.dask.org/en/latest/) = [Scientific_Libraries_Dask.ipynb](scientific_libraries/Scientific_Libraries_Dask.ipynb)
* Creating multiprocessing child processes for faster concurrentcy = [data_multiprocessing.ipynb](cool_stuff/data_multiprocessing.ipynb)
* Tip of the iceberg with regular expressions = [regular_expressions.ipynb](cool_stuff/regular_expressions.ipynb)
* Logging = [loggin.ipynb](cool_stuff/loggin.ipynb)
* How to set up a working program with a command line script and library functions = [main_example.py](workflow/main_example.py), [exception_handling.ipynb](workflow/exception_handling.ipynb)
* Testing you code = [python_testing.ipynb](testing/python_testing.ipynb)

## Standard Style
It is not required but we will encourage using a standard syntax for our Python files. All the Python example codes use [pep8](https://www.python.org/dev/peps/pep-0008/). Your code will run without following this formatting standard, but for sharing the code with others getting used to a standard format will make everyone’s life better.

A nice way to see if your code is following the standard style is to use the [flake8](https://pypi.org/project/flake8/) command line tool. 
```
> flake8 --max-line-length=115 my_python_program.py
```

If something does not meet the standards it will give you the line number and short description of the issue. It just takes practice to understand the style and codes.
