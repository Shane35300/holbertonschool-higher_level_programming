#!/usr/bin/python3
"""
That fonction print a square
"size" is the square size
size only have to be an integer
size dont has to be negative
"""


def print_square(size):
    """That fonction print a square
    "size" is the square size
    size only have to be an integer
    """
    if not isinstance(size, int):
        if isinstance(size, float):
            if size < 0:
                raise TypeError("size must be an integer")
            else:
                size = int(size)
        else:
            raise TypeError("size must be an integer")
    else:
        if size < 0:
            raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
