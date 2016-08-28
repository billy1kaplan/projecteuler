#!/usr/bin/env python3

import sys

import math

def factorial(n):
    if n < 2:
        return 1

    f = 1
    for i in range(2, n):
        f *= i

    return f

n = 100
print(sum([int(x) for x in str(factorial(n))]))
print(sum([int(x) for x in str(math.factorial(n))]))
