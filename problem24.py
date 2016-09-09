#!/usr/bin/env python3

import sys

def factorial(n):
    if n < 2:
        return 1

    res = n * factorial(n-1)
    return res

def find_num(d, n):
    digits = [i for i in range(d)]
    cur = n-1
    num = ""
    for i in range(d):
       step = factorial(d-i-1) 

       nextup = cur // step
       num += str(digits[nextup])
       digits.pop(nextup)
       cur = cur % step

    return num
        
print(find_num(10, 1000000))
