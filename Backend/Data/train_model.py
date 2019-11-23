import glob
import ReadSHP
import ReadAccident


# Using proximities to the variables that are normalized (at least that is what you should use)
def gather_all_shape_file_data():
    0


# Normalize the traffic data
def traffic_data_toronto():
    0


# For each data point, get the distance to each variable (normalized), and the traffic (closest traffic, normalized)
# Pass this to the KDE, and let it run.
# Save model.
# Run model using London data, which will be in production
def training_model():
    shp_files = glob.glob('shapefiles/*.shp')
    geo_json_files = glob.glob('geojson/*.extension')

    shp_data = []
    for s in shp_files:
        shp_data.append(ReadSHP.ReadSHPFile(s, s))

    accident_files = glob.glob('accident/*.csv')
    a = 0
    for file in accident_files:
        a = ReadAccident.Accident(file)

    want_adjustment = True

    adjustment_traffic = 1 + 0.635

    if not want_adjustment:
        adjustment_traffic = 1

    data = a.data

    for i in range(len(data)):
        accident = data[i]
        lat, long = accident.lat, accident.long
        fatal = accident.fatal





training_model()
