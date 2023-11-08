#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    add = 0
    div = 0
    for i in my_list:
        mul = 1
        for j in i:
            mul *= j
        add += mul
    for i in my_list:
        div += i[1]
    return add/div
