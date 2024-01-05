#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    # Initializing Variables
    a = 10
    b = 5

    # Performing Addition
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Performing Subtraction
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Performing Multiplication
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Performing Division
    print("{} / {} = {}".format(a, b, div(a, b)))
