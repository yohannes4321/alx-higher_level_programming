#!/usr/bin/python3
def number_keys(a_dictionary):
    number = 0
    for key in a_dictionary:
        number += len(key)
    return number
