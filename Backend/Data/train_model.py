import glob
import ReadSHP
import ReadAccident



def training_model():
    shp_files = glob.glob('shapefiles/*.shp')

    shp_data = []
    for s in shp_files:
        shp_data.append(ReadSHP.ReadSHPFile(s, s))

    accident_files = glob.glob('accident/*.csv')
    a = 0
    for file in accident_files:
        a = ReadAccident.Accident(file)

    # Adjust for the number of cars that travel through the intersection



training_model()
