#!/usr/bin/python3
"""Load, add, save module"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])
try:
    obj = load_from_json_file("add_item.json")
except Exception:
    obj = []

obj.extend(args)
save_to_json_file(obj, "add_item.json")
