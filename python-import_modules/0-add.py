#!/usr/bin/python3
from add_0 import add
a = 1
b = 2
if __name__ == "__main__":
    print("{a} + {b} = {c}".format(a = a, b = b, c = add(a,b)))
