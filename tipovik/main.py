import numpy as np
from matplotlib import pyplot as plt


def find_n0(f, e, a, n=1, step=1):
    while True:
        if abs(f(n) - a)<e:
            return n
        else:
            n += step

def task4_6(f, e, lim, xlim1=1, xlim2=101, ylim1=0, ylim2=0.6):
    plt.figure(figsize=(12, 6))
    y = find_n0(f, e, lim, step=2)
    plt.ylim(ylim1, ylim2)
    plt.scatter([n for n in range(xlim1, y, 2)], [f(n) for n in range(xlim1, y, 2)], color='red', s=8)
    plt.scatter([n for n in range(y, xlim2, 2)], [f(n) for n in range(y, xlim2, 2)], color='green', s=8)
    plt.scatter([n for n in range(xlim1+1, xlim2, 2)], [f(n) for n in range(xlim1+1, xlim2, 2)], color='black', s=8)
    plt.plot([xlim1-1, xlim2+1], [lim, lim], color='pink')
    plt.plot([xlim1-1, xlim2+1], [lim+e, lim+e], color='cyan', alpha=0.3)
    plt.plot([xlim1-1, xlim2+1], [lim-e, lim-e], color='cyan', alpha=0.3)
    plt.show()

def task7_9(f, e, lim, xlim1=2, xlim2=101, ylim1=0, ylim2=0.6):
    plt.figure(figsize=(12, 6))
    y = find_n0(f, e, lim, n=2, step=2)
    plt.ylim(ylim1, ylim2)
    plt.scatter([n for n in range(xlim1, xlim2, 2)], [f(n) for n in range(xlim1, xlim2, 2)], color='black', s=8)
    plt.scatter(y, f(y), color='green', s=8)
    plt.plot([xlim1-1, xlim2+1], [lim, lim], color='pink')
    plt.plot([xlim1-1, xlim2+1], [lim+e, lim+e], color='cyan', alpha=0.3)
    plt.plot([xlim1-1, xlim2+1], [lim-e, lim-e], color='cyan', alpha=0.3)
    print(f'для окрестности {e}, x_n={y}')
    plt.show()


plt.figure(figsize=(12, 6))

f = lambda n: np.arctan(np.sqrt(2 + (-1)**n))*n/(2*n+5)

plt.scatter([n for n in range(1, 101, 2)], [f(n) for n in range(1, 101, 2)], color='red', s=8)
plt.scatter([n for n in range(2, 101, 2)], [f(n) for n in range(2, 101, 2)], color='black', s=8)

plt.plot([0, 100], [np.pi/6, np.pi/6]) #sup
plt.plot([0, 100], [np.pi/28, np.pi/28]) #inf
plt.plot([0, 100], [np.pi/6, np.pi/6]) #uplim
plt.plot([0, 100], [np.pi/8, np.pi/8]) #unlim
plt.show()


task4_6(f, 0.1, np.pi/8)
task4_6(f, 0.05, np.pi/8)
task4_6(f, 0.001, np.pi/8, xlim1=941, xlim2=1020, ylim1=0.390, ylim2=0.395)
task4_6(f, 0.0001, np.pi/8, xlim1=9801, xlim2=9900, ylim1=0.3925, ylim2=0.3929)

task7_9(f, 0.1, np.pi/6)
task7_9(f, 0.05, np.pi/6)
task7_9(f, 0.001, np.pi/6, xlim1=1280, xlim2=1350, ylim1=0.5223, ylim2=0.5250)
task7_9(f, 0.0001, np.pi/6, xlim1=13050, xlim2=13120, ylim1=0.5233, ylim2=0.5238)
