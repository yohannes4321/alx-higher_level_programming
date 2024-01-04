#!/usr/bin/python3
def uppercase(str):
    for i in range(str):
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            letter = chr(ord(i) - 32)
        print("{:s}".format(letter), end="")
