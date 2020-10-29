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
covid_d = covid_e.loc[covid_e['total_cases'] > 50000]

v = {'novos':covid_d['new_cases'],'dias':range(len(covid_d['total_cases']))}

x_v=pd.DataFrame(data=v)
y_v = pd.DataFrame(covid_d['total_cases'])



# generate a model of polynomial features

poly = PolynomialFeatures(degree=4, include_bias=False)

# transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
X_ = poly.fit_transform(x_v)

# criando e treinando o modelo
model = LinearRegression()
model.fit(X_, y_v)
pred = (model.predict(X_))
print(1-model.score(X_, y_v))
test=X_[:1]
resu=pd.Series()
for i in range(len(pred)+15):
    pred2=model.predict(test)
    t=[[(pred2[0]*0.006),i]]
    test=poly.fit_transform(t)
    resu=resu.append(pd.Series(pred2[0]))

    
print (resu)

plt.plot(range(len(resu)),resu)
plt.plot(range(len(pred)),pred)

plt.show()