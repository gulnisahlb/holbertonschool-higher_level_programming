#!/usr/bin/python3
"""Print the result of the addition of all arguments."""

from sys import argv


if __name__ == "__main__":
    total = 0
    for arg in argv[1:]:
        total += int(arg)
    print(total)
