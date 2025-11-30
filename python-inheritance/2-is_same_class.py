#!/usr/bin/python3
"""
This module defines a function that checks if an object is exactly
an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class, else False.

    Args:
        obj: object to check
        a_class: class to compare

    Returns:
        True if obj is exactly instance of a_class, False otherwise
    """
    return type(obj) == a_class
