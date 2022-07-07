#!/usr/bin/python3
"""
    7-add_item Module
"""
from sys import argv
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file =\
        __import__('6-load_from_json_file').load_from_json_file


    filename = 'add_item.json'
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []

    arg_len = len(argv)

    if arg_len > 1:
        for i in range(1, arg_len):
            my_list.append(argv[i])

    save_to_json_file(my_list, filename)
