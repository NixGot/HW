import os
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt


path = Path('CCD4')
names = [i[4:-4] for i in os.listdir(path)]
averSKO = []
for i in os.listdir(path):
    data = np.loadtxt(Path(path, i))
    plt.plot(data[:,0], data[:,1])
    data = np.loadtxt(Path(path, i), skiprows=14, usecols=1)
    averSKO.append(np.array([np.mean(data), np.std(data), int(i[4:-5])]))


averSKO = np.array(averSKO)
print(averSKO)

plt.yscale('log')
plt.legend(names)
plt.show()

for i in averSKO:
    plt.scatter(i[2], i[0], s=10)
for i in averSKO:
    plt. plot([i[2], i[2]], [i[0] - i[1], i[0] + i[1]], linewidth=1, marker='_', color='black')

print(np.polyfit(averSKO.T[2], averSKO.T[0], 1))

plt.yscale('log')
names.append('СКО')
plt.legend(names)
plt.show()