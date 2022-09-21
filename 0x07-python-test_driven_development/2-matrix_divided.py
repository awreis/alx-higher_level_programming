#!/usr/bin/python
"""
Module 2-matrix_divided
Defines a matrix division function
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix
    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0
    Returns:
        A new matrix representing the result of the division
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    samelen = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(msg)
        if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        newlist = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
