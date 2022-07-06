#!/usr/bin/python3
"""
    3-to_json_string module
"""
import json as js


def to_json_string(my_obj):
    """
        function that returns the JSON representation of an object (string)
    """
    return js.dumps(my_obj)
