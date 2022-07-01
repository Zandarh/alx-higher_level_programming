#!/usr/bin/python3
"""
    The two matrix mul module

"""


def matrix_mul(m_a, m_b):
    """
        This function multiplies two matrixes to groduce one

        Args:
            Matrix a: first matrix
            Matrix b: 2nd matrix

        Return: Returns the new matrix
    """
    ma_len = 0
    mb_len = 0
    m_aError = "m_a should contain only integers or floats"
    m_bError = "m_b should contain only integers or floats"

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for ma_row in m_a:
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")

        for ma_column in ma_row:

            if not isinstance(ma_column, int):

                if not isinstance(ma_column, float):
                    raise TypeError(m_aError)

            if len(ma_row) != ma_len and ma_len != 0:
                raise TypeError("each row of m_a must be of the same size")
            ma_len = len(ma_row)

    for mb_row in m_b:
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")

        for mb_column in mb_row:
            if not isinstance(mb_column, int):

                if not isinstance(mb_column, float):
                    raise TypeError(m_bError)

            if len(mb_row) != mb_len and mb_len != 0:
                raise TypeError("each row of m_a must be of the same size")
            mb_len = len(mb_row)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = list()    # multiplication starts
    for row_a in range(len(m_a)):
        flag = 0
        inner_list = list()
        for row_b in range(len(m_b)):
            for col in range(len(m_b[row_b])):
                if flag == 0:
                    inner_list.append(m_a[row_a][row_b] * m_b[row_b][col])
                else:
                    inner_list[col] += (m_a[row_a][row_b] * m_b[row_b][col])
            flag = 1
        new_matrix.append(inner_list)  # multiplied matrix(2D List)

    return new_matrix
