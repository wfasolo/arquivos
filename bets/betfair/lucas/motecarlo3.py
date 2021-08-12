import random
import pandas as pd
from tqdm import tqdm

prob1=50.3
empate=22.4
prob2=25.6
cs = 0
ep = 0
fr = 0
for iii in tqdm(range(1000)):
    propabilidade = []
    for i in range(3):
        rd = random.randrange(0,100)

        if rd < prob1:
            propabilidade.append('casa')

        elif rd < empate+prob1:
            propabilidade.append('empate')

        else:
            propabilidade.append('fora')

    a = pd.Series(propabilidade)

    if len(a.loc[a == 'casa']) > len(a.loc[a == 'fora']):
        cs += 1
    elif len(a.loc[a == 'casa']) < len(a.loc[a == 'fora']):
        fr += 1
    else:
        ep += 1

fla=round(cs/10,1) 
emp=round(ep/10,1) 
inte=round(fr/10,1)

print(fla,emp,inte)

rd2 = random.randrange(0,100)

if rd2 < fla:
    print('flamengo')

elif rd2 < emp+fla:
    print('empate')

else:
    print('internacional')
