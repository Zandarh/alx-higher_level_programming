#!/usr/bin/python3
def no_c(my_string):
    i = 0
    a = 'c'
    b = 'C'
    string_as_list = my_string.split()
    list_len = len(string_as_list)
    while i < list_len:
        if my_string[i] == a or my_string[i] == b:
            string_as_listpop(i)
        else:
            i += 1
    new_string = string_as_list.join()
    return (new_string)
