import numpy as np
import matplotlib.pyplot as plt


def figure1():
    x = np.linspace(-10, 10, 500)
    y = (np.sin(x) / x)
    plt.plot(x, y)
    plt.show()

def figure2():
    x = np.linspace(0, 20, 500)
    y = np.sin(x**2)
    plt.plot(x,y)
    plt.show()

figure1()
plt.figure()
figure2()
