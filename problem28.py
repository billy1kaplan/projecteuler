#!/usr/bin/env python3

import sys

def getdiag(n):
    total = 1

    for i in range(1, numlayers(n)):
        seed = (2*i + 1)**2
        total += 4*seed - 6*2*i
    return total

def numlayers(n):
    return (n - 1) // 2 + 1

print(getdiag(1001))
