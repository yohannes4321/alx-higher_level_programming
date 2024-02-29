#!/usr/bin/python3
"""  check to know that the object is instance of the same class"""


def is_same_class(obj, a_class):
    """ return True or False """
    if isinstance(obj, a_class):
        return True
    else:
        return False
