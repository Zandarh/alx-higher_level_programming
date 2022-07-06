#!/usr/bin/python3
"""
    6-load_from_json_file module
"""
import json as js


def load_from_json_file(filename):
    """
        function that creates an Object from a “JSON file”

        Args:
            filename: The name of the file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        answer = js.load(file)
    return answer
