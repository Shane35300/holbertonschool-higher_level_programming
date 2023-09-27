#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nb = len(sys.argv) - 1
    print("{} ".format(nb), end="")
    print("arguments" if nb != 1 else "argument", end="")
    print(":" if nb != 0 else ".")
    for i in range(0, nb):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
