# Import libraries
import betfairlightweight
from betfairlightweight import filters
import pandas as pd
import numpy as np
import os
import datetime
import json

# Change this certs path to wherever you're storing your certificates
certs_path = r'/home/lab/Documentos/arquivos/bets/betfair/certs'

# Change these login details to your own
my_username = "wfasolo"
my_password = "@Giana0803"
my_app_key = "HzbBUzvGG92L0QJ2"

trading = betfairlightweight.APIClient(username=my_username,
                                       password=my_password,
                                       app_key=my_app_key,
                                       certs=certs_path)

trading.login()
