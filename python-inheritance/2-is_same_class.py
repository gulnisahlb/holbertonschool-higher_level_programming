#!/usr/bin/python3
"""
Module 2-is_same_class

This module defines a function that returns True if the object
is exactly an instance of the specified class, otherwise False.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if obj is exactly an instance of a_class, else False.
    """
    return type(obj) is a_class
