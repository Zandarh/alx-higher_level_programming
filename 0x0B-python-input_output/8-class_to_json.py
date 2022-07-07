#!/usr/bin/python3
"""
    8-class_to_json module
"""


def class_to_json(obj):
    """
        function for JSON serialization of an object

        Args:
            obj: an isntance of a Class

        Return: The dictionary description with simple data structure
    """
    if hasattr(obj, '__dict'):
        return (obj.__dict__.copy())
    return obj.__dict__
