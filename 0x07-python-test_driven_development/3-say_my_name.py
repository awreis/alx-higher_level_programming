#!/usr/bin/python
"""
Module 3-say_my_name
Defines a name-printing function
"""


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
        first_name (str): The first name to print
        last_name (str): The last name to print
    Raises:
        TypeError: If either of first_name or last_name are not strings
    """
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {:s} {:s}".format(first_name, last_name))
    else:
        raise TypeError("{:s} must be a string".
                format("first_name" if isinstance(last_name, str)
                    else "last_name"))
