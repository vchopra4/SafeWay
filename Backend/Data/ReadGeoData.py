import geopandas

def getCoordinates(fileName, attribute):
    data = geopandas.read_file(fileName)
    finalList = []
    STRIP = "POINTLESRG()"
    for k in range(len(data.loc[:, attribute])):
        line = str(data.at[k, attribute]).strip()
        newLine = ""
        for i in line:
            if i not in STRIP:
                newLine += i
        if ',' in newLine:
            list = newLine.split(',')
            for i in range(len(list)):
                list[i] = list[i].split()
                finalList.append(list)
        elif ' ' in newLine:
            list = newLine.split()
            finalList.append(list)
        else:
            finalList.append(newLine)
    return finalList

