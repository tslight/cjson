# Copyright (c) 2018, Toby Slight. All rights reserved.
# ISC License (ISCL) - see LICENSE file for details.

import argparse
import curses
import os
from color import color
from header import header
from footer import footer
from body import body
from keys import keys
from get_json import get_json


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
    parser.add_argument("path",
                        type=chkfile,
                        help="a valid path to a json file.")
    return parser.parse_args()


def print_list(txt, values, indent=0):
    for e in values:
        if isinstance(e, dict):
            print_dict(txt, e, indent)
        elif isinstance(e, list):
            print_list(txt, e, indent+4)
        else:
            txt.addstr(' ' * indent + str(e) + '\n')


def print_dict(txt, data, indent=0):
    for key, value in data.items():
        # txt.addstr(str(key) + " = " + str(value) + "\n")
        txt.addstr(' ' * indent + str(key) + '\n')
        if isinstance(value, dict):
            print_dict(txt, value, indent+4)
        elif isinstance(value, list):
            print_list(txt, value, indent+4)
        else:
            txt.addstr(' ' * (indent+4) + str(value) + '\n')


def eventloop(screen, div, txt, data):
    while True:
        txt.erase()
        print_dict(txt, data)
        txt.refresh()
        keys(screen)
        # refresh the windows from the bottom up
        screen.noutrefresh()
        div.noutrefresh()
        txt.noutrefresh()
        curses.doupdate


def cjson(screen, path):
    curses.curs_set(0)
    color()
    header(screen)
    footer(screen)
    div, txt = body(screen)
    data = get_json(path)
    eventloop(screen, div, txt, data)


def main():
    args = getargs()
    curses.wrapper(cjson, args.path)


if __name__ == '__main__':
    main()
