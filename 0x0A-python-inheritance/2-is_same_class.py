#!/usr/bin/python3

"""
    2-is_same_class
"""


def is_same_class(obj, a_class):
    """
        function; returns True if object is  an instance of a class, else False

        Args:
            obj: The object to be checked
            a_class: The specified class

        Return: True of False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
