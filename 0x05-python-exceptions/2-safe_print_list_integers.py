#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """

    prints the first x elements of a list and only integers

    Args:
        my_list: The initial list
        x: The number of elements to be printed

    Return:
        X-number of elements.
    """
    res = 0
    for ele in range(0, x):
        try:
            print("{:d}".format(my_list[ele]), end='')
            res += 1

        except (TypeError, ValueError):
            pass
    print()
    return res
