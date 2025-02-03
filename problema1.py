# -*- coding: utf-8 -*-
"""
Problem #1
"""

LIMIT = 1000
FACTORS = 3 , 5

sum = 0

for i in range(LIMIT):
    for factor in FACTORS:
        if i % factor == 0:
            sum += i
            break
        
print(sum)