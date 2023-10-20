#!/usr/bin/python3
"""
Create a function def pascal_triangle(n):
that returns a list of lists of
integers representing the Pascal’s
triangle of n:
"""


def pascal_triangle(n):
    """
    Return an empty string
    if 0<= 0
    """

    list = []
    for i in range(n):
        list_temp = []
        list_temp.append(1)
        for j in range(1, i):
            if j < i:
                nb = list_prov[j - 1] + list_prov[j]
                list_temp.append(nb)
        if i > 0:
            list_temp.append(1)
        list_prov = list_temp
        list.append(list_temp)
    return list
