import scraping as sc
import dados as dd
import random
import pandas as pd
import matplotlib.pyplot as plt


jfla = ['Vas', 'Bra', 'Cor', 'Int', 'São']
jint = ['AtlP', 'Spo', 'Vas', 'Fla', 'Cor']
jatl = ['Goi', 'Flu', 'Bah', 'Spo', 'Pal']
tabPorc = pd.DataFrame()


vf = 0
vi = 0
va = 0
sf = 0
si = 0
sa = 0
tf = 0
ti = 0
ta = 0

tabela = sc.scrap()

for ii in range(1000):
    vitFla = 0
    empFla = 0
    vitInt = 0
    empInt = 0
    vitAtl = 0
    empAtl = 0

    for i in range(len(jfla)):
        result = dd.fim(tabela, 'Fla', jfla[i])
        vitFla = vitFla+result[1]
        empFla = empFla+result[2]

    for i in range(len(jint)):
        result = dd.fim(tabela, 'Int', jint[i])
        vitInt = vitInt+result[1]
        empInt = empInt+result[2]

    for i in range(len(jatl)):
        result = dd.fim(tabela, 'AtlM', jatl[i])
        vitAtl = vitAtl+result[1]
        empAtl = empAtl+result[2]

    ptFla = 61+empFla+3*vitFla
    ptInt = 65+empInt+3*vitInt
    ptAtl = 60+empAtl+3*vitAtl


    if (ptFla > ptInt) and (ptFla > ptAtl):
        vf += 1
    elif  (ptFla > ptInt) and (ptFla < ptAtl) or (ptFla < ptInt) and (ptFla > ptAtl):
        sf += 1
    else:
        tf +=1

    if (ptInt > ptFla) and (ptInt > ptAtl):
        vi += 1
    elif  (ptInt > ptFla) and (ptInt < ptAtl) or (ptInt < ptFla) and (ptInt > ptAtl):
        si += 1
    else:
        ti +=1  

    if (ptAtl > ptFla) and (ptAtl > ptInt):
        vi += 1
    elif  (ptAtl > ptFla) and (ptAtl < ptInt) or (ptAtl < ptFla) and (ptAtl > ptInt):
        si += 1
    else:
        ti +=1        


    porcf = int(100*vf/(vf+vi+va))
    porci = int(100*vi/(vf+vi+va))
    porca = int(100*va/(vf+vi+va))

 

    '''tabPorc = tabPorc.append(
        {'Fla': porcf, 'Int': porci, 'Atl': porca}, ignore_index=True)


plt.plot(tabPorc['Fla'], color='red')
plt.plot(tabPorc['Int'], color='blue')
plt.plot(tabPorc['Atl'], color='black')
plt.show()'''
