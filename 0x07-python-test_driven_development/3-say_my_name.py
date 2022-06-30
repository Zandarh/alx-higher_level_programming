#!/usr/bin/python3

"""
    Print my name module
"""


def say_my_name(first_name, last_name=""):
    """
        Function prints my namae in first name, last name basis

        Args:
            first_name: The fist name
            last_naame: The last name

        Return: the full name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
