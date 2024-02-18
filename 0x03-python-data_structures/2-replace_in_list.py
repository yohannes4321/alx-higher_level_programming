#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    n = len(my_list) - 1

    for i in my_list:
        if i == idx:
            my_list[i] = element
            return my_list
        elif idx < 0 or idx > n:
            return my_list
