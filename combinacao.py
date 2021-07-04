import numpy as np
import pandas as pd

from itertools import combinations
from itertools import permutations
input = [1, 2, 3, 4, 5, 6, 7, 8, 9]

output = sum([list(map(list, permutations(input, i)))
             for i in range(len(input) + 1)], [])

df = pd.DataFrame(output).fillna(0)
print(df)
np.savetxt(r'/home/casa/Documentos/arquivos/jogos/modelos/velhax.txt',
           df, fmt='%d', delimiter='\t')
df.to_csv('/home/casa/Documentos/arquivos/jogos/modelos/velhax.csv', sep='\t')

y = []

for l in range(len(df)):
    c = 8
    while(df[c][l] == 0 and c >= 1):
        c = c-1
    y.append(df[c][l])


np.save(r'/home/casa/Documentos/arquivos/jogos/modelos/y', y)

a = np.load(r'/home/casa/Documentos/arquivos/jogos/modelos/y.npy')
a = list(a)
