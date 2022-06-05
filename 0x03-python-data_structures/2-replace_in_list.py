#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    my_list_len = len(my_list)
    if idx < 0:
        return (my_list)
    elif idx >= my_list_len:
        return (my_list)
    else:
        while i < my_list_len:
            if idx == i:
                my_list[i] = element
                return (my_list)
            i += 1
