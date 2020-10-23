import pandas as pd
import requests

key='&APIkey=6a6e60821e72b841ab0b6ae4f09e9379b3b3a48fb72237a6ee1f2eb51c7924e7'
api='https://apiv2.apifootball.com/?action='
acao='get_standings&'
liga='league_id=68'

url=api+acao+liga+key

r = requests.get(url)
tabela=pd.DataFrame(r.json()).drop([ 'away_league_W', 'away_league_D','away_league_L','away_league_position',
       'away_promotion', 'home_league_W', 'home_league_D', 'home_league_L','home_league_position',
       'home_promotion','country_name', 'league_id', 'league_name','overall_league_W', 'overall_league_D',
       'overall_league_L', 'team_id', 'league_round', 'team_badge','overall_promotion'], axis=1)

tabela.columns=['NOME', 'POS', 'JOGOS','GP', 'GC', 'PTS','C_J','CGP','CGC', 'C_PTS', 'F_J', 'FGP', 'FGC', 'F_PTS']
print(tabela)

acao='get_H2H'
time1='&firstTeam=Internacional'
time2='&secondTeam=Flamengo RJ'

url='https://apiv2.apifootball.com/?action=get_events&from=2020-10-13&to=2020-11-02&timezone=America/Sao_Paulo&league_id=68'+key

r = requests.get(url)

jogos=pd.DataFrame(r.json())

print(pd.DataFrame([jogos['match_round'],jogos['match_date'],jogos['match_time'],jogos['match_hometeam_name'],jogos['match_hometeam_score']
,jogos['match_awayteam_name'],jogos['match_awayteam_score']],index=['RODADA','DATA', 'HORA', 'CASA','GC', 'FORA','GF']).T)

