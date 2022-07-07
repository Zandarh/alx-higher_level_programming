#!/usr/bin/python3
"""
    8-class_to_json module
"""
to_json_string = __import__('3-to_json_string').to_json_string


def class_to_json(obj):
    """
        function for JSON serialization of an object

        Args:
            obj: an isntance of a Class

        Return: The dictionary description with simple data structure
    """
    serialized = to_json_string(obj.__dict__)

    return serialized
