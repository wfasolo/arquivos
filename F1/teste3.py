import random as rd
import pandas as pd
import matplotlib.pyplot as plt
import time

acu = pd.DataFrame()


def pesos(peso1, peso2):
    return [peso1, peso2]


def classificar():
    peso = pesos(50, 50)
    poslarg = rd.choices(population=[1, 2], weights=[peso[0], peso[1]])
    if poslarg[0] == 1:
        p1 = 1
        p2 = 2
    else:
        p1 = 2
        p2 = 1

    return [p1, p2]


def largada():
    cl = classificar()
    peso = pesos(50/cl[0], 50/cl[1])
    larga = rd.choices(population=[1, 2], weights=[peso[0], peso[1]])

    if larga[0] == 1:
        p1 = 1
        p2 = 2
    else:
        p1 = 2
        p2 = 1

    return [p1, p2]


def problema():
    p = rd.choices(population=[1, 2], weights=[0.95, 0.05])
    if p[0] == 1:
        print('sem problemas')
    else:
        qp = rd.choices(population=[1, 2], weights=[0.7, 0.3])
        if qp[0] == 3:
            pu = rd.choices(population=[1, 20])
            print(pu)
        else:
            b = rd.choices(population=[1, 2], weights=[0.8, 0.2])
            if b[0] == 1:
                qb = rd.choices(population=[1, 2])
                print('bateu:', qb)
            else:
                print('quebrou')
           return []




def voltas(nv, tempo1, tempo2):
    ran = rd.random()
    if nv == 1:
        larga = largada()
        peso = pesos(50/larga[0], 50/larga[1])
        volta = rd.choices(population=[1, 2], weights=[peso[0], peso[1]])

        if volta[0] == 1:
            tempo1 = ran
            tempo2 = ran*rd.random()

        else:
            tempo1 = ran*rd.random()
            tempo2 = ran


    else:
        peso = pesos(tempo1, tempo2)
        volta = rd.choices(population=[1, 2], weights=[peso[0], peso[1]])

    if volta[0] == 1:
        tempo1 += ran
        tempo2 += ran*rd.random()
    else:
        tempo1 += ran*rd.random()
        tempo2 += ran

    return [nv, tempo1, tempo2]


volt = voltas(1, 0, 0)

for nv in range(1, 50):
    volt = voltas(nv, volt[1], volt[2])
    acu[nv] = [volt[1], volt[2]]


acu = acu.T
print(acu)

plt.plot(range(len(acu)), acu[0])
plt.plot(range(len(acu)), acu[1])
plt.show()