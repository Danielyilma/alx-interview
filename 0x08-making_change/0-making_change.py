#!/usr/bin/python3
'''make change'''


def makeChange(coins, total):
    '''make change
        return number of coins or -1 if it can't met total
    '''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    numbere_coins = 0

    for coin in coins:
        if total >= coin:
            numbere_coins += total // coin
            total %= coin
        else:
            break

    return numbere_coins if total == 0 else -1
