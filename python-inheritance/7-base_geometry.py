#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value

        Args:
            name (str): name (always string per task)
            value (int): must be integer > 0

        Raises:
            TypeError: if value is not an int OR is boolean
            ValueError: if value <= 0
        """
        # bool int-in subclassıdır → AYRI YOXLANMALIDIR!!!
        if type(value) is bool or type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
