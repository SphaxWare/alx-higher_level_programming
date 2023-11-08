#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_elements = set()
    for i in set_1:
        if i not in set_2:
            uniq_elements.add(i)
    for i in set_2:
        if i not in set_1:
            uniq_elements.add(i)
    return uniq_elements
