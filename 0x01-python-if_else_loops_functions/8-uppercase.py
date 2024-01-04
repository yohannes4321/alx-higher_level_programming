#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= ord('z') and ord(i) >= ord('a'):
            letter = chr(ord(i) - 32)
        else:
            letter = i
        print("{:s}".format(letter), end='')
    print(" ")
