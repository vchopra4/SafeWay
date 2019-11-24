
from math import sqrt
import pickle
from math import pow
import threading
from collections import OrderedDict
import json


class HandleProdGeo:
    def getCoordinates(self, fileName):
        data = json.loads(fileName)
        print(data)

        finalList = []
        STRIP = "POINTLESRG()"
        for k in range(len(data.loc[:, 'geometry'])):
            line = str(data.at[k, 'geometry']).strip()
            newLine = self.fixGeoDataFrameValue(line, STRIP)
            finalList.append(self.averageCoordinate(newLine.split(',')))

        finalList = sorted(finalList, key=lambda n: n[0])

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
        closestIndex = 0
        closestDistance = self.findDistance(location, coordinateList[0])
        start = 0
        end = len(coordinateList) - 1

        while start < end:
            mid = int((start + end)/2)
            if location[0] > coordinateList[mid][0] and mid + 1 < len(coordinateList) and location[0] < coordinateList[mid][1]:
                d = self.findDistance(location, coordinateList[mid])
                return d, mid
            elif location[0] > coordinateList[mid][0]:
                start = mid + 1
            else:
                end = mid - 1

        return closestDistance, closestIndex

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
        distance = sqrt(pow(float(pA[0])-float(pB[0]), 2) + pow(float(pA[1])-float(pB[1]), 2))
        return 111.9*distance

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


def run(location, cost, prodGeo, model, id):
    closestSchool, csi = prodGeo.getClosestDistance(location, prodGeo.schoolCoordinates)
    closestIntersection, cii = prodGeo.getClosestDistance(location, prodGeo.intersectionCoordinates)
    closestLight, cli = prodGeo.getClosestDistance(location, prodGeo.lightCoordinates)
    closestSign, csig = prodGeo.getClosestDistance(location, prodGeo.signCoordinates)
    closestTrafficIndex = prodGeo.getClosestIndex(location, prodGeo.trafficCoordinates)

    traffic = prodGeo.trafficValues[closestTrafficIndex]

    vals = [[traffic, closestIntersection, closestSchool, closestSign, closestLight]]

    cost[id] = model.predict(vals)[0]

    return True

class HandleData:
    def __init__(self):
        self.prodGeo = HandleProdGeo()
        file = open('k_reg.pickle', 'rb')
        self.model = pickle.load(file)



    def run_thread(self, coords):
        cost = OrderedDict()
        threads = []
        
        count = 0

        for c in coords:
            avg_lat = (c['lat1']['lat'] + c['lng1']['lat'])/2
            avg_lng = (c['lat1']['lng'] + c['lng1']['lng'])/2
            x = threading.Thread(target=run, args=([avg_lng, avg_lat], cost, self.prodGeo, self.model, count))
            cost[count] = 0
            count += 1
            x.start()
            threads.append(x)

        flag = True
        while flag:
            flag = False
            for i in threads:
                flag = flag or i.is_alive()

        for i in range(len(threads)):
            threads[i].join()

        total_cost = []
        for cos in cost:
            total_cost.append(cost[cos])

        return total_cost


