#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(argc, "" if argc == 1 else "s"))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
