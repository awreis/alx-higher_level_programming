#!/usr/bin/python3
"""Define Sqaure class with private instance attribute size"""

    class Square:
        """Represent a square"""

        def __init__(self, size=0):
            """
            Initialize a new square

            Args:
                ___size(int): size of a side of a square, defaults to 0 if none
            """
            if type(size) is not int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
