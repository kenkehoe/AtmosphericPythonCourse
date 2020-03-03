# Intro Python Module

A good online free tutorial is available at [datacamp.com](https://www.datacamp.com/courses/intro-to-python-for-data-science). This is a 4 hour course that should give you the basics of Python programming. It would also be good to review the PDF in this folder for some other detials the course may not teach.

You are welcome to follow the instructions in the datacamp.com class for how to use Python, but we suggest using Python in the way you will do large processing. We suggest installing Python through Anaconda and using it on the command line by executing a file. This course is set up assuming you can call a Python script from a terminal window. You can call the script by
```
python script_name.py
```
This will execute the code in the file and do what it stated. You can also develop your code with a terminal window to call the Python script and a second terminal window with interactive Python (ipython) to test things out as you write your code. This is a nice way to test one line at a time to see the correct syntax.

Or you will need to change the permissions of the file to allow the script to be executed by the Python interpriter. For example to change the permissions on Linux or Mac
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
