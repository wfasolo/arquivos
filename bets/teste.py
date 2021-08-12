import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import math
from statistics import mean


key = '&APIkey=6a6e60821e72b841ab0b6ae4f09e9379b3b3a48fb72237a6ee1f2eb51c7924e7'
api = 'https://apiv2.apifootball.com/?action='
acao = 'get_standings&'
liga = 'league_id=68'

url = api+acao+liga+key

r = requests.get(url)
rr = r.json()
tabela = pd.DataFrame(rr).drop(['away_league_W', 'away_league_D', 'away_league_L', 'away_league_position', 'away_promotion', 'home_league_W', 'home_league_D', 'home_league_L', 'home_league_position',
                                'home_promotion', 'country_name', 'league_id', 'league_name', 'overall_league_W', 'overall_league_D', 'overall_league_L', 'team_id', 'league_round', 'team_badge', 'overall_promotion'], axis=1)

tabela.columns = ['NOME', 'POS', 'JOGOS', 'GP', 'GC', 'PTS',
                  'C_J', 'CGP', 'CGC', 'C_PTS', 'F_J', 'FGP', 'FGC', 'F_PTS']

print(tabela)

tj = mean(tabela['JOGOS'].astype(int))*10  # total de jogos
tgc = sum(tabela['CGP'].astype(int))  # total de gol casa
tgf = sum(tabela['CGC'].astype(int))  # total de gol fora

# media de gols campenato
mgc = tgc/tj  # media de gol casa
mgf = tgf/tj  # media de gol fora

time1 = tabela.loc[tabela['NOME'] == 'Sao Paulo']
time2 = tabela.loc[tabela['NOME'] == 'Flamengo RJ']

# media de gols por time

# media de gol pro time mandante
mgptm = time1['CGP'].astype(int)/time1['C_J'].astype(int)
# media de gol contra time mandante
mgctm = time1['CGC'].astype(int)/time1['C_J'].astype(int)

# media de gol pro time visitante
mgptv = time2['FGP'].astype(int)/time2['F_J'].astype(int)
# media de gol contra time visitante
mgctv = time2['FGC'].astype(int)/time2['F_J'].astype(int)

# forca do time mandante
fotm = mgptm/mgc  # forca ofenciva time mandante
fdtm = mgctm/mgf  # forca defenciva casa time 1

# forca do time visitante
fotv = mgptv/mgf  # forca ofenciva time visitante
fdtv = mgctv/mgc  # forca defenciva fora time visitante

# poisson times
lambtm = fotm.values*fdtv.values*mgc  # número provável de gols time mandante
lambtv = fotv.values*fdtm.values*mgf  # número provável de gols time visitante

golm = []
golv = []
for i in range(5):
    golm.append(((lambtm[0]**i)*np.exp(-1.0*lambtm[0]))/math.factorial(i))
    golv.append(((lambtv[0]**i)*np.exp(-1.0*lambtv[0]))/math.factorial(i))

a = pd.DataFrame([golm, golm, golm, golm, golm])
b = pd.DataFrame([golv, golv, golv, golv, golv])
c = a.T*b*100
d = c.round(2)
print(d)

mandante  = (d[0][1]+d[0][2]+d[0][3]+d[0][4]+d[1][2]+d[1][3]+d[1][4]+d[2][3]+d[2][4]+d[3][4])
empate = (d[0][0]+d[1][1]+d[2][2]+d[3][3]+d[4][4])
visitante = (d[1][0]+d[2][0]+d[3][0]+d[4][0]+d[2][1]+d[3][1]+d[4][1]+d[3][2]+d[4][2]+d[4][3])
corrige = mandante+empate+visitante
mandante = (1/(mandante/corrige)).round(2)
empate = (1/(empate/corrige)).round(2)
visitante = (1/(visitante/corrige)).round(2)

print('Resultado Final: ',mandante, empate, visitante)

# under over 1.5
under = (d[0][0]+d[1][0]+d[0][1])
over = 100-under
under = (100/under).round(2)
over = (100/over).round(2)
print('Under/Over: ',over, under)

corr = 100/d
plt.figure(figsize=(7, 5))
sns.heatmap(corr, linewidths=0.2,
            cmap=sns.diverging_palette(220, 10, as_cmap=True),
            vmin=0, vmax=70, annot=True)
plt.show()

"""
acao='get_H2H'
time1='&firstTeam=Internacional'
time2='&secondTeam=Flamengo RJ'

url='https://apiv2.apifootball.com/?action=get_events&from=2020-10-13&to=2020-11-02&timezone=America/Sao_Paulo&league_id=68'+key

r = requests.get(url)

jogos=pd.DataFrame(r.json())

print(pd.DataFrame([jogos['match_round'],jogos['match_date'],jogos['match_time'],jogos['match_hometeam_name'],jogos['match_hometeam_score']
,jogos['match_awayteam_name'],jogos['match_awayteam_score']],index=['RODADA','DATA', 'HORA', 'CASA','GC', 'FORA','GF']).T)

"""
