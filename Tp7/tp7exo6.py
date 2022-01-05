import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


"""
=================================================================
|                           Question 1                          |
=================================================================
"""
print("\n=============\n| Question 1|\n=============\n")


def un_pas():
    r = np.random.rand()
    if r >= 3 / 4:
        return np.array([1, 0])
    elif r >= 2 / 4:
        return np.array([0, 1])
    elif r >= 1 / 4:
        return np.array([-1, 0])
    else:
        return np.array([0, -1])

"""
=================================================================
|                           Question 2                          |
=================================================================
"""
print("\n=============\n| Question 2|\n=============\n")

def marche2d(n):
    Xn = np.zeros(2, dtype=int)
    x = [0]
    y = [0]
    for i in range(n):
        Xn = Xn + un_pas()
        x.append(Xn[0])
        y.append(Xn[1])
    print(x, y)
    plt.plot(x, y)
    #plt.axis('equal')
    plt.show()

marche2d(100)