import glob
import ReadSHP
import ReadAccident
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import math


def calc_dist_shp(shp, long, lat):
    return shp.binary_search(long, lat)


def dist_t_traffic(long, lat):
    toronto_traffic = pd.read_csv('traffic/traffic-vehicle.csv')

    min_index = 0
    min_dist = math.sqrt(
        math.pow(long - toronto_traffic.loc[0, 'Longitude'], 2) + math.pow(lat - toronto_traffic.loc[0, 'Latitude'], 2))
    for j in range(1, len(toronto_traffic.index.values)):
        dist = math.sqrt(
            math.pow(long - toronto_traffic.loc[j, 'Longitude'], 2) + math.pow(lat - toronto_traffic.loc[j, 'Latitude'],
                                                                               2))
        if dist < min_dist:
            min_dist = dist
            min_index = j

    return toronto_traffic.loc[min_index, '8 Peak Hr Vehicle Volume']


def training_model():
    shp_files = glob.glob('shapefiles/*.shp')

    shp_data_objs = []

    for shp in shp_files:
        shp_obj = ReadSHP.ReadSHPFile(shp, shp)
        shp_data_objs.append(shp_obj)

    accident_files = glob.glob('accident/*.csv')
    a = 0
    for file in accident_files:
        a = ReadAccident.Accident(file)

    want_adjustment = True

    adjustment_traffic = 1 + 0.635

    if not want_adjustment:
        adjustment_traffic = 1

    data = a.data

    # Dict of all the x-values
    X = []

    for i in range(len(data)):
        print(i)
        accident = data[i]
        lat, long = accident.lat, accident.long
        fatal = accident.fatal

        fat_mult = 2
        reg_add = 1

        if fatal:
            reg_add *= fat_mult

        for j in range(reg_add):
            small_x = []
            for shp in range(len(shp_data_objs)):
                dist = calc_dist_shp(shp_data_objs[shp], long, lat)
                small_x.append(dist)

        small_x.append(adjustment_traffic*dist_t_traffic(long, lat))

        X.append(small_x)

    scaler = MinMaxScaler(copy=True, feature_range=(-100, 100))
    scaler.fit(X)
    X = scaler.transform(X)

    return X
