#!/usr/bin/python3
import sys

if __name__ == '__main__':
    HUI = len(sys.argv) - 1

    if HUI == 0:
        print ("0 arguments.")
    else:
        print("{} argument:".format(len(sys.argv) - 1))

    for i in range(1, HUI + 1):
        print("{}: {}".format(i, sys.argv[i]))
