import io
import zipfile

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


class quina:

    def __init__(self):

        self.y_train = []
        self.X_train = []
        self.ultimo = []
        self.previsao1 = []

    def prepara(self):

        url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_quina.zip'

        response = requests.get(url, stream=True)
        quina_zip = zipfile.ZipFile(io.BytesIO(response.content))
        quina_html = quina_zip.open('d_quina.htm')
        quina_pd = pd.read_html(quina_html)
        quina_list = quina_pd[0]
        quina_list.drop_duplicates(
            subset='Concurso', keep='first', inplace=True)

        quinafacil = pd.DataFrame([quina_list['1ª Dezena'], quina_list['2ª Dezena'], quina_list['3ª Dezena'],
                                  quina_list['4ª Dezena'], quina_list['5ª Dezena']]).T

        (self.X_train, self.y_train) = (
            quinafacil[:-1].values, quinafacil[1:].values)
        self.ultimo = self.y_train[-1:]

        return self.X_train, self.y_train, self.ultimo

    def model(self, n_n=1):

        # Tainan model
        model1 = KNeighborsClassifier(n_neighbors=(n_n))
        model1.fit(self.X_train, self.y_train)

        # Fazer previsoes
        previsao = model1.predict(self.ultimo)
        self.previsao1 = previsao[0]
        return self.previsao1


x = 100
lt = quina()
lt.prepara()
previsao2 = []
print('Previsão :', set(lt.model()))

for i in range(1, 1000):
    previsao = lt.model(i)
    previsao2.extend(previsao)

    if x == i:

        previsao3 = pd.Series(previsao2)
        print('Prev', x, ':', set(pd.DataFrame(
            previsao3.value_counts()[:5], columns=['Propabilidade']).T))
        x += 250

# bolas = bolas.append(pd.Series(previsao1[0], index=bolas.columns), ignore_index=True)
