#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in matrix:
        new = [x ** 2 for x in i]
        new_matrix.append(new)

    return new_matrix
