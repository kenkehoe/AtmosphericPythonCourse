# Documentation for how to build a library that can be imported

Once you build amazing code you will find some functions will be used by many programs. Instead of copy/past the code the better option is to build a library that can be imported. That way if the code needs to be updated it can be done in one place. It also allows others to help develop the code.

This example is simiar to the more simple example where a file in the same directory contains a function that can be imported and called. But this example demonstrates how to build a library that can be shared with other projects. It is only slightly more complicated.

Typically when a function is imported from a file it will need to be in the same directory. That way the code

```from library_file import library_function```

knows where to look for the file named _library_file.py_ and that a function is defed in that file by the name of _library_function_.

So if we have the libary file in a different directory than the one the main level code is running (and you should do this), then we need to tell the Python intepreter where to look. There are a few ways to do this. The simplest way is to modify the PYTHONPATH environment variable. We can do that from the command line (this example is in bash)

```
export PYTHONPATH="$PYTHONPATH:/full/path/to/directory/containing/library/name"
```

This will need to be done every time the shell is started. I suggest you place this in your starup file (~/.bash_profile file for bash shell) so it is done automatically each time you start the shell.

A different but less good option is to append to the PATH environment variable in your main level Python program. This is less desireable because this bit of code will need to be added to every main level code and you will need to update _path_to_library_ if the library exists somewhere else than this example's. This information is presented so you have it, but I don't suggest you use it.

```
import sys
from pathlib import Path

path_to_library = Path(Path.cwd(), 'repository_example')
sys.path.append(path_to_library)
```

