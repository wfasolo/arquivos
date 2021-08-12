import scraping as sc
import dados as dd
import random
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
import os
os.system('clear')

<<<<<<< HEAD
jfla = ['Int', 'São']
jint = ['Fla', 'Cor']
jsao = ['Grê', 'Pal', 'Bot','Fla']
=======
jfla = ['Cor', 'Int', 'São']
jint = ['Vas', 'Fla', 'Cor']
jatl = ['Bah', 'Spo', 'Pal']
>>>>>>> 8d6c52d103b749ebbc497a3c574a2c5e3815bb3b
tabPorc = pd.DataFrame()
tabPosicao = pd.DataFrame()

vf1 = vi1 = va1 = 0.0001
vf2 = vi2 = va2 = 0.0001
vf3 = vi3 = va3 = 0.0001

tabela = sc.scrap()

print('Calculando probabilidade!')

for ii in tqdm(range(1000)):

    vitFla = 0
    empFla = 0
    vitInt = 0
    empInt = 0
    vitSao = 0
    empSao = 0

    for i in range(len(jfla)):
        result = dd.fim(tabela, 'Fla', jfla[i])
        vitFla = vitFla+result[1]
        empFla = empFla+result[2]

    for i in range(len(jint)):
        result = dd.fim(tabela, 'Int', jint[i])
        vitInt = vitInt+result[1]
        empInt = empInt+result[2]

    for i in range(len(jsao)):
        result = dd.fim(tabela, 'São', jsao[i])
        vitSao = vitSao+result[1]
        empSao = empSao+result[2]

    ptFla = 68+empFla+3*vitFla
<<<<<<< HEAD
    ptInt = 69+empInt+3*vitInt
    ptSao = 59+empSao+3*vitSao

    if (ptFla > ptInt) and (ptFla > ptSao):
=======
    ptInt = 67+empInt+3*vitInt
    ptAtl = 61+empAtl+3*vitAtl

    if (ptFla >= ptInt) and (ptFla >= ptAtl):
>>>>>>> 8d6c52d103b749ebbc497a3c574a2c5e3815bb3b
        vf1 += 1
    elif (ptFla < ptInt) and (ptFla < ptSao):
        vf3 += 1
    else:
        vf2 += 1

    if (ptInt >= ptFla) and (ptInt >= ptSao):
        vi1 += 1
    elif (ptInt < ptFla) and (ptInt < ptSao):
        vi3 += 1
    else:
        vi2 += 1

    if (ptSao > ptFla) and (ptSao > ptInt):
        va1 += 1
    elif (ptSao < ptFla) and (ptSao < ptInt):
        va3 += 1
    else:
        va2 += 1

    porcf1 = int(round(100*vf1/(vf1+vi1+va1), 0))
    porci1 = int(round(100*vi1/(vf1+vi1+va1), 0))
    porca1 = int(round(100*va1/(vf1+vi1+va1), 0))

    porcf2 = int(round(100*vf2/(vf2+vi2+va2), 0))
    porci2 = int(round(100*vi2/(vf2+vi2+va2), 0))
    porca2 = int(round(100*va2/(vf2+vi2+va2), 0))

    porcf3 = int(round(100*vf3/(vf3+vi3+va3), 0))
    porci3 = int(round(100*vi3/(vf3+vi3+va3), 0))
    porca3 = int(round(100*va3/(vf3+vi3+va3), 0))

    tabPorc = tabPorc.append(
        {'Fla': porcf1, 'Int': porci1, 'Sao': porca1}, ignore_index=True)

    tabPosicao = tabPosicao.append({'Fla1': porcf1, 'Fla2': porcf2, 'Fla3': porcf3, 'Int1': porci1,
                                    'Int2': porci2, 'Int3': porci3, 'Sao1': porca1, 'Sao2': porca2, 'Sao3': porca3}, ignore_index=True)


print('Fla: ', porcf1, porcf2, porcf3)
print('Int: ', porci1, porci2, porci3)
print('São: ', porca1, porca2, porca3)

plt.plot([porcf1, porcf2, porcf3], color='red')
plt.plot([porci1, porci2, porci3], color='blue')
plt.plot([porca1, porca2, porca3], color='black')
plt.show()
