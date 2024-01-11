#!/usr/bin/python3
from functools import reduce

def uniq_add(my_list=[]):
    new_list = reduce(lambda a, b: a + b, set(my_list))
    return new_list

# Example usage
original_list = [1, 2, 3, 1, 2, 4, 5]
result = uniq_add(my_list=original_list)
print(result)

