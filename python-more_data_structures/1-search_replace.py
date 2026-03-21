#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = my_list[:]
    for idx, value in enumerate(modified_list):
        if value == search:
            modified_list[idx] = replace
    return modified_list
