import pandas as pd
import requests
from bs4 import BeautifulSoup

req = requests.get('https://projects.fivethirtyeight.com/soccer-predictions/brasileirao/')
if req.status_code == 200:
    print('Requisição bem sucedida!')
    content = req.content

soup = BeautifulSoup(content, 'html.parser')
table = soup.find_all(name='table')

table_str = str(table)
df = pd.read_html(table_str)[686]
tabela=pd.DataFrame([df['Team rating']['off.'],df['Team rating']['def.']]).T
time=df['Unnamed: 0_level_0']['team']

times=[]
for i in range(20):
    nome=time[i]
    if nome[0]=='A':
        letra=nome[9]
    else:
        letra=" "
    nomes=[nome[0]+nome[1]+nome[2]+letra]
    times.append(nomes[0])
    
tabelas=pd.DataFrame([pd.Series(times),tabela['off.'],tabela['def.']],index=['time','ofs','def']).T
print(tabelas)