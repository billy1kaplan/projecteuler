#!/usr/bin/env python3

import sys

memo = {}

def collatz(n):
    global memo
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    res = 0
    if n % 2 == 0:
        res = 1 + collatz(n//2)
    else:
        res = 1 + collatz(3*n+1)
    memo[n] = res
    return res

def longchain(top):
    curBest = [0, 0]
    for i in range(2, top):
        n = collatz(i)

        if curBest[0] < n:
            curBest[0] = n
            curBest[1] = i
    return curBest

print(longchain(int(sys.argv[1])))
