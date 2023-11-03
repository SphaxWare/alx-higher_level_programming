#!/usr/bin/python3
if __name__ == "__main__":
    import sys, calculator_1 as calc
    args = sys.argv
    if len(args) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = args[1]
        op = args[2]
        b = args[3]
        if op == "+":
            print("{:d} + {:d} = {:d}".format(int(a), int(b), calc.add(int(a), int(b))))
            exit(0)
        elif op == "-":
            print("{:d} - {:d} = {:d}".format(int(a), int(b), calc.sub(int(a), int(b))))
            exit(0)
        elif op == "*":
            print("{:d} * {:d} = {:d}".format(int(a), int(b), calc.mul(int(a), int(b))))
            exit(0)
        elif op == "/":
            print("{:d} / {:d} = {:d}".format(int(a), int(b), calc.div(int(a), int(b))))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            print(op)
            exit(1)
