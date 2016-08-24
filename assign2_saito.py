from numpy.random import *
import matplotlib.pyplot as plt

R = randn(1000)
plt.hist(R, bins=10)
plt.show()