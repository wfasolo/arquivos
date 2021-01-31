import scraping as sc
import dados as dd
import random


jfla = ['Spo', 'Vas', 'Bra', 'Cor', 'Int', 'São']
jint = ['Bra', 'AtlP', 'Spo', 'Vas', 'Fla', 'Cor']
vitFla = 0
vitInt = 0

tabela = sc.scrap()

for i in range(len(jfla)):
    result = dd.fim(tabela, 'Fla', jfla[i])
    vitFla = vitFla+result[1]

    print('Fla x', jfla[i], ' :', result)

print(' ')

for i in range(len(jint)):
    result = dd.fim(tabela, 'Int', jint[i])
    vitInt = vitInt+result[1]

    print('Int x', jint[i], ' :', result)

print('')
print(vitFla, vitInt)
print(round((58+18*vitFla/600), 0), round((62+18*vitInt/600), 0))

t1 = tabela.loc[tabela['time'] == 'Fla']
t2 = tabela.loc[tabela['time'] == jfla[i]]

aleotorio = random.randrange(1, 3)


if aleotorio == 1:
    t1['pts'] = t1['pts'].values[0]+3
    result[1] = result[1]-1
elif aleotorio == 2:
    t1['pts'] = t1['pts'].values[0]+1
    t2['pts'] = t2['pts'].values[0]+1
    result[2] = result[2]-1
else:
    t2['pts'] = t2['pts'].values[0]+3
    result[3] = result[3]-1

print(t1['pts'])
