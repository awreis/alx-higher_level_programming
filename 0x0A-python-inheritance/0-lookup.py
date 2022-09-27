#!/usr/bin/python3
"""
Returns the list of available
attributes and methods of an object
"""

def lookup(obj):
    """Returns the list of attributes and Methods

    Args:
        obj: object to look into
    """

    return dir(obj)
