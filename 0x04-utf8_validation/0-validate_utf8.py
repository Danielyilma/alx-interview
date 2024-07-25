#!/usr/bin/python3
'''implementing validUTF8 method'''


def validUTF8(data):
    '''validating utf-8 encoding'''
    if data is None:
        return False

    for num in data:
        if (num >> 7) != 0:
            return False

    return True
