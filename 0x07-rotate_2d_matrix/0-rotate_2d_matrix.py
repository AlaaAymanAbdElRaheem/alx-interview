#!/usr/bin/python3
"""in place rotation of a 2D matrix
by 90 degrees clockwise"""


def rotate_2d_matrix(matrix) -> None:
    """rotate a 2D matrix by 90 degrees clockwise"""
    for i in range(len(matrix)):
        for j in range((i + 1), len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(len(matrix)):
        matrix[i].reverse()
