#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hide
    for str in dir(hide):
        if "__" not in str:
            print(str)
