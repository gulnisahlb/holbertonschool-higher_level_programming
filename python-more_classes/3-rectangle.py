#!/usr/bin/python3
"""3-rectangle.py: Defines a Rectangle and using '#'."""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with optional width and height."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter: set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter: set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle.
        If width or height is 0, perimeter is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle as a string of '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        lines = ['#' * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Return a string that can recreate the object."""
        return f"<3-rectangle.{self.__class__.__name__} object at {hex(id(self))}>"
