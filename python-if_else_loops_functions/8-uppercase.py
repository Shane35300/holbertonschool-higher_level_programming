#!/usr/bin/python3
def uppercase(str):
    for caract in str:
        if 97 <= ord(caract) <= 122:
            caract = chr(ord(caract) - 32)
        print("{}".format(caract), end="")
    print()
