#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for line in matrix:
        copy_line = []
        for elem in line:
            copy_line.append(elem)
        copy.append(copy_line)
    for i in range(len(copy)):
        for j in range(len(copy_line)):
            copy[i][j] *= copy[i][j]
    return copy
