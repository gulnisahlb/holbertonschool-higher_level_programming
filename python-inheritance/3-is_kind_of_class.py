#!/usr/bin/python3
"""Hello world"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class, or of a class
    that inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if obj is an instance or subclass instance of a_class,
        else False.
    """
    return isinstance(obj, a_class)
