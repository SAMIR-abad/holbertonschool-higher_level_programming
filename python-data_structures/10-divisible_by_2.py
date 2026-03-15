#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_divisible_list = list()
    for num in my_list:
        if num % 2 == 0:
            is_divisible_list.append(True)
        else:
            is_divisible_list.append(False)
    return is_divisible_list
