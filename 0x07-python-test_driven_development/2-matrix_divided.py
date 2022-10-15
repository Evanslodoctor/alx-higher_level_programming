#!/usr/bin/python3
""" This module provides a function to divide a matrix by a number. """


def matrix_divided(matrix, div):
    """ Divide each element of a matrix by a number. """
    if not (matrix and
            isinstance(matrix, list) and
            all(isinstance(row, list) and
                all(isinstance(item, (float, int))
                    for item in row) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(len(a) == len(b) for a, b in zip(matrix, matrix[1:])):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    try:
        return [[round(element / div, 2) for element in row] for row in matrix]
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
