import pandas as pd
import numpy as np
import requests
import math

lambtm = 1.53
lambtv = 2.35
golm = []
golv = []
for i in range(6):
    golm.append(((lambtm**i)*np.exp(-1.0*lambtm))/math.factorial(i))
    golv.append(((lambtv**i)*np.exp(-1.0*lambtv))/math.factorial(i))

a = pd.DataFrame([golm, golm, golm, golm, golm, golm])
b = pd.DataFrame([golv, golv, golv, golv, golv, golv])
c = a.T*b*100
d = c.round(2)
print(golm)
print(golv)
print(d)

import matplotlib.pyplot as plt
import seaborn as sns

corr = d
plt.figure(figsize = (7, 5))
sns.heatmap(corr, linewidths = 0.3,
            cmap = sns.diverging_palette(220, 10, as_cmap=True),
            vmin = 0, vmax = 10, annot = True)
plt.show()

