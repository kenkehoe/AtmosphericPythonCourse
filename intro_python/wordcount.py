#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""wordcount.py"""

# import os
# import sys
import argparse
# import datetime


def main():
    """main"""
    args = parse_arguments()
    count_words(args.filename)


def count_words(filename):
    """count words and print results"""
    with open(filename) as f:
        text = f.read()  # Read whole file into a single string variable
        textlist = text.split()  # Split will turn string into a list, split
                                    #   by delim. If no delim passed,
                                    #   it splits on whitespace

        wc = {}  # Empty dictionary
        for word in textlist:
            wc[word] = wc.setdefault(word, 0)+1  # Increment counter for word.
                                                    #  If not in dict yet, add
                                                    #  with count 1

        # Print results
        for word in sorted(wc, key=wc.get, reverse=True):  # sort by count
            if wc[word] > 1:
                print(word+":"+str(wc[word]))


def parse_arguments():
    """Configure and return command line arguments"""
    parser = argparse.ArgumentParser(
            description="A program to count words in a file",
            epilog="ex: ./wordcount.py zen.txt"
            )

    parser.add_argument("filename",
                        help='Filename to open'
                        )

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()
