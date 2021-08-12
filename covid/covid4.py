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

covid_e = covid_csv.loc[covid_csv['iso_code'] == 'BRA']
covid_d = covid_e.loc[covid_e['total_cases'] > 20]
y_v = pd.DataFrame(range(len(covid_d['total_cases'])))
x_v = pd.DataFrame(covid_d['total_cases'])


# generate a model of polynomial features

poly = PolynomialFeatures(degree=7, include_bias=False)

# transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
X_ = poly.fit_transform(x_v)
print((x_v))
# criando e treinando o modelo
model = LinearRegression()
model.fit(X_, y_v)

pred = (model.predict(X_))

print(1-model.score(X_, y_v))

print(len(pred))

plt.scatter(x_v, y_v,color='blue')
plt.plot(x_v, pred,color='blue')



#BRASIL

covid_e = covid_csv.loc[covid_csv['iso_code'] == 'BRA']
covid_d = covid_e.loc[covid_e['total_cases'] > 20]
y_v = pd.DataFrame(range(len(covid_d['total_cases'])))
x_v = pd.DataFrame(covid_d['total_cases'])


# generate a model of polynomial features


# transform the x data for proper fitting (for single variable type it returns,[1,x,x**2])
X_ = poly.fit_transform(x_v)

# criando e treinando o modelo


pred = (model.predict(X_))

print(1-model.score(X_, y_v))

print(len(pred))

#plt.scatter(x_v, y_v,color='red')
plt.plot(x_v, pred,color='red')

plt.show()