import numpy as np
import matplotlib.pyplot as plt
def triangle(x, y, c):
    plt.fill([x, x+c, x+c/2], [y, y, y+c*np.sqrt(3)/2], "b")

triangle(0, 0 , 0.5)
triangle(0.5, 0 , 0.5)
triangle(0.25 , np.sqrt(3)/ 4, 0.5)

plt.show()