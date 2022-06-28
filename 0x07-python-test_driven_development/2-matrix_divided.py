#!/usr/bin/python3
"""
    The matrix divide module
"""

def matrix_divided(matrix, div):
    """ Divides element of a matrix by a number
        Args: Matrix, and div and the denominator
        Return: Returns a new matrix
    """

    if (not isinstance(matrix, list) or matrix ==[] or not all(isinstance(row, list) for row in matrix) or not all((isinstance(column, int) or isinstance(column, float) for column in [num for row in matrix for num in row]))):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    new_matrix = ([list(map(lambda column: round(column / div, 2), row)) for row in matrix])
    return (new_matrix)
