#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lst_1, lst_2 = set_1, set_2
    result = []
    for el_1 in lst_1:
        if el_1 not in lst_2:
            result.append(el_1)
    for el_2 in lst_2:
        if el_2 not in lst_1:
            result.append(el_2)
    return set(result)
