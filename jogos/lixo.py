import numpy as np
import pandas as pd
a=pd.DataFrame()
for i in range(5):
    a.append([pd.Series(i)])
    
print (a.T)
