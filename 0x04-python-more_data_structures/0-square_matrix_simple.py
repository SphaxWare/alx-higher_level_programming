#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = []
    for i in matrix:
        array = []
        for j in i:
            array.append(j ** 2)
        newmat.append(array)
    return newmat
