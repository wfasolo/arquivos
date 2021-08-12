import io
import zipfile

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier


class Mega:

    def __init__(self):

        self.y_train = []
        self.X_train = []
        self.ultimo = []
        self.previsao1 = []

    def prepara(self):

        url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_megase.zip'

        response = requests.get(url, stream=True)
        mega_zip = zipfile.ZipFile(io.BytesIO(response.content))
        mega_html = mega_zip.open('d_mega.htm')
        mega_pd = pd.read_html(mega_html)
        mega_list = mega_pd[0]
        mega_list.drop_duplicates(
            subset='Concurso', keep='first', inplace=True)

        megafacil = pd.DataFrame([mega_list['1ª Dezena'], mega_list['2ª Dezena'], mega_list['3ª Dezena'],
                                  mega_list['4ª Dezena'], mega_list['5ª Dezena'], mega_list['6ª Dezena']]).T

        meg100=megafacil[-50:]
        (self.X_train, self.y_train) = (
            meg100[:-1].values, meg100[1:].values)
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


lt = Mega()
lt.prepara()
prep = lt.prepara()

print('Ultimo :', prep[2])
print('Previsão 1 :', set(lt.model()))
print('Previsão 2 :', set(lt.model(len(prep[0]))))


# bolas = bolas.append(pd.Series(previsao1[0], index=bolas.columns), ignore_index=True)
