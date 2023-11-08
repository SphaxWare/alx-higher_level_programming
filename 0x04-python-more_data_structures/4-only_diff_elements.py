#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    uniq_elements = set()
    for i in set_1:
        if i not in set_2:
            uniq_elements.add(j)
    for i in set_2:
        if i not in set_1:
            uniq_elements.add(j)
    return uniq_elements
