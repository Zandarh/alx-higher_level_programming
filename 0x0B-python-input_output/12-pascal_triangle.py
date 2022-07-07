#!/usr/bin/python3
"""
    12-pascal_triangle module
"""


def pascal_triangle(n):
    """
        Functions that represents the Pascals triangle of n

        Args:
            n: The triangle number

        Return: list of lists of integers
    """
    if n <= 0:
        return []

    new_list = []
    sub_list = []
    for i in range(n):

        if i == 0:
            new_list.append([1])
            sub_list.append(1)
            continue

        check = [0] + sub_list + [0]

        another_sub_list = []
        for i in range(len(check)):
            if i + 1 != len(check):  # prevent checking wrong index
                another_sub_list.append(check[i] + check[i + 1])
        new_list.append(another_sub_list)
        sub_list = another_sub_list

    return new_list
