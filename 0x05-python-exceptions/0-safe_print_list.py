#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    prints element of a list

    Args:
        my_list: initial list
        x: Number of elements to print

    Return:
        number of elements to print
    """
    ele = 0
    while ele < x:
        try:
            print(my_list[ele], end='')
            ele += 1
        except IndexError:
            break
    print()
    return ele
