#!/usr/bin/python3
"""
Defines a Rectangle Class
"""


class Rectangle:
    """Defined width and height of a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.

        Args:
            height: height of the rectangle
            width: width of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves the width of a Rectangle instance."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the width of a Rectangle instance

        Args:
            value: value of the height, must be a positive
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calsulates the area of the Rectangle

        Returns:
            Area of the rectangle, as the product of height and width
        """
        return self._width * self._height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle

        Returns:
            Perimeter of the rectangle, as the sum of the height and
            width times 2
        """
        if self._width == 0 or self._height == 0
            return 0
        return 2 * (self._width + self._height)
