import leitura
import correcao
import prepro
import KNeighbors
import Florest
import SVC
import graficos

leit = leitura.ler()

corrige = correcao.corrigir(leit)

prepara = prepro.dados(corrige, leit['estacao'])

dados_KN = KNeighbors.valor(prepara)

dados_FL = Florest.valor(prepara)

dados_SVC = SVC.valor(prepara)

graficos.graf(corrige['corrigido'],dados_SVC)
