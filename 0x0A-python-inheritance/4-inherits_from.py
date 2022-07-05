#!/usr/bin/python3
"""
    4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
        Function; checks the di.r or indir. ancestors of a class.

        Args:
            obj: The class checked
            a_class: The referenced class

        Return: True of False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
