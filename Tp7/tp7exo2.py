import numpy as np
import matplotlib.pyplot as plt
import sympy as sm



"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")

def serie():
    jeu = 100
    L = np.random.randint(0, 2, jeu)
    k = 0
    c = 0
    for i in range(len(L)):
        if L[i] == 1:
            c += 1
        else:
            c = 0
        if (c == 4):
            k += 1
    return k / jeu

print(serie())
L = [0 for i in range(5)]
print(L)
"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")

def serie2(n):
    jeu = 100
    L = np.random.randint(0, 2, jeu)
    k = 0
    c = 0
    for i in range(len(L)):
        if L[i] == 1:
            c += 1
        else:
            c = 0
        if (c == n):
            k += 1
    return k / jeu


def hto():
    L = [serie2(i) for i in range(3, 8)]
    largeur = 0.35
    index = np.arange(3, 8)
    plt.bar(index, L, largeur, color='b', label='Maths')
    plt.show()


hto()




