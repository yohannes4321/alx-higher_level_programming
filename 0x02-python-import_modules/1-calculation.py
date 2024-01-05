#!/usr/bin/python3
# 1-calculation.pyI
# Importing Specific Functions from calculator_1 Module
from calculator_1 import add, sub, mul, div

def main():
    a = 10
    b = 5

    # Performing Addition and Printing Result
    result_add = add(a, b)
    print(f"Result of {a} + {b} = {result_add}")

    # Performing Subtraction and Printing Result
    result_sub = sub(a, b)
    print(f"Result of {a} - {b} = {result_sub}")

    # Performing Multiplication and Printing Result
    result_mul = mul(a, b)
    print(f"Result of {a} * {b} = {result_mul}")

    # Performing Division and Printing Result
    result_div = div(a, b)
    print(f"Result of {a} / {b} = {result_div}")

# Ensuring the Script is not Executed when Imported
if __name__ == '__main__':
    # Calling the Main Function
    main()
