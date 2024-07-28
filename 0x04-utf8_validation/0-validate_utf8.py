#!/usr/bin/python3
'''implementing validUTF8 method'''


def validUTF8(data):
    '''validating utf-8 encoding'''
    no_bytes = 0

    for i in data:
        mask_byte = 1 << 7

        if no_bytes == 0:
            while i & mask_byte:
                no_bytes += 1
                mask_byte = mask_byte >> 1

            if no_bytes == 0:
                continue

            if no_bytes == 1 or no_bytes > 4:
                return False

            no_bytes -= 1

        else:
            if not ((i & (1 << 7)) and not (i & (1 << 6))):
                return False

            no_bytes -= 1
    if no_bytes != 0:
        return False

    return True
