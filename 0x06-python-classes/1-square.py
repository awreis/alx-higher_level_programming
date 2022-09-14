#!/usr/bin/python3
"""Define class Square with private attribute size"""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """
        Initialize a new square

        Args:
        size: size of new square
        """
        self.__size = size
