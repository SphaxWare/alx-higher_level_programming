#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        last = number % 10
    else:
        last = abs(number) % 10
        last = last + last * 10
    return last
t = print_last_digit(-98)
print(t)
