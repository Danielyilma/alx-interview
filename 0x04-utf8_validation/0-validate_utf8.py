#!/usr/bin/python3
'''implementing validUTF8 method'''


def validUTF8(data):
    '''validating utf-8 encoding'''
    for num in data:
        if num >> 7 == 1:
            return False

    return True