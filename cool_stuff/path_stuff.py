#! /usr/bin/env python3

from pathlib import Path
import shutil
import datetime as dt

if True:
    # Create a full path directory from scratch
    # Notice the individual parts are individual strings, not list or tuple.
    full_path = Path("/one", "two", "three", "four")
    print("\nfull_path:", full_path)
    print("type(full_path):", type(full_path))
    print("type(str(full_path)):", type(str(full_path)))

    # Get the current work directory
    current_dir = Path.cwd()
    print("\ncurrent_dir:", current_dir)

    # Get user's home directory
    print("home:", Path.home())

    # Create a new path with an additional directory and a filename
    fl = current_dir.joinpath("new_dir", "my_awesome_file.py")
    print("\nparent:", fl.parent)  # Return just the path
    print("name:", fl.name)  # Return just the filename
    print("suffix:", fl.suffix)  # return the filename suffix
    print("stem:", fl.stem)  # return the filename without path or suffix
    print("anchor:", fl.anchor)  # return the base of the path

# Let's play with creating new directories and the directory parts.
if False:
    # Get the current direcotory path
    current_dir = Path.cwd()

    # Create a new path with additional directories and a file name
    fl = current_dir.joinpath("new_dir", "second_dir", "my_awesome_file.py")

    # Take a full path and split into parts.
    fl_pts = fl.parts
    print("\nparts:", fl_pts)
    print("type of parts:", type(fl_pts))
    print("parts as list:", list(fl_pts))
    print()

    # Now trim the path by using the parts and array indexing.
    print(fl)
    if True:
        # If we use the * character at the start of the tuple it will unpack
        # the tuple into individual parts to work with pathlib. If not pathlib
        # will not work. Think of the * as mulple returning individual strings.
        print(Path(*fl_pts[:-3]))
    else:
        # When we try to use the tuple returned from .parts in the Path
        # it will cause an error because Path does not accept a list or tuple.
        print(Path(fl_pts[:-3]))

    # The alternative is to string together multiple parents methods.
    # This is good when you know ahead of time how many levels down to go
    # but does not work when we don't know before compiling the program.
    print(fl.parent.parent.parent)

# Let's play with getting a list of files from a directory
if False:
    current_dir = Path.cwd()  # Get current directory
    print("current_dir:", current_dir)

    # Search for all file that end in .py in the directory.
    all_py_files = current_dir.glob("*.py")
    print("\nall_py_files:", all_py_files)  # Not this a generator not a list

    # Convert the generator to a list so we can see it. Notice how the individual
    # parts are still pathlib objects, not strings.
    all_py_files = list(all_py_files)
    print("\nlist:", all_py_files)

    # If we wanted to convert all individual pathlib objects to strings we can use
    # a for loop or even better a list comprehension
    conv_files = [str(x) for x in all_py_files]
    print("\nstr:", conv_files)

    # Print the first file from the pathlib list without the full path directory list.
    print("\nall_py_files[0].name", all_py_files[0].name)

# Let's play with making directories and files then renaming, deleting files and directories.
if False:
    # Make a new path using current directory as base.
    current_dir = Path.cwd()
    new_dirs = current_dir.joinpath("one", "two")

    # Actually create the new directory. Using the parents keyword to make multiple
    # directories all at once.
    new_dirs.mkdir(parents=True, exist_ok=True)

    # Add a thrid level directory. Use exist_ok to do nothing if the
    # directory already exists. Otherwise there will be an error.
    add_dir = new_dirs.joinpath("three")
    add_dir.mkdir(exist_ok=True)

    # Create a new pathlib with a filename.
    new_file = new_dirs.joinpath("file.txt")
    # Use this new pathlib to write text to a file.
    new_file.write_text("Hello world")

    # Change the suffix from .txt to .text_name
    print("\nwith_suffix:", new_file.with_suffix(".text_name"))
    # Change the full file name from file.text_name to a_new_file.txt
    print("\nwith_name:", new_file.with_name("a_new_file.txt"))
    # Read the file and print.
    print("\nread_text:", new_file.read_text())

    if False:
        # Create a new pathlib path one directory down from previous
        # made directory pathlib.
        new_dirs2 = new_dirs.parent
        print(new_dirs2)
        new_file2 = new_dirs2.joinpath("greatest_file_ever.csv")
        # Create the file, with nothing inside.
        new_file2.touch()
        # Use the pathlib path to extract the directory path and create
        # a new full path filename.
        new_file3 = new_file2.parent.joinpath("good_not_great_file.csv")
        # Use this with a new name to rename the file.
        new_file2.replace(new_file3)

    if False:
        # Delete a file. Note, it will not ask if you are sure, so be careful.
        new_file.unlink()

        # Delete a directory. The directory needs to be empty. It will not ask
        # if correct directroy so be careful.
        add_dir.rmdir()

    if False:
        # Use the current directory to get path to base of our new directory tree.
        rm_dir = Path.cwd().joinpath("one")
        print("\nrm_dir:", rm_dir)

        # Use a different library to delete a directory with something in it.
        # Be VERY CAREFUL with this!!!!!
        shutil.rmtree(rm_dir)

# Let's play with metadata about the file.
if False:

    # Creaet pathlib path to this file in current directory.
    new_file = Path("path_stuff.py")

    # Get information about the file
    stats = new_file.stat()
    print("\nstats:\n", stats)

    # Print size of file in bytes
    print("\nst_size: ", stats.st_size)

    # Print the three different times associated with the file
    print("\nst_ctime:", dt.datetime.utcfromtimestamp(stats.st_ctime))
    print("st_mtime:", dt.datetime.utcfromtimestamp(stats.st_mtime))
    print("st_atime:", dt.datetime.utcfromtimestamp(stats.st_atime))

# Play with some more advanced Pathlib stuff to find specific files.
if False:

    # Normal creation of a path
    if True:
        data_path = Path("..", "data", "sgpmetE13.b1")
    else:
        # Using a special "/" operator. This will add directories
        # or files to an existing path. It is actually OS independent and will
        # work on Windows even if the path separator is not that character.
        data_path = Path.cwd() / ".." / "data" / "sgpmetE13.b1"

    # Use glob method to search the directory for files ending in '.cdf'
    files = data_path.glob("*.cdf")

    # loop over all the returned files and check if the data is in that pathlib object.
    # Need to perform match on a single pathlib object entry, hence the loop.
    for fl in files:
        print(fl, fl.match("*.20191101.*"))

# Use the recursive file glob to look for files in a data directory tree.
if False:
    # Make a relative path pathlib to base of data directory
    data_path = Path("..", "data")
    # Initiallize an emptch list
    files = []
    # Recursively search for a file ending in old netCDF extension. Extend the exising
    # list by adding on the list of returned matched files.
    files.extend(data_path.rglob("*.cdf"))
    # Recursively search for a file ending in new netCDF extension. Extend the exising
    # list by adding on the list of returned matched files.
    files.extend(data_path.rglob("*.nc"))

    # Print number of files found
    print("\nlen(files):", len(files))
    print()

    # Loop over list printing each filename.
    for fl in files:
        print(fl)


print()
