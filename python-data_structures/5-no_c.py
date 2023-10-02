#!/usr/bin/python3
def no_c(my_string):
    my_string = ''.join(x for x in my_string if x not in "cC")
    return my_string
