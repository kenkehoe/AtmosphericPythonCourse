#! /usr/bin/env python3

import numpy as np

# Save data to a normal ASCII file
if True:
    # define data
    data = np.arange(10)
    # save to csv file
    np.savetxt('data.csv', data, delimiter=',')

    # read data from file
    read_data = np.loadtxt('data.csv', delimiter=',')
    # print the array
    print(read_data)

# Save multiple data to a normal ASCII file
if False:
    # define data
    data_1 = np.arange(10)
    data_2 = np.arange(10) + 100
    # save to csv file using lists of the data for multiple data.
    # The data need to be the same length
    np.savetxt('data.csv', [data_1, data_2], delimiter=',')

    # read data from file
    read_data = np.loadtxt('data.csv', delimiter=',')
    # print the array
    print(read_data)

if False:
    # define data
    data = np.arange(10)
    # save to Numpy bindary file
    np.save('data.npy', data)

    # read data from file
    read_data = np.load('data.npy')
    print(read_data)

if False:
    # define data
    data_1 = np.arange(10)
    data_2 = np.arange(20, dtype=float)
    data_3 = np.zeros(5, dtype=bool)
    filename = 'data.npz'
    # save to Numpy binary file
    np.savez(filename, data_1, data_2, data_3)

    # read data from file
    read_data = np.load(filename)
    # print the array
    print(read_data.files)
    print(read_data['arr_0'])

if False:
    # define data
    data_1 = np.arange(10000)
    data_2 = np.arange(20000, dtype=float)
    data_3 = np.zeros(5000, dtype=bool)
    filename = 'data.npz'
    # save to Numpy binary file
    np.savez(filename, data_1=data_1, data_2=data_2, data_3=data_3)

    # read data from file
    read_data = np.load(filename)
    # print the array
    print(read_data.files)
    for key in read_data.files:
        print(key, ':', read_data[key])

if False:
    # define data
    data_1 = np.arange(10000)
    data_2 = np.arange(20000, dtype=float)
    data_3 = np.zeros(5000, dtype=bool)
    filename = 'data_compressed.npz'
    # save to Numpy compressed binary file
    np.savez_compressed(filename, data_1=data_1, data_2=data_2, data_3=data_3)

    # read data from file
    read_data = np.load(filename)
    # print the array
    print(read_data.files)
    for key in read_data.files:
        print(key, ':', read_data[key])


    


