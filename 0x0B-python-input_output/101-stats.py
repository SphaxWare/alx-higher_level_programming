#!/usr/bin/python3
"""stats module"""
from sys import stdin


total_size = i = 0
status_counts = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }


def showstats():
    """this func print stats"""
    print(f'File size: {total_size}')
    for k, v in sorted(status_counts.items()):
        if v > 0:
            print('{:s}: {:d}'.format(k, v))


try:
    for l in stdin:
        splitline = l.split()
        if len(splitline) >= 2:
            status = splitline[-2]
            total_size += int(splitline[-1])
            if status in status_counts:
                status_counts[status] += 1
        i += 1

        if i % 10 == 0:
            showstats()
    showstats()
except KeyboardInterrupt as e:
    showstats()
