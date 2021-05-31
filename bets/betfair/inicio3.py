# https://docs.developer.betfair.com/display/1smk3cen4v3lu3yomq5qye0ni/Getting+Started#GettingStarted-RequesttheMarketInformationforanEventmarket
# http://www.bespokebots.com/betfair-ssl-certs.php#Linux%20Tutorial

import pandas as pd
import json
import requests


token = '5ut+NfW2OYN3dp2WJ1kjqWYKBxtuzfmj4Hk6t0h8Vh8='
key1 = 'HzbBUzvGG92L0QJ2'
key2 = 'mcpTvHCrfZa1Psf4'


url = "https://api.betfair.com/exchange/betting/json-rpc/v1"
header = {'X-Application': key1, 'X-Authentication': token,
          'content-type': 'application/json'}

jsonrpc_req ='{"jsonrpc": "2.0", "method": "SportsAPING/v1.0/listMarketBook","params": {"marketIds": ["1.176519099"],"priceProjection": {"priceData": ["EX_BEST_OFFERS", "EX_TRADED"],"virtualise": "true"} },"id": 1}'

response = requests.post(url, data=jsonrpc_req, headers=header)


print (json.dumps(json.loads(response.text), indent=3))