import numpy as np
import matplotlib.pyplot as plt

from sympy import var, sin, cos, pi, pprint, together, apart, simplify, factor, expand, sqrt, Float, evalf, solve, Rational, plot, limit, oo, integrate, diff, log

var('z')

"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

def f(x):
    return 2*x + 3 - np.exp(x)

def f2(x):
    return np.log(x) - np.sin(x)


def df2(x):
    return -np.cos(x) + 1/x
def df(x):
    return 2 - np.exp(x)

def newt(f,Df,x,eps):
    xn = x
    max_iter = 100000
    for n in range(1, max_iter):
        fxn = f(xn)
        if abs(fxn) < eps:
            print('Found solution after', n ,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

print(newt(f, df, 1, 10**-8))

