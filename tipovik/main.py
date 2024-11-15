import numpy as np
from matplotlib import pyplot as plt


for n in range(1, 101, 2):
    plt.scatter(n, np.arctan(np.sqrt(2 + (-1)**n))*n/(2*n+5), color='black')
for n in range(2, 101, 2):
    plt.scatter(n, np.arctan(np.sqrt(2 + (-1)**n))*n/(2*n+5), color='red')

n = 1
print(np.arctan(np.sqrt(2 + (-1)**n)))

plt.show()