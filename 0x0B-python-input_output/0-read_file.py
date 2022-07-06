#!/usr/bin/python3
"""
    0-read_file module
"""


def read_file(filename=""):
    """
        function that reads a text file (UTF8) and prints it to stdout

        Args:
            filname: name of the file to be read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
