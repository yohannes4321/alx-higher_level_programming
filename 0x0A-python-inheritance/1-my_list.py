#!/usr/bin/python3

class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """printing the list accesding the list """
        print(sorted(self))
