#!/usr/bin/python3
"""Pascal's Triangle module"""

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n

    Takes in an argument n integer
    You can assume n will be always an integer

    Return: an empty list if n <= 0
    """
    triangle = []
    if (n <= 0):
        return triangle
    else:
        for i in range(n):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
