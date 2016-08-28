#!/usr/bin/env python3

import sys

def readFile(filename):
    a = []
    with open(filename, 'r') as f:
        for line in f:
            cur = line.strip().split(' ')
            cur = [int(x) for x in cur]
            a.append(cur)
    return a

def bestPathScore(A):
    l = len(A)
    B = [[A[0][0]]]

    for i in range(1, l):
        B.append([0]*(i+1))
        for j in range(i+1):
            if j == 0:
                B[i][j] = B[i-1][0] + A[i][0]
            elif j == i:
                B[i][j] = B[i-1][i-1] + A[i][i]
            else:
                B[i][j] = max(B[i-1][j] + A[i][j], B[i-1][j-1] + A[i][j]) 
    return max(B[l-1])

A = readFile('problem18.txt')
print(bestPathScore(A))
