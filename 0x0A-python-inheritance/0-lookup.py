#!/usr/bin/python3
"""
    Available atrribut module
"""


def lookup(obj):
    """
        function returning the list of attributes and methods of an object:

        Args:
            obj: A Class

        Return: A list object
    """

    attributes = dir(obj)
    return (attributes)
