#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    length = len(my_list)
    list = []
    for i in range(length):
        if my_list[i] % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
