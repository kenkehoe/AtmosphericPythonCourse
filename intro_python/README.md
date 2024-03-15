# Intro Python Module

A good online free tutorial is available at [datacamp.com](https://www.datacamp.com/courses/intro-to-python-for-data-science). This is a 4 hour course that should give you the basics of Python programming. It would also be good to review the PDF in this folder for some other details the course may not teach.

## Executing a Python script
You are welcome to follow the instructions in the datacamp.com class for how to use Python, but we suggest using Python in the way you will do large processing. We suggest installing Python through Anaconda and using it on the command line by executing a file. This course is set up assuming you can call a Python script from a terminal window. You can call the script by
```
python script_name.py
```
This will execute the code in the file and do what it stated. You can also develop your code with a terminal window to call the Python script and a second terminal window with interactive Python (ipython) to test things out as you write your code. This is a nice way to test one line at a time to see the correct syntax.

Or you will need to change the permissions of the file to allow the script to be executed by the Python interpreter. For example, to change the permissions on Linux or Mac:
```
> ls -l python_script.py 
-rw-r--r--  1 kehoe  staff  0 Mar  3 14:45 python_script.py
```
This -rw-r--r-- part indicates the file is readable but not able to be executed. To change the permissions use *chmod*.
```
> cchmod u=rwx,g=r,o=r python_script.py
> ls -l python_script.py
-rwxr--r--  1 kehoe  staff  0 Mar  3 14:45 python_script.py
```
Now we can just call the script (assuming you have the shibang set correctly in the first line of the script)
```
> python_script.py
```
It is up to you which you prefer.

## Running your first program
You can test out your first program by running the script in /intro_python folder called wordcount.py
```
> python wordcount.py siteData.py
```
This is a simple (and somewhat silly) program to count the number of words in the file "siteData.py" Take a look at the output and then read through the code to see what it is doing. If you want you can change the code (maybe add a print() statement) and see what that does. Don't worry if you mess it up, you can always use *git checkout wordcount.py* to get back the original version.


## Reading in a data file and making a plot
Next we can do the most important thing in science, reading in a data file and making a plot. You will do this a lot in atmospheric science. We can use the already written program to do this for you.
```
> python siteData.py data/co2_alt_surface-flask_1_ccgg_event.txt
```
Notice how it opened up a new window and made a plot. You can point to a different file in the /data/ directory and get a different plot.
```
> python siteData.py data/co2_spo_surface-flask_1_ccgg_event.txt
```

Next, change some things in the siteData.py program to see how the plot changes.

You can also see how the program is written to be user friendly. If you didn't know how to use it you can get information from the script printed to the screen. This is a special module in the python file that will show a help menu.
```
> siteData.py -h
usage: siteData.py [-h] [-r] filename

A description for this script

positional arguments:
  filename

optional arguments:
  -h, --help          show this help message and exit
  -r, --retainedData  Pass to filter results to non flagged data

An epilogue for the help
```

Can you add an option so the help menu changes? A good way to do this is to copy a section of code and make the variable name different.
