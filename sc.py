import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap():
    req = requests.get('https://www.365scores.com/pt-br/football/germany/bundesliga/match/arminia-bielefeld-wolfsburg/339-345-25')
    if req.status_code == 200:
        print('Baixando dados da Tabela!')
        content = req.content

    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find_all('div',class='standings-widget-content-table-container')

    table_str = str(table)
    print(table_str)

scrap()