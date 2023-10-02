#!/usr/bin/python3
def no_c(my_string):
    characters = "cC"
    for x in range(len(characters)):
        my_string = ''.join(x for x in my_string if x not in characters)
    return my_string
