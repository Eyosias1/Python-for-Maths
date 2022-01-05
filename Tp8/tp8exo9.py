import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")
a = 0
b = np.pi / 2

n = 100


x = np.linspace(a , b, n + 1)

fg = [np.sin(x[i]) for i in range(n)]
fr = [np.sin(x[i]) for i in range(1, n + 1)]

def int_rect_g(f, a, b, n):
    h = (b - a) / n
    Sg = h * sum(f)
    print("Sg", Sg)

int_rect_g(fg, a, b, n)

def int_rect_r(f, a, b, n):
    h = (b - a) / n
    Sr = h * sum(f)
    print("Sr", Sr)

int_rect_g(fr, a, b, n)

def int_trap(f, f2, a, b, n):
    h = (b - a) / n
    St = (h * (sum(f) + sum(f2)) ) / 2
    print("St", St)

int_trap(fg, fr, a, b, n)
"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")


def int_rect_g(f, a, b, n):
    h = (b - a) / n
    Sg = h * sum(f)
    return Sg

int_rect_g(fg, a, b, n)

def int_rect_r(f, a, b, n):
    h = (b - a) / n
    Sr = h * sum(f)
    return Sr

int_rect_g(fr, a, b, n)

def int_trap(f, f2, a, b, n):
    h = (b - a) / n
    St = (h * (sum(f) + sum(f2)) ) / 2
    return St

def repet():
    a = - np.pi
    b =   np.pi
    for i in range(1, 8):
        n = 10 ** i
        x = np.linspace(a , b, n + 1)
        fg = [np.exp(np.sin(x[i])) for i in range(n)]
        fr = [np.exp(np.sin(x[i])) for i in range(1, n + 1)]
        Sg = int_rect_g(fg, a, b, n)
        Sr = int_rect_r(fr, a, b, n)
        St = int_trap(fg, fr, a, b, n)
        print("iteration",i ,"Sg", Sg, "Sr", Sr, "St", St)

repet()








