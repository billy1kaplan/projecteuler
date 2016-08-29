#!/usr/bin/env python3

import sys

d = {}
d[0] = 'zero'
d[1] = 'one'
d[2] = 'two'
d[3] = 'three'
d[4] = 'four'
d[5] = 'five'
d[6] = 'six'
d[7] = 'seven'
d[8] = 'eight'
d[9] = 'nine'
d[10] = 'ten'
d[11] = 'eleven'
d[12] = 'twelve'
d[13] = 'thirteen'
d[14] = 'fourteen'
d[15] = 'fifteen'
d[16] = 'sixteen'
d[17] = 'seventeen'
d[18] = 'eighteen'
d[19] = 'nineteen'
d[20] = 'twenty'
d[30] = 'thirty'
d[40] = 'forty'
d[50] = 'fifty'
d[60] = 'sixty'
d[70] = 'seventy'
d[80] = 'eighty'
d[90] = 'ninety'
d[100] = 'hundred'
d[1000] = 'thousand'
for k in d:
    d[k] = len(d[k])

def countLetters(n):
    n += 1
    count = 0

    for i in range(1, n):
         prev = count
         if i < 100:
             count += u100(i)
         elif i >= 100 and i < 1000:
             count += o100(i)
         else:
             count += len('thousand') + d[1]
    return count

def u100(n):
    if n <= 20:
        return d[n]

    res = ones(n%10)
    if n < 30:
        res += d[20]
    elif n < 40:
        res += d[30]
    elif n < 50:
        res += d[40]
    elif n < 60:
        res += d[50]
    elif n < 70:
        res += d[60]
    elif n < 80:
        res += d[70]
    elif n < 90:
        res += d[80]
    elif n < 100:
        res += d[90]
    return res

def o100(n):
    assert (n >= 100 and n < 1000)
    x = n // 100
    res = d[x] + d[100]
    if n % 100 != 0:
        res += u100(n%100) + 3
    return res

def ones(n):
    if n != 0:
        return d[n]
    return 0

print(countLetters(1000))
