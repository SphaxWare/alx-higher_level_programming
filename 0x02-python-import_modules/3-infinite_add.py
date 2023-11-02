#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(0)
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
    print(result)
