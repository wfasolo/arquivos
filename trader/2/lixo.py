import pandas as pd
from sklearn.preprocessing import MinMaxScaler
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
scaler = MinMaxScaler()
scaler.fit(data)
print(scaler.transform(data))
d= pd.concat([pd.DataFrame(data),pd.DataFrame(data)])
print (d)