#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    matrix2 = ([list(map(lambda column: column**2, row)) for row in matrix])
    return (matrix2)
