#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argstr = "argument"
    argnum = len(argv) - 1

    if argnum == 0:
        argstr += 's.'
    elif argnum == 1:
        argstr += ':'
    else:
        argstr += 's:'

    print("{} {}".format(argnum, argstr))

    i = 0
    for arg in argv[1:]:
        i += 1
        print("{:d}: {:s}".format(i, arg))
