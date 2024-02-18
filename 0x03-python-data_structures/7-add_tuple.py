#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    n = len(tuple_a)
    m = len(tuple_b)

    sum_tuple = (
        (tuple_a[0] if n >= 1 else 0) + (tuple_b[0] if m >= 1 else 0),
        (tuple_a[1] if n >= 2 else 0) + (tuple_b[1] if m >= 2 else 0)
    )

    return sum_tuple
