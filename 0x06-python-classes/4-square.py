#!/usr/bin/python3
"""
Define class Square with private size and public area
Can access and update size
"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """
        Initialize a new square
        Args:
            size (int): The size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Obtain and return size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set value of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

        def area(self):
            """Return the current area of the square."""
            return (self.__size * self.__size)
