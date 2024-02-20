#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        for i in range(0, x):
            # Check if the element is an integer before printing
            
            if type(my_list[i])==int:
                print("{:d}".format(my_list[i]),end='')
                num+=1
    except(IndexError,ValueError,TypeError):
        raise IndexError("list index out of range")
    print()
    return num
