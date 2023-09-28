#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            func = calc.add
        elif sys.argv[2] == "-":
            func = calc.sub
        elif sys.argv[2] == "*":
            func = calc.mul
        elif sys.argv[2] == "/":
            func = calc.div
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
    print("{} {} {} = {}".format(a, sys.argv[2], b, func(a, b)))
