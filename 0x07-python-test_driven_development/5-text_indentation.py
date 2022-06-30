#!/usr/bin/python3

"""
    The inedntation module
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after a ., ?, and :

        Args:
            text: The text to be read

        Return: Returns the new text format
    """

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    index = 0
    while index < len(text) and text[index] == ' ':
        index += 1

    while index < len(text):
        print(text[index], end="")
        if text[index] == "\n" or text[index] in '.?:':
            if text[index] in ".?:":
                print("\n")
            index += 1
            while index < len(text) and text[index] == ' ':
                index += 1
            continue
        index += 1
