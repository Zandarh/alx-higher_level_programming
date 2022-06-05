#!/usr/bin/python3
def element_at(my_list, idx):
    my_list_len = len(my_list)
    i = 0
    if idx < 0:
        return (None)
    elif idx >= my_list_len:
        return (None)
    else:
        while i < my_list_len:
            if idx == i:
                return (my_list[i])
            i += 1
