#! /usr/bin/env python3

with open('requirements.txt') as requirements_file:
    # Parse requirements.txt, ignoring any commented-out lines.
    requirements = [line for line in requirements_file.read().splitlines()
                    if not line.startswith('#')]

modules = []
missing_modules = []
for x in requirements:
    try:
        modules.append(__import__(x))
#        print("Successfully imported ", x, '.')
    except ImportError:
        missing_modules.append(x)
#        print("Error importing ", x, '.')

if len(missing_modules) > 0:
    print('\nYou are missing some needed software. Pleas import these modules:')
    for mod in missing_modules:
        print(mod)

    print()

