#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    divises elements by elements in 2 lists

    Args:
     my_list1: First list
     my_list2: Second list
     list_lenght: list lenght

    Return:
        A new list
    """
    new_list = list()
    for ele in range(list_length):
        try:
            new_list.append(my_list_1[ele] / my_list_2[ele])

        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            print(end="")
    return new_list
