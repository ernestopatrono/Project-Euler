# -*- coding: utf-8 -*-
"""
Problem #1
"""

limit = 1000

factors = 3 , 5

sum = 0

for n in range(limit):
    for factor in factors:
        if n % factor == 0:
            sum += n
            break
        
print(sum)