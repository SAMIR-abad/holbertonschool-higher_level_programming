#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    length = max(len(tuple_a), len(tuple_b))
    result = list()
    for i in range(length):
        val_a = tuple_a[i] if i < len(tuple_a) else 0
        val_b = tuple_b[i] if i < len(tuple_b) else 0
        result.append(val_a + val_b)

    return tuple(result)
