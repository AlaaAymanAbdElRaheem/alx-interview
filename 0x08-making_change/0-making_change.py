#!/usr/bin/python3
'''Making Change'''


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total."""

    if coins is None or total is None or total < 1:
        return 0

    storage = {0: 0}
    for i in range(1, total + 1):
        storage[i] = float('inf')
        for coin in coins:
            if i - coin >= 0:
                storage[i] = min(storage[i], storage[i - coin] + 1)

    return storage[total] if storage[total] != float('inf') else -1
