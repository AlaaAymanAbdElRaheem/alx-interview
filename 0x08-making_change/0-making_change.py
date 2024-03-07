#!/usr/bin/python3
'''Making Change using greedy algorithm'''


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total."""

    if total <= 0 or not coins or len(coins) == 0:
        return 0

    coins.sort(reverse=True)
    num_coins = 0
    sum = 0

    for coin in coins:
        while sum + coin <= total:
            sum += coin
            num_coins += 1

        if sum == total:
            return num_coins
    return -1
