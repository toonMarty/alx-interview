#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """
    determining the fewest number of coins needed to meet a given amount total
    Args:
        coins: a list of the values of the coins in your possession
        total: total given amount
    Return:
        fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0
    if min(coins) > total:
        return -1
    lst = [-1 for i in range(0, total + 1)]

    for i in coins:
        if i > len(lst) - 1:
            continue
        lst[i] = 1
        for j in range(i + 1, total + 1):
            if lst[j - i] == -1:
                continue
            elif lst[j] == -1:
                lst[j] = lst[j - i] + 1
            else:
                lst[j] = min(lst[j], lst[j - i] + 1)
    return lst[total]
