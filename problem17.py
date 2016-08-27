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
             count += len('thousand') + len(d[1])
    return count

def u100(n):
    if n <= 20:
        return len(d[n])
    elif n > 20 and n < 30:
        return len(d[20]) + ones(n % 10)
    elif n >= 30 and n < 40:
        return len(d[30]) + ones(n % 10)
    elif n >= 40 and n < 50:
        return len(d[40]) + ones(n % 10)
    elif n >= 50 and n < 60:
        return len(d[50]) + ones(n % 10)
    elif n >= 60 and n < 70:
        return len(d[60]) + ones(n % 10)
    elif n >= 70 and n < 80:
        return len(d[70]) + ones(n % 10)
    elif n >= 80 and n < 90:
        return len(d[80]) + ones(n % 10)
    elif n >= 90 and n < 100:
        return len(d[90]) + ones(n % 10)

def o100(n):
    x = n // 100
    if n % 100 == 0:
        return len(d[x]) + len(d[100])

    if n >= 100 and n < 1000:
        return len(d[x]) + len(d[100]) + u100(n % 100) + 3

def ones(n):
    if not n == 0:
        return len(d[n])
    return 0

print(countLetters(1000))
