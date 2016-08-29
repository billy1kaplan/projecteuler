#!/usr/bin/env python3

import sys

from math import sqrt

MAX_SIZE = 28124

def findAbundant():
    A = set()
    for i in range(12, MAX_SIZE):
        if isAbundant(i):
            A.add(i)

    return A

def countNon():
    A = findAbundant()
    count = 0
    for i in range(1, MAX_SIZE):
        non = True
        for j in A:
            if i - j in A or j * 2 == i:
                non = False
                break

        if non:
            count += i
    return count

def isAbundant(n):
    A = [1]
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            A.append(i)
            A.append(n // i)
    return sum(A) > n

print(countNon())
