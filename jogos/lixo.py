import numpy as np
import pandas as pd

matriz = np.array([[1, 41, 71],
                   [2, 51, 81],
                   [3, 61, 91]]).astype(np.float32)



matriz[1, 1]=777.4
print(matriz)
