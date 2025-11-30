#!/usr/bin/python3
"""Hello world"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    from a specified class, excluding the class itself.

    Args:
        obj: The object to check.
        a_class: The class to compare.

    Returns:
        True if obj is an instance of a subclass of a_class,
        False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
