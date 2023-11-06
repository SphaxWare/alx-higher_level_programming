#!/usr/bin/python3
import ctypes

# Load the shared library
lib = ctypes.CDLL('./libPyList.so')

# Define the argument types for the function
lib.print_python_list_info.argtypes = [ctypes.py_object]

# Create a Python list
my_list = ['hello', 'world', 42]

# Call the C function to print list information
lib.print_python_list_info(my_list)
