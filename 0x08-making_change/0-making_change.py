#!/usr/bin/python3
""" module to get coins count """


def makeChange(coins, total):
    """ calculate the minimum amount of coins needed to make change """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    fewest = 0
    for coin in coins:
        if total <= 0:
            break
        fewest += total // coin
        total %= coin

    if total != 0:
        return -1

    return fewest

