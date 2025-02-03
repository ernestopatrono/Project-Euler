# -*- coding: utf-8 -*-
"""
Problem #2
"""

LIMIT = 4000000

m, n = 1, 1
sum = 0

while n < LIMIT:
    if n % 2 == 0:
        sum += n
    m, n = n, m + n

print(sum)
