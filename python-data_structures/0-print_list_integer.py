#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers of a list, one per line, using str.format()"""
    for num in my_list:
        print("{:d}".format(num))
