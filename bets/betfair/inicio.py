# http://www.bespokebots.com/betfair-ssl-certs.php#Linux%20Tutorial

token = '5ut+NfW2OYN3dp2WJ1kjqWYKBxtuzfmj4Hk6t0h8Vh8='
key1 = 'HzbBUzvGG92L0QJ2'
key2 = 'mcpTvHCrfZa1Psf4'


import requests
import json
import pandas as pd
 
url="https://api.betfair.com/exchange/betting/json-rpc/v1"
header = { 'X-Application' : key1, 'X-Authentication' : token ,'content-type' : 'application/json' }
 
jsonrpc_req='{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listEvents", "params": {"filter":{ "eventTypeIds": [1],"competitionIds": ["13"]}}, "id": 1}'
 
response = requests.post(url, data=jsonrpc_req, headers=header)

lista=response.json()
print(lista)
a=(lista["result"])
b=pd.DataFrame(a).drop(['marketCount'],axis=1)
c=(b['event'])
print(c[0]['id'])