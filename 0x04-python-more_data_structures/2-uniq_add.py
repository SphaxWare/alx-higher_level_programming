#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set()
    n = 0
    for i in my_list:
        if i not in uniq:
            n += i
            uniq.add(i)
    return n
