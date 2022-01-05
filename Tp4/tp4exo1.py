"""pour importer un exo
j'ai pris des photo """

import matplotlib.pyplot as plt
import numpy as np

def FibIt(n):
    n1 = 0
    n2 = 1
    new  = 0
    i = 0
    if (n > 0):
        while ( i < n):
            new = n1 + n2
            n1 = n2
            n2 = new
            i += 1
    return n1

def renvoiLIst(start, end):
    count = 0
    L = []
    for i in range(start, end + 1):
        L.append(FibIt(i))
    return L


LIstemat = renvoiLIst(5, 25)
print(LIstemat)

plt.plot(LIstemat)
plt.yscale('log')
plt.show()


""" on peut dire que la croissance cette suite devient une droite """