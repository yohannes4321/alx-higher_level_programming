#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    n = len(my_list) - 1
    new = my_list.copy()

    if idx < 0:
        return my_list
    if idx > n:
        return my_list

    new[idx] = element
    return new
