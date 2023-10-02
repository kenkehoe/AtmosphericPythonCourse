#! /usr/bin/env python3

# Option 1. Copy and past this to the command line.
# export PYTHONPATH="$PYTHONPATH:$PWD/repository_example"

# Option 2. Uncomment these lines
# import sys
# from pathlib import Path

# path_to_library = Path(Path.cwd(), 'repository_example')
# sys.path.append(path_to_library)

from repository_example.mypythonlib.myfunctions import haversine

result = haversine(4.895168, 52.370216, 13.404954, 52.520008)
print(f"result = {result}")
