import tabela as tb
import teste
import pandas as pd
from tqdm import tqdm

tabelax = tabelay = tab_json = pd.DataFrame()

for ii in tqdm(range(0, 100, 20)):
    tickers = tb.ler_ticker(ii)

    tab_json = pd.concat([tab_json, tb.ler_json(tickers)], ignore_index=True)


for ii in tqdm(range(len(tab_json))):
    dados2 = tb.criar_tab(tab_json, ii)

    dados = teste.converter(dados2)
    tabtreino = tb.tab_treino(dados, tabelax, tabelay)
    tabelax, tabelay = tabtreino[0], tabtreino[1]

tb.salvar_tab(tabtreino[0], tabtreino[1])
