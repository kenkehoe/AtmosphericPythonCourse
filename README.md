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


## Standard Style
It is not required but we will encourage using a standard syntax for our code. All the example codes will use pep8 (https://www.python.org/dev/peps/pep-0008/). Your code will run without following this formatting standard, but for sharing the code with others getting used to a standard format will make everyone’s life better.

A nice way to see if your code is following the standard style is to use the flake8 (https://pypi.org/project/flake8/) command line tool. 
```
> flake8 --max-line-length=115 my_python_program.py
```

If something does not meet the standards it will give you the line number and short description of the issue. It just takes practice to understand the style and codes.
