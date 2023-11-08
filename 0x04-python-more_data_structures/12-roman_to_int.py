#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or not isinstance(roman_string, str):
        return 0
    n = 0 
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        current = d[roman_string[i]]
        if  i + 1 < len(roman_string) and d[roman_string[i + 1]] > current:
            n += d[roman_string[i + 1]] - current
            i += 2
        else:
            n += current
            i += 1
    return n
