#!/usr/bin/python3
""" reun using shebang python3"""
"""
to check if hte object is an instace of a class that inheried(direcly or iddiricelty"""

def inherits_from(obj,a_class):
    if isinstance(obj,a_class) and type(obj)!=a_class:
        return True
    else:
        return False
