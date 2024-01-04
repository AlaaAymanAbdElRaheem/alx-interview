#!/usr/bin/python3
"""defining pascal_triangle function"""


def pascal_triangle(n):
    """return list of lists of ints representing the Pascal’s triangle of n"""
    result = []
    for i in range(n):
        nested_list = []
        if i == 0:
            result.append([1])
        elif i == 1:
            result.append([1, 1])
        else:
            nested_list.append(1)
            for li in range(len(result[i - 1])):
                try:
                    num = result[i - 1][li] + result[i - 1][li + 1]
                    nested_list.append(num)
                except IndexError:
                    break
            nested_list.append(1)
            result.append(nested_list)

    return result
