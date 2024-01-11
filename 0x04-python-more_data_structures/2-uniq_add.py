#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    new_list = reduce(lambda a, b: a + b, set(my_list))
    return new_list
