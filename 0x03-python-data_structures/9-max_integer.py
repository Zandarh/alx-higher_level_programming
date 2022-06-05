#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    i = 0
    if len(my_list) == 0:
        return (None)
    else:
        while i < len(my_list):
            if max < my_list[i]:
                max = my_list[i]
            i += 1
        return (max)
