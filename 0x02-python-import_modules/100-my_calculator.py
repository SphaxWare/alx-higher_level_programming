#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    args = sys.argv
    if len(args) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(args[1])
    op = str(args[2])
    b = int(args[3])
    if op == "+":
        print("{:d} + {:d} = {:d}".format(a, b, calc.add(a, b)))
        exit(0)
    elif op == "-":
        print("{:d} - {:d} = {:d}".format(a, b, calc.sub(a, b)))
        exit(0)
    elif op == '*':
        print("{:d} * {:d} = {:d}".format(a, b, calc.mul(a, b)))
        exit(0)
    elif op == "/":
        print("{:d} / {:d} = {:d}".format(a, b, calc.div(a, b)))
        exit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        print(op)
        exit(1)
