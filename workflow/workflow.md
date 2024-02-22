# Building a larger project
This file attempts to explain how to build a larger project with dependencies on other repositories and other code written by you.

## First throughs
We need to have a general idea of what we want to be in this repository vs. imported and used in this repository. Initially we need an entry point. Typically we use single entry point file that accecpts arguments and keywords to allow driving the process. This folder contains a file _main_example.py_ that serves this purpose.

The file uese argpase to accept and understand arguments and keywords. We can see what options are availalbe by using the _-h_ or _--help_ option. It will print a help menu and exit.

`./main_example.py -h`
