#!/usr/bin/python3
"""creating a class"""


class Square:
    """ intailze the init"""
    def __init__(self,size=0):

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size=size
        """ return the area of the size of square"""
    def area(self):
        return self.__size**2
