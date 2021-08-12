from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'


covid_csv = pd.read_csv(url)
paises_df = pd.DataFrame(covid_csv['iso_code'])
paises = paises_df.drop_duplicates()
paises = paises.dropna()
paises = paises.reset_index()
print(paises['iso_code'][1])

covid_e = covid_csv.loc[covid_csv['iso_code'] == 'BRA']
covid_d = covid_e.loc[covid_e['total_cases'] > 10000]
x_v = pd.DataFrame(range(len(covid_d['total_cases'])))
y_v = pd.DataFrame(covid_d['total_cases'])
yy = pd.DataFrame(((200000000-(covid_d['total_cases']*15))))
test = pd.DataFrame(list(range(320)))

# generate a model of polynomial features
for i in (range(2, 8)):
    poly = PolynomialFeatures(degree=i, include_bias=False)

    # transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
    X_ = poly.fit_transform(x_v)
    XX = poly.fit_transform(test)
    print((x_v))
    # criando e treinando o modelo
    model = LinearRegression()
    model.fit(X_, y_v)

    pred = (model.predict(X_))

    print(1-model.score(X_, y_v))

    pred2 = model.predict(XX)

    pp = pd.DataFrame(pred2)
    print(len(pred))

    plt.xlabel(
        'dias '+str(pp.idxmax().values[0]-len(pred))+' infectados '+str(int(pp.max().values)))
    plt.plot(range(len(pred2)), color='black')
    plt.scatter(x_v, y_v, color='red')

    #plt.plot(x_v, pred)
    plt.plot(range(len(pred2)), pred2, color="blue")

    plt.scatter(pp.idxmax().values, pp.max().values, color='green')
    plt.show()
