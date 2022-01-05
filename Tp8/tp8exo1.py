import numpy as np
import matplotlib.pyplot as plt



def sin():
    n = 100
    x = np.linspace(-1, 1, n)
    for i in range(0, 100):
        if (i == 0):
            a = np.array([np.sin(x[0])] )

        a = np.hstack((a, np.sin(x[i])) )
    return a
a = sin()





plt.hist(np.sin(np.arange(0, 10000, 1)), bins=np.linspace(-1, 1, 100), edgecolor='black')
plt.show()

"""
hist des 10000 1er val de la suite, comparer les barres
"""

print("the terms given by sin(x) don't appear to be uniformly spaced within the [-1, 1] interval")