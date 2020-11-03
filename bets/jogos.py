https://rapidapi.com/api-sports/api/api-football/pricing

import requests
import pandas as pd
key = '&APIkey=6a6e60821e72b841ab0b6ae4f09e9379b3b3a48fb72237a6ee1f2eb51c7924e7'
acao = 'get_H2H'
time1 = '&firstTeam=Internacional'
time2 = '&secondTeam=Flamengo RJ'

url = 'https://apiv2.apifootball.com/?action=get_events&from=2020-10-13&to=2020-11-02&timezone=America/Sao_Paulo&league_id=68'+key
         https://apifootball.com/api/?action=get_events&from=2016-10-30&to=2016-11-01&league_id=62&APIkey=xxxxxxxxxxxxxx

r = requests.get(url)

jogos = pd.DataFrame(r.json())

print(pd.DataFrame([jogos['match_round'], jogos['match_date'], jogos['match_time'], jogos['match_hometeam_name'], jogos['match_hometeam_score'],
                    jogos['match_awayteam_name'], jogos['match_awayteam_score']], index=['RODADA', 'DATA', 'HORA', 'CASA', 'GC', 'FORA', 'GF']).T)
