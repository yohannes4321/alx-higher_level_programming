#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    n=len(my_list)-1
    if idx < 0:
        return my_list
    elif idx >n:
        return my_list
        
    del my_list[idx]
    return my_list
