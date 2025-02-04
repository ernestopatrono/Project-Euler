# -*- coding: utf-8 -*-
"""
Problem #4
"""

DIGITS = 7

largest_palindrome = 100 ** (DIGITS-1)

lower_bound = 10 ** (DIGITS-1)

for x in range(10 ** DIGITS - 1, lower_bound - 1, -1):
    for y in range(10 ** DIGITS - 1, x - 1, -1):
        prod = x * y
        if prod <= largest_palindrome:
            break
        if str(prod) == str(prod)[::-1]:
            largest_palindrome = prod
            lower_bound = x
                
print(largest_palindrome)