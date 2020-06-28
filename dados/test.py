from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib as plt
import sklearn
df = pd.read_csv('a.csv')
print(df)

print(df.corr())
df['tipo'] = df['tipo'].map({True: 1, False: 0})
print(len(df.loc[df['tipo'] == 1]))

X = df.drop(columns=('valor'))
X = X.drop(columns=('tipo')).values
y = df['valor'].values
xtreino, ytreino, xteste, yteste = train_test_split(X, y, test_size=.1)
