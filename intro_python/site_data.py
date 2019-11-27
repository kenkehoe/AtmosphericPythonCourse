#!/usr/bin/env python3
"""site_data.py"""
# _*_ coding: utf-8 _*_

# import os
# import sys
import argparse
from datetime import date

from matplotlib import pyplot as plt


def main():
    """Read in ccgg site file and plot results"""

    args = parse_arguments()
    data = read_site_data(args.filename, args.retainedData)

    # Simple plot
    if data:
        label, x, y = data
        plt.plot(x, y)
        plt.xlabel(label)
        plt.show()
    else:
        print("No data found to print")


def read_site_data(filename, retained):
    """Read passed file, strip comments and return data
        as (label, sample_dates, values) or false

        filename: path to target filename
        filter: True to return retained data only
    """
    sample_dates, values, label = [], [], ''

    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()  # ...any trailing/leading white space

                # Skip comments and empty lines
                if line.startswith("#") or len(line) == 0:
                    continue

                # Split cols into a list
                t = line.split()

                # Pull out target columns
                y, m, d = t[1:4]
                sample_date = date(int(y), int(m), int(d))
                value = float(t[11])
                site = t[0]
                flag = t[13][:1]  # First col of 3 char flag

                # print(flag,site,value,sample_date)
                # sys.exit()

                # If filtering see if flag starts with . and not a default val
                if (retained and flag != '.') or value < 0:
                    continue

                # Return data
                sample_dates.append(sample_date)
                values.append(value)

                # Set label if needed
                if not label:
                    label = "Retained " if filter else ""
                    label += "CO2 data from "+site

        return (label, sample_dates, values)

    except FileNotFoundError:
        print("File not found")

    return False


def parse_arguments():
    """Configure and return command line arguments"""
    parser = argparse.ArgumentParser(
            description="A description for this script",
            epilog="An epilog for the help"
            )

    parser.add_argument("filename")
    parser.add_argument("-r", "--retainedData",
                        action='store_true',
                        help="""Pass to filter results to non flagged data"""
                        )

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()
