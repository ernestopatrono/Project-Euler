# -*- coding: utf-8 -*-
"""
Problem #5
"""
REF = 20

#number to check

def factorize(n):
    lista=[]
    m=n
    x=2
    while m!=1:
        if m%x!=0:
            x+=1
        else:
            m//=x
            lista.append(x)
    return lista

def lcm(a,b):
    factors_a = factorize(a)
    factors_b = factorize(b)
    for f in factors_a:
        if f in factors_b:
            factors_b.remove(f)
    factors = factors_a+factors_b
    total = 1
    for f in factors:
        total *= f
    return total

multiple = 2
for n in range(2,REF+1):
    multiple = lcm(multiple,n)
    
print(multiple)