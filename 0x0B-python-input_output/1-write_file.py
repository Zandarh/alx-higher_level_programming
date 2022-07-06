#!/usr/bin/python3
"""
    1-write_file module
"""


def write_file(filename="", text=""):
    """
         function that writes a string to a text file (UTF8) and

        Args:
            filename: name of the file
            text: Tex to be written

        Return: returns the number of characters written:
    """
    with open(filename, encoding="utf-8") as file:
        update = file.write(text)
        
    return (update)
