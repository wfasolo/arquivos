from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import tensorflow as tf

ch = pd.read_csv('chuva.csv')
chu = pd.DataFrame(ch)
chuva = chu.drop(['codigo_estacao', 'data', 'hora', 'temp_max', 'temp_min', 'umid_max', 'umid_min', 'pto_orvalho_max',
                  'pto_orvalho_min', 'pressao_max', 'pressao_min', ' vento_rajada', 'radiacao'
                  ], axis=1)


X = chuva.drop('precipitacao', axis=1).to_numpy()

chuva.loc[(chuva["precipitacao"] != 0), "precipitacao"] = 1

y = chuva['precipitacao'].to_numpy()

MinMaxScaler = MinMaxScaler()
X = MinMaxScaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64, input_dim=6, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=25, batch_size=10, verbose=1)
# model.fit(X_train, y_train, epochs=10)
predictions = model.predict(X_test)
print('First prediction:', predictions[0])

score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
print(predictions)
print(y_test)
