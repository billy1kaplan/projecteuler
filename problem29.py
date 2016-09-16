#!/usr/bin/env python3

import sys

def distinctpow(n):
    nums = set()

    for i in range(2, n + 1):
        cur = i
        for j in range(2, n + 1):
            cur *= i
            if cur not in nums:
                nums.add(cur)

    return len(nums)

print(distinctpow(100))
