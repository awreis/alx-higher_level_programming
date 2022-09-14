#!/usr/bin/python3
"""class Square with private attribute size and public attribute area"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """
        Initialize a new square
        Args:
            size(int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculate and return area of square"""
        return (self.__size)**2
