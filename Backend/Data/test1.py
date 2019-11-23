from sklearn.neighbors.kde import KernelDensity
import numpy as np
from random import random
import matplotlib.pyplot as mp
import train_model

def run_t():
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


def run():
    data = train_model.training_model()

    rand = int(random()*(len(data)-1))
    random_data = [data[rand]]
    print(random_data)

    kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(data)

    return kde.score_samples(random_data)[0]


if __name__ == '__main__':
    run()
