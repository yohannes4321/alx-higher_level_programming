#!/usr/bin/python3
for i in range(0,100):
    last_digit = i % 10
    front_digit = i//10

    if front_digit < last_digit:
        print("{:2}".format(i) ,end=", ")
    elif fornt_digit == last_digit:
        continue
