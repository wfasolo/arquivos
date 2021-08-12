# https://www.deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/

from sklearn.model_selection import train_test_split


import pandas as pd


import tensorflow as tf

from tensorflow.keras import layers, Sequential
from tensorflow.keras.layers import Dense


prev = []
###
tabelax = pd.read_pickle(
    'Trader/Tabelas/tabelax')
tabelay = pd.read_pickle(
    'Trader/Tabelas/tabelay')
###
#tabelax=pd.DataFrame([tabelax[0]/tabelax[0],tabelax[1]/tabelax[0],tabelax[2]/tabelax[0],tabelax[3]/tabelax[0]]).T
#tabelay=pd.DataFrame([tabelay[0]/tabelay[0],tabelay[1]/tabelay[0],tabelay[2]/tabelay[0],tabelay[3]/tabelay[0]]).T

###
X_train, X_test, y_train, y_test = train_test_split(
    tabelax.values, tabelay.values, test_size=0.35)
###

###
modelo = Sequential()
modelo.add(layers.Flatten())
modelo.add(layers.Dense(256, kernel_initializer="random_uniform",
           bias_initializer="random_uniform"))
modelo.add(Dense(28, activation="relu"))
modelo.add(Dense(64, activation="elu"))
modelo.add(Dense(32, activation="selu"))
modelo.add(Dense(16))
modelo.add(Dense(4))
###

###
callback = tf.keras.callbacks.EarlyStopping(monitor='loss', min_delta=0.01)
opt = tf.keras.optimizers.RMSprop(learning_rate=0.00001)
modelo.compile(loss='MAE', optimizer=opt, metrics=['accuracy'])

hist = modelo.fit(X_train, y_train, batch_size=64, epochs=50,
                  verbose=2, validation_data=(X_test, y_test))

print(hist.history['val_loss'][-1:])

###

# Fazer previsoes
y_pred = modelo.predict(X_test)

t_y_pred = pd.DataFrame(y_pred)
# print(t_y_pred)

t_y_test = pd.DataFrame(y_test)
# print(t_y_test)

# Fazer previsoes
previsao = modelo.predict(tabelax[-2:-1].values)

prev.extend(previsao[0])

print(pd.DataFrame(tabelay[-2:-1].values))
print(prev)
