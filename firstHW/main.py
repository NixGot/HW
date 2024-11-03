import numpy as np
import matplotlib.pyplot as plt
import os

class Func():
    def ReadData(self, rows, path, i):
         return np.loadtxt(path + i, comments="'", delimiter='	', skiprows=rows)

class Graph(Func):
    def __init__(self, data, path):
        self.data = data
        self.path = path
    
    def MakePlot1(self):
            for i in self.data:
                data = self.ReadData(0, self.path, i)
                plt.plot(data[:, 0], data[:, 1]/max(data.T[1]))

    def MakeApprox(self, x0, x1, step, data, dg):
        a = np.polyfit(data[0], data[1], deg=dg)
        plt.plot(np.arange(x0, x1, step), [self.Apr(dg, i, a) for i in np.arange(x0, x1, step)], color='pink')

    @staticmethod
    def MakePlot2(data, x, y):
        for i in data:
            plt.scatter(i[x], i[y])

    @staticmethod
    def MakeLegend(names):
         plt.legend(names)

    @staticmethod
    def MakeLabel(x, y, t):
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(t)

    @staticmethod
    def Apr(dg, x, cof):
        r = 0
        for i in range(0, dg + 1):
            r += x**i*cof[-1-i]
        return r


class NameData(Func):
    def __init__(self, path):
        self.data = list(filter(lambda x: x[-3:] == 'txt', os.listdir(path)))
        self.max_data = []
        self.names = [i[:-4] for i in self.data]
        for i in self.data:
            data = self.ReadData(70, path, i)
            self.max_data.append([data.T[0][np.argmax(data.T[1])], data.T[1][np.argmax(data.T[1])]])
        self.max_data = np.array(self.max_data)

    def Names(self):
         return self.names
    

    def PrintMax(self):
        for i in range(len(self.max_data)):
            print(self.names[i],f' ({self.max_data[i][0]}nm, {self.max_data[i][1]})')

path = 'csv/'
Name = NameData(path)
graph = Graph(Name.data, path)

graph.MakePlot1()
graph.MakeLegend(Name.Names())
graph.MakeLabel('Длина волны нм', 'Относительная интенсивность', 'abs spectra')

Name.PrintMax()

plt.show()
dat_dipol = np.array([2.88, 1.04, 1.69, 1.85, 0.36])
dat_diel = np.array([21, 4.8, 24.55, 80, 2.4])
graph.MakePlot2(np.array([Name.max_data.T[0], dat_dipol]).T, 1, 0)
graph.MakeApprox(0.25, 3, 0.1, [dat_dipol.T, Name.max_data.T[0]], 2)
n = Name.Names()
n.append('аппроксимация')
graph.MakeLegend(n)
graph.MakeLabel('Дипольный момент', 'Положение максимума, нм', 'dipol moment and maximums')
plt.show()

graph.MakePlot2(np.array([Name.max_data.T[0], dat_diel]).T, 1, 0)
graph.MakeApprox(0, 90, 1, [dat_diel.T, Name.max_data.T[0]], 2)
n.append('аппроксимация')
graph.MakeLegend(n)
graph.MakeLabel('Диэлектрическая постоянная', 'Положение максимума, нм', 'diel and maximums')
plt.show()