#!/usr/bin/env python3

from timeit import default_timer as timer
import sys

#recursive
def makechange(n, coins):
    return _makechange(n, len(coins)-1, coins)

def _makechange(n, i, coins):
    if n == 0:
        return 1

    if i < 0 or n < 0:
        return 0

    return _makechange(n-coins[i], i, coins) + _makechange(n, i-1, coins)

#dynamic
def dynochange(n, coins):
    return _dynochange(n, len(coins), coins)

def _dynochange(n, m, coins):
    memo = [[0 for x in range(m)] for x in range(n+1)]

    for i in range(m):
        memo[0][i] = 1

    for i in range(1, n + 1):
        for j in range(m):
            x = memo[i-coins[j]][j] if i-coins[j] >= 0 else 0
            y = memo[i][j-1] if j >= 1 else 0

            memo[i][j] = x + y
    
    return memo[n][m-1]


coins = [1, 2, 5, 10, 20, 50, 100, 200]
start = timer()
makechange(200, coins)
end = timer()
print(end - start)

start = timer()
dynochange(200, coins)
end = timer()
print(end - start)
