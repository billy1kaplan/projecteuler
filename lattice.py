#!/usr/bin/env python3

import sys

def lattice(n):
    n+=1
    A = [[1]*n for i in range(n)]

    for k in range(1, n):
        for i in range(1, k+1):
            A[i][k] = A[i-1][k] + A[i][k-1]
            A[k][i] = A[k-1][i] + A[k][i-1]

    return A[n-1][n-1]

print(lattice(int(sys.argv[1])))
