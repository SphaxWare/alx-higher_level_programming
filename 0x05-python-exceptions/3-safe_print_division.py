#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
    else:
        print("result is", result)
    finally:
        print("Inside result: {}".format(result))
