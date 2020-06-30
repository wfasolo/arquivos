import numpy as np
import matplotlib.pyplot as plt
import leitura
import correcao
import prepro
import KNeighbors
import SVC
import Florest

ler = leitura.ler()

corrige = correcao.corrigir(ler)

dados = prepro.dados(corrige,ler['estacao'])

dados_mu = KNeighbors.valor(dados['X_train'],
                            dados['X_test'],
                            dados['y_train'],
                            dados['y_test'],
                            dados['previsao'])

dados_mu2 = SVC.valor(dados['X_train'],
                      dados['X_test'],
                      dados['y_train'],
                      dados['y_test'],
                      dados['previsao'])

dados_mu3 = Florest.valor(dados['X_train'],
                          dados['X_test'],
                          dados['y_train'],
                          dados['y_test'],
                          dados['previsao'])


#print(dados_mu.idxmax(),  dados_mu.max())
#print(dados_mu2.idxmax(), dados_mu2.max())
#print(dados_mu3.idxmax(), dados_mu3.max())
