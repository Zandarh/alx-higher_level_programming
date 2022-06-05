#!/usr/bin/python3
def print_list_integer(my_list=[]):
    i = 0
    my_list_len = len(my_list)
    while i < my_list_len:
        print("{:d}".format(my_list[i]))
        i += 1
