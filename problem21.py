#!/usr/bin/env python3

import sys
from math import sqrt

def sumproper(n):
    if n <= 1:
        return 0

    count = 0

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            other = n // i
            if other != i and other != n:
                count += n // i
            count += i
    return count

def amicablenum(n):
    nums = {}
    for i in range(1, n):
       nums[i] = sumproper(i) 

    total = 0
    for k, v in nums.items():
        if v in nums and v != k:
            if nums[v] == k:
                total += v + k
    return total//2

print(amicablenum(10000))
