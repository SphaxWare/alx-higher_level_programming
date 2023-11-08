#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for i in set_1:
        if i in set_2:
            set_3.add(i)
    return set_3
