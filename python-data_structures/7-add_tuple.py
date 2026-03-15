#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length = max(len(tuple_a), len(tuple_b))
    result = list()
    for idx in range(length):
        if idx > len(tuple_a) - 1:
            value_a = 0
        else:
            value_a = tuple_a[idx]
        if idx > len(tuple_b) - 1:
            value_b = 0
        else:
            value_b = tuple_b[idx]
        result.append(value_a + value_b)
    return result
