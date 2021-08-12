import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

corr = np.random.rand(5, 5)
plt.figure(figsize = (7, 5))
sns.heatmap(corr, linewidths = 0.2,
            cmap = sns.diverging_palette(220, 10, as_cmap=True),
            vmin = -1, vmax = 1, annot = True)
plt.show()


