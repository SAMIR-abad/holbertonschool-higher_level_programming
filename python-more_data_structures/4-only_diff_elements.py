#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    lst_1, lst_2 = set_1, set_2
    result = []
    for el_1 in lst_1:
        if not el_1 in lst_2:
            result.append(el_1)
    return set(result)
