#!/usr/bin/python3
"""
finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        finds a peak in a list of unsorted integers
        Args:
            list_of_integers:
        Return: the peak
    """
    if list_of_integers is None or list_of_integers == []:
        return None

    lower_bound = 0
    upper_bound = len(list_of_integers)
    mid = ((upper_bound - lower_bound) // 2) + lower_bound
    mid = int(mid)

    if upper_bound == 1:
        return list_of_integers[0]

    if upper_bound == 2:
        return mx(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
