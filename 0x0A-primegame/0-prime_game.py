#!/usr/bin/python3
'''prime game'''


def memoize(fn):
    '''stores previously calculated value '''
    resultDict = {}

    def wrapper(num):
        if num in resultDict:
            return resultDict[num]

        resultDict[num] = fn(num)
        return resultDict[num]

    return wrapper


@memoize
def primeCount(n):
    '''count the number of prime numbers form 2 - n'''
    count = 0
    for i in range(2, n + 1):
        if isPrime(i):
            count += 1
    return count


@memoize
def isPrime(num):
    '''check if a number is prime or not'''
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2

    return True


def isWinner(x, nums):
    '''the game function that decides who wins the game'''
    benWin = 0
    mariaWin = 0
    for num in nums:
        if primeCount(num) % 2 == 0:
            benWin += 1
        else:
            mariaWin += 1

    if mariaWin < benWin:
        return 'Ben'
    elif mariaWin > benWin:
        return 'Maria'
    return None
