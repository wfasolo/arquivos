import scraping as sc
import dados as dd
import random


jfla = ['Spo', 'Vas', 'Bra', 'Cor', 'Int', 'São']
jint = ['Bra', 'AtlP', 'Spo', 'Vas', 'Fla', 'Cor']

vf=0
vi=0

tabela = sc.scrap()

for ii in range(10000):
    vitFla = 0
    empFla=0
    vitInt = 0
    empInt=0

    for i in range(len(jfla)):
        result = dd.fim(tabela, 'Fla', jfla[i])
        vitFla = vitFla+result[1]
        empFla=empFla+result[2]

        #print('Fla x', jfla[i], ' :', result)

    print(' ')

    for i in range(len(jint)):
        result = dd.fim(tabela, 'Int', jint[i])
        vitInt = vitInt+result[1]
        empInt=empInt+result[2]

        #print('Int x', jint[i], ' :', result)

    ptFla=58+empFla+3*vitFla
    ptInt=62+empInt+3*vitInt
   # print('')
   # print(vitFla, vitInt)
    #print(round((ptFla), 0), round((ptInt), 0))

    if ptFla>ptInt:
        vf+=1
    else:
        vi+=1

    porcf=int(100*vf/(vf+vi))
    porci=int(100-100*vf/(vi))
    print(porcf,porci)


