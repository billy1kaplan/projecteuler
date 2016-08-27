#!/usr/bin/env python3

import sys

def bignums(n):
    A = [1]

    for i in range(n):
        carry = 0
        for j in range(len(A)):
            A[j] = A[j] * 2 + carry

            if A[j] >= 10:
                carry = A[j] // 10
                A[j] = A[j]%10
            else:
                carry = 0

            if j == len(A)-1 and carry > 0:
                A.append(carry)

    print(sum(A))

bignums(1000)
print(sum([int(i) for i in str(2**1000)]))
