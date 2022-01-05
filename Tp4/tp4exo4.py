import numpy as np
import matplotlib.pyplot as plt


def Tangente():
    x = np.linspace(1, 3, 200)
    y = (1 / x)
    plt.plot(x, y)
    y1 = -(1 / 4)*(x - 2) + (1 / 2)
    plt.plot(x, y1)
    plt.axis("equal")
    plt.show()

Tangente()
