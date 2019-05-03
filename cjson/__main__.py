# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import argparse
import curses
import cgitb
import os

from .paths import Paths
# Get more detailed traceback reports
cgitb.enable(format="text")  # https://pymotw.com/2/cgitb/


def chkfile(path):
    """
    Checks for valid file path.
    """
    if not os.path.isfile(path):
        msg = "{0} is not a file.".format(path)
        raise argparse.ArgumentTypeError(msg)
    return path


def getargs():
    """
    Return a list of valid arguments. If no argument is given, default to $PWD.
    """
    parser = argparse.ArgumentParser(description=(
    ))
    parser.add_argument("-s", "--source",
                        type=chkfile,
                        help="a valid path to a csv file.")
    return parser.parse_args()


def main(picked=[]):
    args = getargs()
    root = os.path.abspath(os.path.expanduser(args.path))
    hidden = args.hidden
    relative = args.relative
    paths = curses.wrapper(pick, root, hidden, relative)
    print("\n".join(paths))


if __name__ == '__main__':
    main()
