#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = matrix[:]
    squared_matrix = []
    for line in copy_matrix:
        squared_line = list(map(lambda x: x**2, line))
        squared_matrix.append(squared_line)
    return squared_matrix
