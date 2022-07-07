#!/usr/bin/python3
"""
    100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
        inserts a line of text to a file, after a specified string

        Args:
            filename: The name of the file
            search_string: The string to be appended after
            new_string: The string to append

    """
    with open(filename, mode='r+', encoding='utf-8') as file:
        new_list = []
        for sentence in file:
            new_list.append(sentence)

            # check if the string is a present in the sentence
            if sentence.rfind(search_string) != -1:
                new_list.append(new_string)

        file.seek(0)  # move cusor to the begining
        file.write(''.join(new_list))
