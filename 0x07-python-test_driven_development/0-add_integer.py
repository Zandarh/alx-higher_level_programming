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
            if a != a: #checking for NaN numbers
                raise TypeError("a must be an integer")
            else:
                a = int(a) #typcasting float to int
        else:
            raise TypeError("a must be an integer")
    if isinstance(b, int) is False:
        if isinstance(b, float) is True:
            if b != b: #checking for NaN numbers
                raise TypeError("b must be an integer")
            else:
                b = int(b) #typcasting float to int
        else:
            raise TypeError("b must be an integer")
    return (a + b)
