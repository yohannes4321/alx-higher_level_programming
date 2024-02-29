#!/usr/bin/python3

class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """printing the list accesding the list """
        sort_list = sorted(self)
        print(sort_list)
