# -*- coding: utf-8 -*-
"""
Problem #2
"""

limit = 4000000

n = 1,1

sum = 0
while n[1] < limit:
    if n[1]%2 == 0:
        sum += n[1]
    n = n[1], n[0] + n[1]
    
print(sum)