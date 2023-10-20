#!/usr/bin/python3
"""
12-main
"""


def pascal_triangle(n):
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
