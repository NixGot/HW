import os
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt


def Apr(dg, x, cof):
    r = 0
    for i in range(0, dg + 1):
        r += x**i*cof[-1-i]
    return r

def MakeApprox(x0, x1, step, data, dg):
    a = np.polyfit(data[0], data[1], deg=dg)
    plt.plot(np.arange(x0, x1, step), [Apr(dg, i, a) for i in np.arange(x0, x1, step)], color='pink')


print('''
----------------------------------
Задание выполнено для папки CCD4
Группа:
Молодцов Максим
Марасан Маргарита
Фёдоров Евгений
----------------------------------
''')


path = Path('CCD4')
names = [i[4:-4] for i in os.listdir(path)]
averSKO = []
for i in os.listdir(path):
    data = np.loadtxt(Path(path, i))
    plt.plot(data[:,0], data[:,1])
    data = np.loadtxt(Path(path, i), skiprows=14, usecols=1)
    averSKO.append(np.array([np.mean(data), np.std(data), int(i[4:-5])]))

averSKO = np.array(averSKO)
for i, n in enumerate(names):
    # print(n, ':')
    # print(f'    среднее = {averSKO[i][0]}')
    # print(f'    СКО = {averSKO[i][1]}')
    print(f'''
{n}:
    среднее = {averSKO[i][0]}
    СКО = {averSKO[i][1]}''')

plt.yscale('log')
plt.legend(names)
plt.title('График шума при разных температурах')
plt.xlabel('Номер элемента матрицы')
plt.ylabel('Полученное значение')
plt.show()

for i in averSKO:
    plt.scatter(i[2], i[0], s=10)
for i in averSKO:
    plt. plot([i[2], i[2]], [i[0] - i[1], i[0] + i[1]], linewidth=1, marker='_', color='black')

data = np.array([averSKO.T[2], averSKO.T[0]])
MakeApprox(-60, 10, 1, data, 5)
names.append('СКО')
plt.legend(names)
plt.title('Зависимость среднего показания шума от температуры')
plt.xlabel('температура, °C')
plt.ylabel('среднее значение шума')
print('''
--------------------------------------------------------------------------------------
Данные для средних значений взяты с 14 столбца матрицы, тк возможно столбцы до неё
засвечены
Данная функция возможно аппроксимируется гиперболой, но построить её не вышло :( , 
поэтому взят полином, отдалённо напоминащий её. Зависимость точно не экспоненциальная,
т.к. при y - лог. шкала, зависимость не линейная
--------------------------------------------------------------------------------------''')
plt.show()