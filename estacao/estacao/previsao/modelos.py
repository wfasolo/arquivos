import matplotlib.pyplot as plt
import prepro
import KNeighbors
import SVC
import Florest

dados = prepro.dados()

dados_mu = KNeighbors.valor(dados['X_train'], dados['X_test'],
                            dados['y_train'], dados['y_test'], dados['atual'])

dados_mu2 = SVC.valor(dados['X_train'], dados['X_test'],
                      dados['y_train'], dados['y_test'], dados['atual'])

dados_mu3 = Florest.valor(dados['X_train'], dados['X_test'],
                          dados['y_train'], dados['y_test'], dados['atual'])

print(dados_mu.idxmax(),  dados_mu.max())
print(dados_mu2.idxmax(), dados_mu2.max())
print(dados_mu3.idxmax(), dados_mu3.max())


plt.plot(range(len(dados_mu)),  dados_mu,label='KN')

plt.plot(range(len(dados_mu2)), dados_mu2, label='SVC')

plt.plot(range(len(dados_mu3)), dados_mu3,label='Flor')
plt.legend()
plt.show()
