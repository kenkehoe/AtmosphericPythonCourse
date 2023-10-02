# Documentation for how to build a library that can be imported

Once you build some code you will find some functions will be used by many programs. Instead of copy/past the code the better option is to build a library that can be imported. That way if the code needs to be updated it can be done in one place. It also allows others to help develop the code.

This example is simiar to the more simple example where a file in the same directory contains a function that can be imported and called. But this example demonstrates how to build a library that can be shared with other projects. It is only slightly more complicated.

Typically when a function is imported from a file it will need to be in the same directory. That way the code

_from library_file import library_function_

knows where to look for the file named _library_file.py_ and that a function is defed in that file by the name of _library_function_.

