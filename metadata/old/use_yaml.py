#! /usr/bin/env python3

import yaml


filename = 'example.yaml'
# The with statement ensures the file handle is closed after the file
# is read. This means we don't need to manage that part. A "with" works
# with any context manager.
with open(filename, "r") as fp:
    docs = yaml.load(fp, Loader=yaml.FullLoader)

print('type(docs):', type(docs))
print()
print('docs:\n', docs)
print()
print("type(docs['a_variable_name'])", type(docs['a_variable_name']))
print()
print("type(docs['b_variable_name'])", type(docs['b_variable_name']))
print()
print("type(docs['c_variable_name'])", type(docs['c_variable_name']))
print()
print("type(docs['d_variable_name'])", type(docs['d_variable_name']))
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
