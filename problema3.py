# -*- coding: utf-8 -*-
"""
Problem #3
"""

def prime_factors(n):
    factorized = prime_factorization(n)
    length = len(factorized)
    factors = [k for k in range(2, length + 2) if factorized[k - 2] != 0]
    if factors:
        return factors
    return [n]
    
def prime_factorization(n):
    k = n
    factorized = []
    for t in range(2, int(n ** 0.5 + 1)):
        d = 0
        while k % t == 0:
            k //= t
            d += 1
        factorized.append(d)
    return factorized

N = 11

factors_N = prime_factors(N)

print(factors_N)