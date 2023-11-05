#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(i) == 0:
            print()
        for j in i:
            if j == i[(len(i) - 1)]:
                print("{:d}".format(j))
            else:
                print("{:d}".format(j), end=' ')
