# AtmosphericPythonCourse

This is a Git repo of some example python3 files. It is designed to work by calling the
python script from the command line. Each example file has blocks of code to process
controld by an if statement. Just change "False" to "True" to execute those bits of code.
It is suggested to also change the previous "True" to "False" to limit the amount of
information printed to the screen.

There is also a test_requirements.py script that will ensure all the libraries listed
in requirements.txt are installed. Run that script to check for missing libraries.
If a missing library is detected insall using pip.
```
> pip install <missing library name>
```
Enjoy and happy coding.


# Class Notes
## Intro Section
You should start with the intro_pyton folder for the PDF presentation that explains some of the basics of Python. After going through the introl PDF you should go through the three python example files (files ending in \*.py) in the intro_python file.

## Advanced Section
Once you have a basic start to Python you can start working through the advanced libraries. Here is a suggestion for which files to review and the order.

* [Numpy](https://docs.scipy.org/doc/numpy/reference/), (which is a subset of [SciPy](https://www.quora.com/What-is-the-difference-between-NumPy-and-SciPy)) - To work with arrays of data efficiently = scientific_libaries/data_np.py
  * Maybe skip masked arrays and Python datetime object for time?
* Plotting with matplotlib  = plotting/make_plot.py
* Pandas - To store/read data and use some powerful tools with the data = scientific_libaries/data_pandas.py
* Xarray - To store/read data and use some powerful tools with the data over 1-D dimensionality = scientific_libaries/data_xarray.py
* Advanced plotting with matplotlib (also use Pandas and Xarray wrapper around matplotlib) = scientific_libaries/make_plot_real_data.py
* Advanced Xarray to start working with data and perform analysis = scientific_libaries/data_xarray_2.py
* Metadata with JSON and YAML = metadata/use_json.py & use_yaml.py
* Advanced pathlib.Path = cool_stuff/path_stuff.py
* Saving data with Numpy = cool_stuff/data_save.py




## Standard Style
It is not required but we will encourage using a standard syntax for our code. All the example codes will use [pep8](https://www.python.org/dev/peps/pep-0008/). Your code will run without following this formatting standard, but for sharing the code with others getting used to a standard format will make everyone’s life better.

A nice way to see if your code is following the standard style is to use the [flake8](https://pypi.org/project/flake8/) command line tool. 
```
> flake8 --max-line-length=115 my_python_program.py
```

If something does not meet the standards it will give you the line number and short description of the issue. It just takes practice to understand the style and codes.
