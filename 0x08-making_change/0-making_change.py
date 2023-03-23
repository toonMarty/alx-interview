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

    else:
        ordered_coin = sorted(coins)
        ordered_coin.reverse()
        counter = 0
        for i in ordered_coin:
            while total >= i:
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1
