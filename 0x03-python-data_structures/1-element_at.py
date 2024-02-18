#!/usr/bin/python3

def element_at(my_list, idx):
    n = len(my_list) - 1

    for i in my_list:
        if i == idx:
            return my_list[i]
        elif idx < 0 or idx > n:
            return None
