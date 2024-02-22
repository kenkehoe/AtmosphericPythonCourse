# Building a larger project
This file attempts to explain how to build a larger project with dependencies on other repositories and other code written by you.

## First thoughts
We need to have a general idea of what we want to be in this repository vs. imported and used in this repository. Initially we need an entry point. Typically we use single entry point file that accecpts arguments and keywords to allow driving the process. This folder contains a file _main_example.py_ that serves this purpose.

## Explaining the main program
The file uese argpase to accept and understand arguments and keywords. We can see what options are availalbe by using the _-h_ or _--help_ option. It will print a help menu and exit.

`./main_example.py -h`

Running this program will interpret the arguments and keywords and execute. For example:

<pre>
./main_example.py one -f 1.2 -tfk -l eggs spam

args: Namespace(argument='one', true_false_keyword=True, keyword=None, float_keyword=1.2, keyword_list=['eggs', 'spam'])
This is the keyword 'keyword' = 'None'. It has a value even when not set.

You set --true_false_keyword which sets the value to True

You set --float_keyword to '1.2'. Did you provide the number with decimal precision or did it get upconverted?

You set --keyword_list to ['eggs', 'spam']. Notice how it prints as a list even when you provide only one value. It expects and makes a list.
</pre>

Looking at _main_example.py_ we can see the file permissions are set to allow executing the code

`-rwxr-xr-x  1 kehoe  staff  6262 Feb 22 13:21 main_example.py`

and the first line of the file has a "shebang" line that tells the system this is a Python file and what Python executible to use to interpret the code. This is the Linux syntax but we can update for Windows if needed.

`line 1: #! /usr/bin/env python3`

When called the _main_example.py_ file is read from top to bottom and parsed/compiled. The _def_ word indicates a definition of a function, but the function is not automatically executed. Nothing is execute until end of file. This syntax will look at the _\_\_name\_\__ Python variable to see if it is set to the string _\_\_main\_\__. If so the if statement is executed which calls the _main()_ function defined previously.

<pre>
  if __name__ == '__main__':
    main()
</pre>

In _main()_ we call another predefined function that will handle command line input for arguments and keywords. The _parse_commandline()_ function defines the argument and keyword variable names, definitions and help menu. The function returns _arg_ which is an argparse Namespace object.
