#!/usr/bin/python3
for i in range(0, 100):
    last_digit = i % 10
    front_digit = i//10
    if i==89:
        print("{:2}".format(i))
    if front_digit < last_digit && 1 != 89:
        print("{:2}".format(i), end=", ")
    elif front_digit == last_digit:
        continue

