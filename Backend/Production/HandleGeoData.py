import geopandas
from math import sqrt
import pickle
from sklearn.preprocessing import RobustScaler
import numpy as np


class HandleProdGeo:
    def getCoordinates(self, fileName):
        data = geopandas.read_file(fileName)

        finalList = []
        STRIP = "POINTLESRG()"
        for k in range(len(data.loc[:, 'geometry'])):
            line = str(data.at[k, 'geometry']).strip()
            newLine = self.fixGeoDataFrameValue(line, STRIP)
            finalList.append(self.averageCoordinate(newLine.split(',')))

        return finalList

    def getVolumeCount(self, fileName):
        data = geopandas.read_file(fileName)
        finalList = []
        STRIP = "POINTLESRG()"
        for k in range(len(data.loc[:, 'VolumeCount'])):
            line = str(data.at[k, 'VolumeCount']).strip()
            newLine = self.fixGeoDataFrameValue(line, STRIP)
            finalList.append(newLine)
        return finalList

    def getClosestDistance(self, location, coordinateList):
        # closestIndex = 0
        scaler = RobustScaler(copy=True, quantile_range=(25.0, 75.0), with_centering=True, with_scaling=True)
        scaler.fit(coordinateList)
        coordinateList = scaler.transform(coordinateList)
        closestDistance = self.findDistance(location, coordinateList[0])
        for i in range(1, len(coordinateList)):
            d = self.findDistance(location, coordinateList[i])
            if d < closestDistance:
                closestDistance = d
                # closestIndex = i
        return closestDistance

    def getClosestIndex(self, location, coordinateList):
        closestIndex = 0
        closestDistance = self.findDistance(location, coordinateList[0])
        for i in range(1, len(coordinateList)):

            d = self.findDistance(location, coordinateList[i])
            if d < closestDistance:
                closestDistance = d
                closestIndex = i
        return closestIndex


    # only needs to be used internally
    def findDistance(self, pA, pB):
        distance = sqrt((float(pA[0])-float(pB[0]))**2 + (float(pA[1])-float(pB[1]))**2)
        return distance

    def averageCoordinate(self, xyList):
        xSum = 0
        ySum = 0
        for i in xyList:
            point = i.split()
            xSum += float(point[0])
            ySum += float(point[1])
        xAverage = xSum/len(xyList)
        yAverage = ySum/len(xyList)
        avCoordinate = [xAverage, yAverage]

        return avCoordinate


    def fixGeoDataFrameValue(self, line, unwanted):
        newLine = ""
        for i in line:
            if i not in unwanted:
                newLine += i
        return newLine

    def __init__(self):
        self.schoolCoordinates = self.getCoordinates("School_Crossings.geojson")
        self.intersectionCoordinates = self.getCoordinates("Intersection_Types.geojson")
        self.lightCoordinates = self.getCoordinates("Street_Lighting.geojson")
        self.signCoordinates = self.getCoordinates("Traffic_Signs.geojson")
        self.trafficCoordinates = self.getCoordinates("Traffic_Volumes.geojson")
        self.trafficValues = self.getVolumeCount("Traffic_Volumes.geojson")



def run(location):
    prodGeo = HandleProdGeo()
    closestSchool = prodGeo.getClosestDistance(location, prodGeo.schoolCoordinates)
    closestIntersection = prodGeo.getClosestDistance(location, prodGeo.intersectionCoordinates)
    closestLight = prodGeo.getClosestDistance(location, prodGeo.lightCoordinates)
    closestSign = prodGeo.getClosestDistance(location, prodGeo.signCoordinates)
    closestTrafficIndex = prodGeo.getClosestIndex(location, prodGeo.trafficCoordinates)


    trValsAdj = np.array(prodGeo.trafficValues)
    trValsAdj = trValsAdj.reshape(-1, 1)
    scaler = RobustScaler(copy=True, quantile_range=(25.0, 75.0), with_centering=True, with_scaling=True)
    scaler.fit(trValsAdj)
    trVals = scaler.transform(trValsAdj)
    traffic = trVals[closestTrafficIndex]

    vals = [[closestIntersection, closestSchool, closestSign, closestLight, traffic]]
    file = open('model.pickle', 'rb')
    model = pickle.load(file)

    hard_code_add = 44000

    print(model.score_samples(vals)[0] + hard_code_add)


run([-81.273547, 43.011173])
run([-81.253038, 42.996176])
run([-81.207588, 43.000732])
run([-81.276542, 43.001993])
