#!/usr/bin/python3
"""

    This is a module for adding two integers.

"""


def add_integer(a, b=98):
    """ A function that adds two integers.
        Args: a: first integer, b: second integer
        Return: Returns the summation of both arguments """

    if isinstance(a, int) is False:
        if isinstance(a, float) is True:
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if isinstance(b, int) is False:
        if isinstance(b, float) is True:
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return (a + b)
