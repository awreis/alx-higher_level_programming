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
        return self.__width

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
        self.__width = value

    @property
    def height(self):
        """Retrieves the width of a Rectangle instance."""
        return self.__height

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
        self.__height = value

    def area(self):
        """Calsulates the area of the Rectangle

        Returns:
            Area of the rectangle, as the product of height and width
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle

        Returns:
            Perimeter of the rectangle, as the sum of the height and
            width times 2
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic

    def __repr__(self):
        """Return a string representation of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
