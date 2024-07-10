#!/usr/bin/env python3


def minOperations(n):
    if n == 0 or n == 1:
        return 0
    
    oper = 2
    h_count = 2
    inc = 1

    while h_count != n:
        if n % h_count == 0:
            oper += 1
            inc = h_count
        oper += 1
        h_count += inc
    return oper
