import time


def some_function(input_tuple):
    if isinstance(input_tuple, (tuple, list)):
        inputs, wait = input_tuple
    elif isinstance(input_tuple, (int, float)):
        wait = input_tuple
        inputs = 'some_function'
    else:
        wait = 0
        inputs = 'some_function'

    # Wait for some number of seconds
    print(f"Starting processs '{inputs}'\tWaiting {wait} seconds")
    time.sleep(int(wait))
    print(f"Process '{inputs}'' complete. Waited {wait} seconds to finish")

    return (inputs, wait)
