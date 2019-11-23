import shapefile
import os


class ReadSHPFile:
    def __init__(self, file_name, data_type):
        self.points = []
        self.f_name = file_name
        self.read_file()
        self.type = data_type

    def read_file(self):
        assert os.path.exists(self.f_name)
        shape = shapefile.Reader(self.f_name)
        features = shape.shapeRecords()
        shape.iterShapeRecords()
        for i in range(len(features)):
            dt = features[i].shape.__geo_interface__
            self.points.append(dt)
