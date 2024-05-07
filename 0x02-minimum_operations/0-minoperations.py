#!/usr/bin/python3
"""MinOperations module finding the minimum operations"""


def minOperations(n):
    """
    Takes in an integer argument and returns the minimum number of operations of Copy All
    and Paste needed to have n amount of the letter H. If n is impossible to reach then 0
    is returned instead.
    """
    amount_of_h = 1
    operations = 0
    opUsed = 0

    while amount_of_h < n:
        if amount_of_h == n / 2 or amount_of_h == n // 2:
            copy_all = amount_of_h
            paste = amount_of_h + copy_all
            amount_of_h = paste
        else:
            paste = amount_of_h + copy_all
            amount_of_h = paste
        if amount_of_h <= n:
            opUsed += 1
        else:
            return 0

    return operations + opUsed