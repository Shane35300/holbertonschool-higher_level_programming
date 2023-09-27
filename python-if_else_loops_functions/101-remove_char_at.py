#!/usr/bin/python3
def remove_char_at(str, n):
    string = str
    if n >= 0:
        string = str[:n] + str[n + 1:]
    return string
