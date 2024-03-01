#!/usr/bin/python3
"""Peak from a list of unsorted ints"""
def find_peak(list_of_integers):
    newlist = sorted(list_of_integers)
    return (newlist[-1])
