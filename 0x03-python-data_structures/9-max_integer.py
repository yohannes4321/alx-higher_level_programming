#!/usr/bin/python3

def max_integer(my_list=[]):
    n = len(my_list)
    max_value = my_list[0]

    if n == 0:
        return None

    for i in my_list:
        max_value = max(max_value, i)

    return max_value
