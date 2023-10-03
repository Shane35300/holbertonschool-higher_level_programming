#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    temp_list = []
    for i in range(len(my_list)):
        trap = 0
        for j in range(len(temp_list)):
            if my_list[i] == temp_list[j]:
                trap = 1
        temp_list.append(my_list[i])
        if trap == 0:
            result += my_list[i]
    return result
