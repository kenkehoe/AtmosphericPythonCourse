#! /usr/bin/env python3

import json

filename = 'example.json'   # Filename of JSON file
# If we needed to go to a different directory to get to the JSON
# file we can use relative or full path to the file.
# The with statement ensures the file handle is closed after the file
# is read. This means we don't need to manage that part. A "with" works
# with any context manager.
with open(filename, "r") as read_file:
    docs = json.load(read_file)

# The best way to ust this part is to open the JSON file and see how it is
# stuctured so you can see how the data types are nested and data are preserved.
# Feel free to mess with the JSON file to see how things change.
# You can alwasy get it back to orginal state with a "git checkout example.json"
print()
print('type(docs):', type(docs))
print()
# Notice how docs is read in as a nested dictionary
print('docs:\n', docs)
print()

# Here we can see how the JSON file preserves data type depending on the
# syntax used in the JSON file.
print("type(docs['a_variable_name'])", type(docs['a_variable_name']))
print()
print("type(docs['b_variable_name'])", type(docs['b_variable_name']))
print()
print("type(docs['c_variable_name'])", type(docs['c_variable_name']))
print()
print("type(docs['d_list_name'])", type(docs['d_list_name']))
print()
print("type(docs['site'])", type(docs['site']))
print()
print("docs['a_variable_name']:", docs['a_variable_name'])
print()
print("docs['site']['DEN']['lon']:", docs['site']['DEN']['lon'])
print()
print("docs['d_list_name']:", docs['d_list_name'])
print()
print("docs['d_list_name']:", docs['d_list_name']["five"])
