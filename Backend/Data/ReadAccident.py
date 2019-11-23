import pandas as pd


class Accident:

    data = []

    def __init__(self, f_name):
        self.f_name = f_name
        self.frame = pd.read_csv(self.f_name)
        self.read_file()

    def read_file(self):
        for f in self.frame.index.values:
            lat = self.frame.loc[f, 'LATITUDE']
            long = self.frame.loc[f, 'LONGITUDE']
            fatal = self.frame.loc[f, 'ACCLASS']
            ped = self.frame.loc[f, 'IMPACTYPE']
            self.data.append(Location(lat, long, fatal, ped))


class Location:
    def __init__(self, lat, long, fatal, ped):
        self.lat = lat
        self.long = long
        self.fatal = not ('non-fatal' in fatal.lower())
        self.involves_ped = ped.lower() == 'pedestrian'

