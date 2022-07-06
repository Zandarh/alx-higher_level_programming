#!/usr/bin/pyhon3
"""
    5-save_to_json_file module
"""
import json as js


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file, using a JSON representation
    
        Args:
            my_obj: Th object
            filename: the text file
    """
    with open(filename, mode='w', encoding='utf=8') as file:
        return js.dumps(my_obj)
