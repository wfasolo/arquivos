import io
import zipfile

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


class LotoFacil:

    def __init__(self):

        self.y_train = []
        self.X_train = []
        self.ultimo = []
        self.previsao1 = []

    def prepara(self):

        url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_lotfac.zip'

        response = requests.get(url, stream=True)
        loto_zip = zipfile.ZipFile(io.BytesIO(response.content))
        loto_html = loto_zip.open('d_lotfac.htm')
        loto_pd = pd.read_html(loto_html)
        loto_list = loto_pd[0]
        loto_list.drop_duplicates(
            subset='Concurso', keep='first', inplace=True)

        lotofacil = pd.DataFrame([loto_list['Bola1'], loto_list['Bola2'], loto_list['Bola3'],
                                  loto_list['Bola4'], loto_list['Bola5'], loto_list['Bola6'],
                                  loto_list['Bola7'], loto_list['Bola8'], loto_list['Bola9'],
                                  loto_list['Bola10'], loto_list['Bola11'], loto_list['Bola12'],
                                  loto_list['Bola13'], loto_list['Bola14'], loto_list['Bola15']]).T
        print(lotofacil)
        (self.X_train, self.y_train) = (
            lotofacil[:-1].values, lotofacil[1:].values)
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
lt = LotoFacil()
lt.prepara()
previsao2 = []
print('Previsão :', set(lt.model()))

for i in range(1, 1750):
    previsao = lt.model(i)
    previsao2.extend(previsao)

    if x == i:

        previsao3 = pd.Series(previsao2)
        print('Prev', x, ':', set(pd.DataFrame(
            previsao3.value_counts()[:15], columns=['Propabilidade']).T))
        x += 250

# bolas = bolas.append(pd.Series(previsao1[0], index=bolas.columns), ignore_index=True)
