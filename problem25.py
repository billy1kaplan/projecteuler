#!/usr/bin/env python3

import sys

def fib():
    a1, a2, index  = 1, 1, 2

    while len(str(a2)) < 1000:
        a1, a2, index = a2, a1 + a2, index + 1
    return  index
        
print(fib())
