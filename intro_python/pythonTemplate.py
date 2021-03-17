#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""Template file for python 3 script"""

# import os
# import sys
import argparse
# import datetime


def main():
    """[docstring/purpose 
    of this script]"""
    args=parse_arguments()
    print("Required arg: ",args.requiredArg)

    if args.optionalArg : 
        print("Optional: ",args.optionalArg)
        
    if args.secondOptionalArg : 
        print("2nd Optional: ",args.secondOptionalArg)
        increment_number(args.secondOptionalArg)
  


def increment_number(n):
    try:
        n=n+1
        print("Incremented: ",n)
    except TypeError:
        print("Can't add to %s" % (type(n)))


def parse_arguments():
    """Configure and return command line arguments"""
    parser = argparse.ArgumentParser(
            description="A description for this script",
            epilog="An epilog for the help"
            )

    parser.add_argument("requiredArg")
    parser.add_argument("-o", "--optionalArg",
                        default='',
                        help='This is an optional argument'
                        )
    parser.add_argument("-s", "--secondOptionalArg",
                        default=0,
                        type=int,
                        help="""This is an optional argparse
                        that requires an int"""
                        )
    parser.add_argument("-b", "--booleanFlag",
                        action='store_true',
                        help="""True when passed, defaults to false""")

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()
