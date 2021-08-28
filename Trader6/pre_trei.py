import tabela as tb
import pandas as pd
from tqdm import tqdm

tabelax = tabelay = tab_json = pd.DataFrame()

for ii in tqdm(range(0, 100, 20)):
    tickers = tb.ler_ticker(ii)

    tab_json = pd.concat([tab_json, tb.ler_json(tickers)], ignore_index=True)


for ii in tqdm(range(len(tab_json))):
    dados = tb.criar_tab(tab_json, ii)

    tabtreino = tb.tab_treino(dados, tabelax)
    
tb.salvar_tab(tabtreino)
