#!/usr/bin/python3
"""
Defines BaseGeometry class with area() and integer_validator().
"""


class BaseGeometry:
    """
    BaseGeometry class.
    """

    def area(self):
        """Raises an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): The name of the variable
            value (int): The value to validate
        """
        if type(value) is not int or type(value) is bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
