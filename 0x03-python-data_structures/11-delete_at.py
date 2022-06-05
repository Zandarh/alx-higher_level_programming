#!/usr/bin/pthon3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        i = 0
        while i < len(my_list):
            if idx == i:
                my_list.remove(my_list[i])
            i += 1
        return my_list
