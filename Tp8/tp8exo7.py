import numpy as np
import matplotlib.pyplot as plt
import sympy as sm

"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")
print("faire juste la fonction qui est fait")

"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")



def f(x):
    return np.log(x) - np.sin(x)

def f2(x):
    return 2*x + 3 - np.exp(x)

def dicho(f, a, b, eps):
    while((b - a) > eps):
        m = (a + b) / 2
        if (f(a)*f(m) < 0):
            b = m
        else:
            a = m
    return m

eps = 10**(-8)
print(eps, pow(10, -8))

print(dicho(f, 1, 3, pow(10, -8)))
print(dicho(f2, 1, 3, pow(10, -8)))

"""
=================================================================
|                           Question 3                          |
=================================================================
"""
print("\n=============\n| Question 3|\n=============\n")
def dicho_nbr(f, a, b, eps):
    i = 0
    while((b - a) > eps):
        m = (a + b) / 2
        if (f(a)*f(m) < 0):
            b = m
        else:
            a = m
        i += 1
    return i

print("nombre iteration", dicho_nbr(f2, 1, 3, pow(10, -8)))