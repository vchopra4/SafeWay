from sklearn.neighbors.kde import KernelDensity
import numpy as np
from random import random
import matplotlib.pyplot as mp
X = np.array([[-3, -3], [-2, -2], [-1, -1], [0, 0], [1, 1], [2, 2], [3, 3]])
yep = []
yum = []
xum = []
for i in range(200):
    x = 4*random()-2
    y = 6*random()-3
    xum.append(x)
    yum.append(y)
    yep.append([x, y])

kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(yep)
mp.hist2d(xum, yum)

print(kde.score_samples(X))
mp.show()
