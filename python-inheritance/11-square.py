#!/usr/bin/python3
"""hello world"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """
        Initialize Square with size

        Size must be a positive integer validated by integer_validator
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return string representation: [Square] width/height"""
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
