#!/usr/bin/python3
"""
    2-append_write module
"""


def append_write(filename="", text=""):
    """
        function that appends a string at the end of a text file (UTF8) 

        Args:
            filename: name of the file
            text: text to e appended to the file

        Return: the number of characters added:
    """
    with open(filename, mode='a', encoding="utf-8") as file:
        update = file.write(text)

    return (update)