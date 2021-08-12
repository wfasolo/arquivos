import pandas as pd

d=pd.DataFrame([[1.00001,2.090898],[3.877567878,2],[4,3]])
dd=(round(d,3))
print(dd)
print(dd[-1:])