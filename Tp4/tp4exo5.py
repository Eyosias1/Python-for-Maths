import numpy as np
import matplotlib.pyplot as plt


def cercle():
    t = np.linspace(0, 2*np.pi, 500)
    y = np.sin(t)
    x = np.cos(t)
    plt.plot(x, y)
    plt.fill(x, y)
    plt.axis("equal")
    plt.show()

cercle()


# trois cordonnes suffit de mettre pour afficher un trianle si 4 maybe un carrer
def Triangle():
    plt.plot([0, 1, 0.5], [0, 0, 1])
    plt.fill([0, 1, 0.5], [0, 0, 1])
    plt.axis("equal")
    plt.show()

plt.figure()

Triangle()