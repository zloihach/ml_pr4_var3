import numpy as np
import matplotlib.pyplot as plt


def critic_polyfeet(x, y):
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r")
    plt.show()


