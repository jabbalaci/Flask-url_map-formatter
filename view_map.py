#!/usr/bin/env python3
# encoding: utf-8

import re
import sys

from termcolor import colored

from main import app

ROUTE_COLOR = 'green'
FN_COLOR = 'yellow'


def color(text, color, attrs=[]):
    return colored(text, color, attrs=attrs)


def bold(text, color='white'):
    return colored(text, color, attrs=['bold'])


def main():
    if len(sys.argv) == 2 and sys.argv[1] == "-n":
        print(app.url_map)
        return

    maps = str(app.url_map).split("\n")
    for line in maps:
        m = re.search(r"(.*)'(.*)'(.*)", line)
        if m:
            line = re.sub(r"(.*)'(.*)'(.*)",
                          r"\1'{}'\3".format(bold(m.group(2), ROUTE_COLOR)),
                          line)
        m = re.search(r"(.*) -> ([^>]*)(.*)", line)
        if m:
            line = re.sub(r"(.*) -> ([^>]*)(.*)",
                          r"\1 -> {}\3".format(bold(m.group(2), FN_COLOR)),
                          line)
        print(line)

##############################################################################

if __name__ == "__main__":
    main()
