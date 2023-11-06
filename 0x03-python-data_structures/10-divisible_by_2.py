#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in range(0, len(my_list)):
        new.append(True) if my_list[i] % 2 == 0 else new.append(False)
    return new
