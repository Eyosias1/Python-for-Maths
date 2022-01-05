import numpy as np
import matplotlib.pyplot as plt



def MatAl():
    n = 300
    for i in range(n):
        b = np.random.randint(0, i + 1, n)
        if (i == 0):
            A =  b
        else:
            A = np.vstack((A, b))
    plt.matshow(A, cmap='hot')

MatAl()

plt.show()