#!/usr/bin/python3
"""Hello World"""


class BaseGeometry:
    """Hello World"""

    def area(self):
        """hello world"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """hello world"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
