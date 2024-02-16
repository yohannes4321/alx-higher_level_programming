#!/usr/bin/python3
from sys import argv
from hidden_4 import *
if __name__ == "__main__":
    for names in dir(hidden_4):
        if names[0:2] != '__':
            print("{}".format(names))
