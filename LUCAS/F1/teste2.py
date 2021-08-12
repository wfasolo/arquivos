import random as rd


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


problema()
