#!/usr/bin/env python3

import sys

def alphascore(name):
    score = 0
    for c in name:
        score += ord(c) - ord('A') + 1
    return score

names = []
with open('names.txt', 'r') as f:
    for line in f:
        curline = line.split(",")
        for v in curline:
            v = v.strip()
            names.append(v[1:-1])

sortednames = sorted(names)
total = 0
for index, name in enumerate(sortednames):
    total += (index+1)*alphascore(name)
print(total)
