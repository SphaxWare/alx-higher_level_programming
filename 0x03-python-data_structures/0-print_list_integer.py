#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        num = my_list[i]
        print(f"{num:d}")


my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
