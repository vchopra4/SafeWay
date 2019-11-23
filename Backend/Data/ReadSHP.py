import shapefile
import os
import math


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

        # Likely going to have to sort by latitude in order to perform a binary search to make reading a file faster
        self.points = key = lambda i: i['coordinates'][0]

    def binary_search(self, long, lat):
        start = 0
        end = len(self.points)

        hard_coded_limit = 0.1
        hard_coded_return = 1

        while start <= end:
            mid = int((start + end)/2)
            lo = self.points[mid]['coordinates'][0]
            la = self.points[mid]['coordinates'][1]
            if abs(lo - long) < hard_coded_limit:
                dist = math.sqrt(math.pow(lo - long, 2) + math.pow(la - long, 2))
            elif lo > long:
                end = mid - 1
            else:
                start = mid + 1

        return 1
