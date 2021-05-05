#! /usr/bin/env python3

import numpy as np
import pickle

# Save data to a normal ASCII file
if False:
    # define data
    data = np.arange(10)

    # save to csv file
    np.savetxt("data.csv", data, delimiter=",")

    # read data from file
    read_data = np.loadtxt("data.csv", delimiter=",")

    # print the array
    print(read_data)

# Save multiple data to a normal ASCII file
if False:
    # define data
    data_1 = np.arange(10)
    data_2 = np.arange(10) + 100

    # Save to csv file using lists of the data for multiple data.
    # The data need to be the same length because saving each list as a new row.
    np.savetxt("data.csv", [data_1, data_2], delimiter=",")

    # read data from file
    read_data = np.loadtxt("data.csv", delimiter=",")

    # print the array
    print(read_data)

if False:
    # define data
    data = np.arange(10)

    # save to Numpy bindary file
    np.save("data.npy", data)

    # read data from file
    read_data = np.load("data.npy")
    print(read_data)

if False:
    # define data
    data_1 = np.arange(10)
    data_2 = np.arange(20, dtype=float)
    data_3 = np.zeros(5, dtype=bool)
    filename = "data.npz"

    # save to Numpy binary file
    np.savez(filename, data_1, data_2, data_3)

    # read data from file
    read_data = np.load(filename)

    # print the array
    # Notice the use of the .files method. Strange name but this is what
    # Numpy chose for the data objects in the written data file. Also notice
    # how the name of the variables are not consistent. So you just need to
    # handle this in your code.
    list_names = read_data.files
    print(list_names)
    print(read_data[list_names[0]])

if False:
    # What if we want to preserve the variable name when read from the Numpy file?
    # define data
    data_1 = np.arange(10000)
    data_2 = np.arange(20000, dtype=float)
    data_3 = np.zeros(5000, dtype=bool)
    filename = "data.npz"
    # save to Numpy binary file and define the name of the variabls when saving.
    np.savez(filename, data_1=data_1, data_2=data_2, data_3=data_3)

    # read data from file
    read_data = np.load(filename)

    # print the array
    print('read_data.files:', read_data.files)
    for var_name in read_data.files:
        print(var_name, ":", read_data[var_name])

if False:
    # What if the data is large and we need to save space when writing the data
    # to disk. We can compress the data and uncompress when reading.

    # define data
    data_1 = np.arange(10000)
    data_2 = np.arange(20000, dtype=float)
    data_3 = np.zeros(5000, dtype=bool)
    filename = "data_compressed.npz"

    # save to Numpy compressed binary file
    np.savez_compressed(filename, data_1=data_1, data_2=data_2, data_3=data_3)

    # read data from file. Notice how we didn't say it was compressed data, it
    # just figured it out.
    read_data = np.load(filename)

    # print the array
    print('read_data.files:', read_data.files)
    for var_name in read_data.files:
        print(var_name, ":", read_data[var_name])

if True:
    # What if we want to save object that are not Numpy? Then we can use a different
    # method called Pickel. This will write the object as an object to the binary
    # file and return it as the Python object.

    # NOTE:
    # Pickle files can be hacked. If you receive an unverified raw pickle file,
    # don't trust it! It could have malicious code in it, that would run arbitrary
    # python when you try to de-pickle it.

    if True:
        # Create a dictionary with information
        favorite_color = {"lion": "yellow", "kitty": "red"}

        # Dump the dictionary to a binary file as a dictionary.
        filename = "save.pkl"
        pickle.dump(favorite_color, open(filename, "wb"))

        # Remove the dictionary just to prove it is read in.
        del favorite_color

        # Read the dictionary back into memory
        favorite_color = pickle.load(open(filename, "rb"))
        print("favorite_color:", favorite_color)

    # We can also pickel multiple variables and return them to multiple variables.
    if True:
        # Create a dictionary with information
        favorite_color = {"lion": "yellow", "kitty": "red"}
        favorite_season = 'winter'
        favorite_numbers = [4, 42, np.pi]
        favorite_series = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], dtype=np.int8)

        # Dump the different objects to a single file. For the pickle.dump() method
        # to work we need to pass in one object. That object can contain as many different
        # objects as we want.
        filename = "save.pkl"
        with open(filename, "wb") as f:
            single_tuple = (favorite_color, favorite_season, favorite_numbers, favorite_series)
            pickle.dump(single_tuple, f)

        # Remove the dictionary just to prove it is read in.
        del favorite_color, favorite_season, favorite_numbers, favorite_series

        # Read the dictionary back into memory
        favorite_color, favorite_season, favorite_numbers, favorite_series = \
            pickle.load(open(filename, "rb"))
        print("favorite_color:", favorite_color)
        print("favorite_season:", favorite_season)
        print("favorite_numbers:", favorite_numbers)
        print("favorite_series:", favorite_series, favorite_series.dtype)
