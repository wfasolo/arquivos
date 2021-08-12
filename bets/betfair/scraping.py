import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap():
    req = requests.get('https://projects.fivethirtyeight.com/soccer-predictions/brasileirao/')
    if req.status_code == 200:
        print('Baixando dados da Tabela!')
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all(name='table')

    table_str = str(table)
    '''for l in range(10):
        print(pd.read_html(table_str)[l])'''
        
    df = pd.read_html(table_str)[len(pd.read_html(table_str))-1]
    tabela=pd.DataFrame([df['Team rating']['off.'],df['Team rating']['def.']]).T
    time=df['Unnamed: 0_level_0']['team']

    times=[]
    for i in range(20):
        nome=time[i]
        if nome[0]=='A':
            letra=nome[9]
        else:
            letra=""
        nomes=[nome[0]+nome[1]+nome[2]+letra]
        times.append(nomes[0])
    pts=[62,58,57,58,52,51,50,45,45,44,45,42,42,35,35,36,35,29,27,23]   
    tabelas=pd.DataFrame([pd.Series(times),tabela['off.'],tabela['def.'],pd.Series(pts)],index=['time','ofs','def','pts']).T
    

    return tabelas