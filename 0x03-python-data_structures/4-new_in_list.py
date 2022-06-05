#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_list_len = len(my_list)
    i = 0
    new_list = my_list.copy()
    if idx < 0:
        return (new_list)
    elif idx >= my_list_len:
        return (new_list)
    else:
        while i < my_list_len:
            if idx == i:
                new_list[i] = element
                return (new_list)
            i += 1
