#!/usr/bin/python3
import sys

if __name__ == "__main__":
    total = 0
    number = sys.argv

    for i in range(1, len(number)):
        total += int(number[i])
    print("{}".format(total))
