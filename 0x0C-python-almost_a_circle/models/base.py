#!/usr/bin/python3
"""Creating a class called Base"""


class Base:
    """Creating a public class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        If id is not None, put self.id = id to the value from the user.
        Else equal to Base.__nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
