# !/usr/bin/python3

import os
import logging
import sys
from map import *

logFilePath = 'log/readMain.log'

# Read Helper
def formatLines (rawLst):
    new = []
    for each in rawLst:
        if each[0] != '#':
            each.strip()
            new.append(each)

    out = []
    for each in new:
        out.append(each.replace("\n", ""))
    return out

def fromLinesToDict(lines):
    dic = {}
    for each in lines:
        temp = each.split()
        if temp[0] == "size":
            dic[temp[0]] = (int(temp[1]))
        else:
            dic[temp[0]] = (temp[1])
    return dic

def getRealtedFilesInfo(ret):
    return fromLinesToDict(formatLines(ret))





def read (mainName):
    if os.path.exists(logFilePath):
        os.remove(logFilePath)
        print("# Removed old log file #")
    
    logging.basicConfig(filename=logFilePath, filemode='w', level=logging.INFO)

    cwd = os.getcwd()
    logging.info(cwd)
    filePath = os.path.join(cwd + "/data", mainName)

    cities = []

    if os.path.exists(filePath):
        logging.info(filePath + "  exists")

        with open(filePath) as f:
            ret = f.readlines()
            infoS = getRealtedFilesInfo(ret)
            logging.info(infoS)

            # print(infoS)

            if len(ret) < 1:
                print("File is empty")
                logging.warning("File is empty")
                sys.exit(0)

            # Read Related Files:
            # dist:
            distPath = os.path.join(cwd + "/data", infoS['dist'])
            if os.path.exists(distPath):
                logging.info("\tdist path : " + distPath + "  exists")
                with open(distPath) as distF:
                    distRet = distF.readlines()
                    distLst = formatLines(distRet)
                    logging.info(distLst)

                    # print(distLst)


            else:
                print("\tdist path : " + distPath + " doesn't exist")
                logging.warning(distPath + " doesn't exist")
                sys.exit(0)

            # name:
            namePath = os.path.join(cwd + "/data", infoS['name'])
            if os.path.exists(namePath):
                logging.info("\tname path : " + namePath + "  exists")
                with open(namePath) as nameF:
                    nameRet = nameF.readlines()
                    nameLst = formatLines(nameRet)
                    logging.info(nameLst)

                    #print(nameLst)


            else:
                print("\tname path : " + namePath + " doesn't exist")
                logging.warning(namePath + " doesn't exist")
                sys.exit(0)

            # Constructing the Map:
            for i in range(infoS["size"]):
                city = City(nameLst[i], infoS["size"], nameLst, distLst[i])
                cities.append(city)

            if len(cities) < 1:
                print("There is not city in file")
                logging.info("There is not city in file")
                sys.exit(0)

            
            logCities(cities)
            return cities
    else:
        print(filePath + " doesn't exist")
        logging.warning(filePath + " doesn't exist")
        sys.exit(0)

def logCities(cities):
    temp = []
    for city in cities:
        temp.append(city.__dict__)
    
    logging.info("\n\tCities: ")
    logging.info(temp)

def printMap(cities):
    for city in cities:
        print(city.__dict__)