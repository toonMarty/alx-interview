#!/usr/bin/python3
"""
This module contains a function minOperations
that calculates the fewest number of operations
needed to result in exactly n H characters
"""


def minOperations(n):
    """
    This function calculates the fewest number
    of operations needed to result in exactly
    n H characters
    Args:
        n (int): the number of characters to be
        eventually in the file
    Return:
         total fewest operations needed to result in
         exactly n H characters
    """
    if n < 2:
        return 0

    lst = []
    k = 1
    while n != 1:
        k += 1
        if n % k == 0:
            while n % k == 0:
                n /= k
                lst.append(k)
    return sum(lst)
