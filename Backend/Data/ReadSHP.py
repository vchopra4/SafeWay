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

        fields = shape.fields[1:]
        fields_name = [field[0] for field in fields]

        attributes = shape.records()

        for i in range(len(features)):
            if not 'TOPO_POLES' in self.f_name or attributes[i][1] == 'Street Light Pole' or attributes[i][1] == 'Pedestrian Light Pole':
                dt = features[i].shape.__geo_interface__
                self.points.append(dt)
            elif 'TSignals' in self.f_name and 'Traffic Signal Pole' in attributes[i][1]:
                dt = features[i].shape.__geo_interface__
                self.points.append(dt)

        # Likely going to have to sort by latitude in order to perform a binary search to make reading a file faster
        self.points = sorted(self.points, key = lambda n: n['coordinates'][0])

    def binary_search(self, long, lat):
        start = 0
        end = len(self.points)

        while start < end:
            mid = int((start + end)/2)
            lo = self.points[mid]['coordinates'][0]
            la = self.points[mid]['coordinates'][1]

            if self.points[mid]['coordinates'][0] < long and mid + 1 < len(self.points) and self.points[mid + 1]['coordinates'][0] > long:
                dist = math.sqrt(math.pow(lo - long, 2) + math.pow(la - lat, 2))
                return dist
            elif lo > long:
                end = mid - 1
            else:
                start = mid + 1

        last_point_lo = self.points[len(self.points) - 1]['coordinates'][0]
        last_point_la = self.points[len(self.points) - 1]['coordinates'][1]

        last_point_dist = math.sqrt(math.pow(last_point_lo - long, 2) + math.pow(last_point_la - lat, 2))
        return last_point_dist
