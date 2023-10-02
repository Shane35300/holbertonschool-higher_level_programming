#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        i = 0
        for elem in line:
            if i == 1:
                print("{}".format(" "), end="")
            print("{}".format(elem), end="")
            i = 1
        print("{}".format("\n"), end="")
