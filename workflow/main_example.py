#! /usr/bin/env python3

# The line above is called the shebang line. It should be the first line of the file.
# It allows the system to know what intepreter to
# call to parse this code, compile and call the compiled code. We could put a full path
# to the exact python executible (which python) but this allows us to say use Python 3.*
# and the system figures out which one to call. One specail thing to remember is that to
# use the shebang line the file permissions of this file need to be set to execute.

# Here we are importing the second and thrid party libaries. Convention suggest the imports
# are done at the top of the script and we only import things we actually use. Convention
# also suggest we put the second party libraries first then the thrid part libraries.
import argparse

# This is importing a function from a file in this directory. This is how you can better
# organize your code into different files and functions. Takes a little more effort
# but the clarity and ability to see where your code is failing is worth it.
# You can import more than one function from a file.
from library_example import argument_function, more_complicated_function


# Here is the main processing routine. It looks strange to have so many different functions
# but it allows for more modularity and easier debugging. So I suggest you go through
# the effort to add a few more lines of code. It will make your life better in the end.
def main():
    """
    Typically we will document what a function does and how to use it right after the
    def command. We can use the tripple quotes to allow multiple lines of documentation.
    There are some conventions for how to document the code. Does not really matter which
    one you choose, choose one and document.

    Example
    -------
    Using the -h keyword will print the help menu. It is abbreviated below for simplicity.

    > ./main_example.py -h
    usage:
    This is where you can add a description of the program...

    """

    # Call the function that parses the argumetns and keywords provided by command line.
    # This is called by a funciton written below. Python will read the entire file and compile
    # functions before executing them so the functions can be declared after they are called.
    args = parse_commandline()
    print('args:', args)

    # Now that we have the command line arguments we can go do something. Most likely the
    # logic of what to do next is based on the command line arguments and keywords.

    print(f"This is the keyword 'keyword' = '{args.keyword}'. It has a value even when not set.\n")

    if args.true_false_keyword:
        print("You set --true_false_keyword which sets the value to True\n")

    if args.float_keyword is not None:
        print(f"You set --float_keyword to '{args.float_keyword}'. "
              "Did you provide the number with decimal precision or did it get upconverted?\n")

    if args.keyword_list is not None:
        print(f"You set --keyword_list to {args.keyword_list}. "
              "Notice how it prints as a list even when you provide only one vale. It expects and makes a list.")

    # Here we will pass values into a function and retrieve something. This will be the
    # typical programing flow.
    result, value1, value2 = argument_function(args.argument, 'spam and eggs', value2=args.true_false_keyword)
    print(result)
    if value2:
        print(value1, value2)

    # more_complicated_function()
    # more_complicated_function('one', 2, 5-2, dogs=10, cats=99)


def parse_commandline():
    usage = '''
This is where you can add a description of the program and what it does.
We are using tripple quotes to allow multi-line text.

We can also insert the name of this program, %(prog)s, with this specail text.

Notice how resizing the window affects the help text.

Example for running;
> main_example.py one -tfk --float_keyword 2 --keyword_list two --keyword something_more
'''

    # Set up command-line options
    parser = argparse.ArgumentParser(usage=usage)

    parser.add_argument(
        "argument", type=str,
        help='''Here we pull in the positional arguments.
                An argument does not take a keyword and it is required.
                Notice how the spaces and returns in this help menu differ from the usage above.''')

    parser.add_argument(
        "-tfk", "--true_false_keyword", action="store_true",
        help="This one is a keyword used to set something to a boolean. We can define the default and set action.")

    parser.add_argument(
        "--keyword", help="This is a command line keyword.")

    parser.add_argument(
        "-f", "--float_keyword", default=None, type=float,
        help="""This is a keyword with a data type defined. If the value can not be converted to a
                float it will raise an error. Also notice how we can use -f or --float_keyword
                from the command line. Both work just fine. Also notice how the default is
                set to None.""")

    parser.add_argument(
        "-l", "--keyword_list", default=None, nargs='+', type=str,
        help="""This is a keyword that expects one or more values when set. It will set all values as
                strings. You can provide more than one value separated by a space.
                So what do you do when the thing you want to provide has a space?""")

    # Retrieve the command-line args and enable the help menu.
    # The data type is an argparse.Namespace
    args = parser.parse_args()

    # This will return args to the function that called this function. This is how we pass
    # varialbes between functions.
    return args


# Here is a bit code that uses a global varible __name__ to see what the name of the module
# is and if that variable is set to '__main__' then execute the code below. The reason we
# use this is to distingush the executible code expected to called when we call this program
# from the command line vs. library code. This allows us to mix code that can be imported
# by other programs from the code that is not intened to be imported. Convention suggests
# we use a function called main() but it does not need that name.
if __name__ == '__main__':
    main()
