import ReadAccident
import glob
import pandas as pd
import math
import numpy as np
import statsmodels.api as sm


def relationship_road_traffic_accidents():
    accidents = glob.glob('accident/*.csv')

    acc = 0
    for a in accidents:
        acc = ReadAccident.Accident(a)

    toronto_traffic = pd.read_csv('traffic/traffic-vehicle.csv')

    # Relationship between peak vehicle volume and # of accidents at that intersection

    data = acc.data

    intersec_id = {}

    print('Running')

    for i in range(len(data)):
        print(i)
        long = data[i].long
        lat = data[i].lat
        fatal = data[i].fatal

        min_index = 0
        min_dist = math.sqrt(math.pow(long - toronto_traffic.loc[0, 'Longitude'], 2) + math.pow(lat - toronto_traffic.loc[0, 'Latitude'], 2))
        for j in range(1, len(toronto_traffic.index.values)):
            dist = math.sqrt(math.pow(long - toronto_traffic.loc[j, 'Longitude'], 2) + math.pow(lat - toronto_traffic.loc[j, 'Latitude'], 2))
            if dist < min_dist:
                min_dist = dist
                min_index = j

        if min_index not in intersec_id:
            intersec_id[min_index] = 1
        else:
            intersec_id[min_index] += 1

    xs = []
    ys = []
    for j in intersec_id:
        xs.append(toronto_traffic.loc[j, '8 Peak Hr Vehicle Volume'])
        ys.append(intersec_id[j])

    print(xs)
    xs = np.array(xs)
    ys = np.array(ys)

    # xs = sm.add_constant(xs)

    model = sm.OLS(ys, xs).fit()

    print(model.summary())
    print(model.params)


relationship_road_traffic_accidents()
