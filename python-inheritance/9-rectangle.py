#!/usr/bin/python3
"""Hello world"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height

        Both must be positive integers validated by integer_validator
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation: [Rectangle] width/height"""
        return f"[Rectangle] {self.__width}/{self.__height}"
