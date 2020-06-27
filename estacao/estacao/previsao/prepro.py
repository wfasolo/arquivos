# https://api.thinger.io/v1/users/i9pool/buckets/teste/data?authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxMCIsInVzciI6Imk5cG9vbCJ9.Lnm-rY-sv-rWysHUtLY8AZvm9A3-QYS2p5qa1A8Dh-I
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

est_json=pd.read_json('https://api.thinger.io/v1/users/i9pool/buckets/teste/data?authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxMCIsInVzciI6Imk5cG9vbCJ9.Lnm-rY-sv-rWysHUtLY8AZvm9A3-QYS2p5qa1A8Dh-I')
esp_df=pd.DataFrame(est_json)
esp_val=esp_df.val
print(esp_df)

def dados():

    mu_csv = pd.read_csv('mu.csv', sep=';')

    chuva = pd.DataFrame([mu_csv['TEM_INS'], mu_csv['PRE_INS'],
                          mu_csv['UMD_INS'], mu_csv['PTO_INS'], mu_csv['CHUVA']],index=['temp','press','umid']).T

    chuva = chuva.dropna()
    X = chuva.drop(['CHUVA'], axis=1)
    y = chuva['CHUVA']
    y = y.values
    for i in range(len(y)):
        if y[i] != 0:
            y[i] = 1

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30)

    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    return {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}
