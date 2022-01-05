import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


"""
=================================================================
|                           Question  1                         |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

def serie(n):
    v = np.random.randint(1, 7, n)
    return v

print(serie(10))

"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")

def checkN(L, n):
    for i in range(len(L)):
        if (L[i] == n):
            return 1
    return 0

def P4():
    n = 0
    nfoi = 10
    for i in range(nfoi):
        L = serie(4)
        n += checkN(L, 6)
    return n / nfoi

print(P4())


"""
=================================================================
|                           Question 2(b)                       |
=================================================================
"""
print("\n=============\n|Question 2a|\n=============\n")

def checkN2(L, L2, n):
    for i in range(len(L)):
        if ((L[i] == L2[i])):
            if (L[i] == 6):
                return 1
    return 0

def P24():
    n = 0
    nfoi = 100000
    for i in range(nfoi):
        L = serie(24)
        L2 = serie(24)
        n += checkN2(L, L2, 6)
    return n / nfoi


print(P24())










