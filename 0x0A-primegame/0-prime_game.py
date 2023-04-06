#!/usr/bin/python3
"""
Prime Game implementation
"""


def is_prime(n):
    """
    Checks whether a number is a prime
    number
    Args:
        n: the number to check
    Return:
        True: If number is prime
            else
        False: If number is not prime
    """
    mod_list = []
    if n > 1:
        for i in range(1, n+1):
            mod = n % i
            mod_list.append(mod)

        zero_count = mod_list.count(0)
        if zero_count > 2:
            return False
        else:
            return True


def isWinner(x, nums):
    """
    Finds the winner of the game
    Args:
        x: the number of rounds
        nums: a list of 1 to n inclusive
    Return:
        Winner
    """
    for i in nums:
        # 2 -> [1, 2]
        # 5 -> [1, 2, 3, 4, 5]
        # Each item in nums represents a range of numbers the players
        # will choose from i.e 1 to n inclusive

        round_list = [j for j in range(1, i+1)]
        for j in range(1, x+1):     # Let the games begin round 1 to x
            # j is the round to play.
            for idx, k in enumerate(round_list):
                if is_prime(k):
                    # maria goes first
                    round_list.pop(idx)
                    return 'Maria'
                else:
                    return 'Ben'

    return None
