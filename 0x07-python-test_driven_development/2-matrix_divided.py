#!/usr/bin/python3
"""
    The matrix divide module
"""


def matrix_divided(matrix, div):
    """ Divides element of a matrix by a number
        Args: Matrix, and div and the denominator
        Return: Returns a new matrix
    """
    prev_len = 0
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(list_error)

    for row in matrix:
        if matrix == []:
            raise TypeError(list_error)

        if type(row) is not list:
            raise TypeError(list_error)

        for column in row: 
            if type(column) is not int and type(column) is not float:
                raise TypeError(list_error)

        if len(row) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(row)

    if type(div) is not int and type(div) is not float:
            raise TypeError("div must be a number")

    if div == float('inf'):
        raise TypeError("div must be a number")        

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    return [[round(column / div, 2) for column in row] for row in matrix]
