import os
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt


path = Path('CCD4')
names = [i[4:-4] for i in os.listdir(path)]
for i in os.listdir(path):
    data = np.loadtxt(Path(path, i))
    plt.plot(data[:,0], data[:,1])

plt.yscale('log')
plt.legend(names)
plt.show()