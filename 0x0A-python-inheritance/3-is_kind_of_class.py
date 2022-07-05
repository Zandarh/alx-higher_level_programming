#!/usr/bin/python3
"""
    3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
        Function that checks if a class is a subclass of another

        Args:
            obj: The class checked
            a_class: The referenced class

        Return: True of False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
