#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""Template file for python 3 script"""

# import os
# import sys
import argparse
# import datetime


def main():
    """[docstring/purpose of this script]"""
    print("Spam & eggs")

    args=parse_arguments()
    print(args.optionalArg)
    if args.secondOptionalArg : print(args.secondOptionalArg*2)


def parse_arguments():
    """Configure and return command line arguments"""
    parser = argparse.ArgumentParser(
            description="A description for this script",
            epilog="An epilog for the help"
            )

    parser.add_argument("requiredArg")
    parser.add_argument("-o", "--optionalArg",
                        default='spam',
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
