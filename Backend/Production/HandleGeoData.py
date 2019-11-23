import geopandas
from math import sqrt

def getCoordinates(fileName):
    data = geopandas.read_file(fileName)
    finalList = []
    STRIP = "POINTLESRG()"
    for k in range(len(data.loc[:, 'geometry'])):
        line = str(data.at[k, 'geometry']).strip()
        newLine = fixGeoDataFrameValue(line, STRIP)
        finalList.append(averageCoordinate(newLine.split(',')))

    return finalList
def getVolumeCount(fileName):
    data = geopandas.read_file(fileName)
    finalList = []
    STRIP = "POINTLESRG()"
    for k in range(len(data.loc[:, 'VolumeCount'])):
        line = str(data.at[k, 'VolumeCount']).strip()
        newLine = fixGeoDataFrameValue(line, STRIP)
        finalList.append(newLine)
    return finalList

def getClosestObject(location, coordinateList):
    closestIndex = 0
    closestDistance = findDistance(location, coordinateList[0])
    for i in range(1, len(coordinateList)):
        d = findDistance(location, coordinateList[i])
        if d < closestDistance:
            closestDistance = d
            closestIndex = i
    return closestIndex


# only needs to be used internally
def findDistance(pA, pB):
    distance = sqrt((float(pA[0])-float(pB[0]))**2 + (float(pA[1])-float(pB[1]))**2)
    return distance
def averageCoordinate(xyList):
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

def fixGeoDataFrameValue(line, unwanted):
    newLine = ""
    for i in line:
        if i not in unwanted:
            newLine += i
    return newLine
