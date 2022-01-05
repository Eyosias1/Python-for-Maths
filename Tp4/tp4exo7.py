import numpy as np
import matplotlib.pyplot as plt


""" Question 1
def affiche(n):
    xo = 0.2
    a = 2.1
    xnext = xo
    if (n > 0):
        for i in range(n + 1):
            xnext = a * xnext * ( 1 - xnext)
    return xnext

print(affiche(201))

L = []

L2 = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]

for i in range(len(L2)):
    L.append(affiche(L2[i]))

print(L)

print("ON remarque que la suite est convergente car elle affiche le meme resultat")


Question 2

def affiche2(n):
    xo = 0.2
    a = 3.1
    xnext = xo
    if (n > 0):
        for i in range(n + 1):
            xnext = a * xnext * ( 1 - xnext)
    return xnext

print(affiche2(201))

L3 = []

L4 = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]

for i in range(len(L4)):
    L3.append(affiche2(L4[i]))

plt.plot(L4, L3)
plt.show()

print("ON remarque que la suite n'est pas convergente")

print(L3)

 Question 3


def affiche3(n):
    xo = 0.2
    a = 3.1
    xnext = xo
    if (n > 0):
        for i in range(n + 1):
            xnext = a * xnext * ( 1 - xnext)
    return xnext

print(affiche3(201))

L5 = []

L6 = [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]

for i in range(len(L6)):
    L5.append(affiche2(L6[i]))


plt.plot(L6, L5, '.', markersize=3)
plt.show()

print("il peut y avoir 10 points")

 Question 4"""




def affiche4(n, a):
    xo = 0.2
    xnext = xo
    if (n > 0):
        for i in range(n):
            xnext = a * xnext * ( 1 - xnext)
    return xnext

def vaire():
    x = np.arange(2.5, 4.01, 0.01)
    L8 = np.arange(200, 301, 1)
    for i in x:
        L7 = []
        for j in range(len(L8)):
            L7.append(affiche4(L8[j], i))
        plt.plot(L8, L7, '.', color = 'r', markersize=3)



vaire()

plt.show()













