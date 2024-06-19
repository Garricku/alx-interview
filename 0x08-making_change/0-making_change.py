#!/usr/bin/python3


def makeChange(coins, total):
    """Make total with the coins in the fewset coins possible"""
    coins.sort(reverse=True)
    num_coins = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1

    if total == 0:
        return num_coins
    else:
        return -1
