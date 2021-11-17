# !/usr/bin/python3

class City:
    def __init__(self,name, size, nameLst, distLst):
        self.name = name
        self.map = {}
        line = distLst.split()
        for i in range(size):
            self.map[nameLst[i]] = int(line[i])
        
    def loopUpDist(self, name):
        if name in self.map:
            return self.map[name]
        else:
            return -1 # mean couldn't find this city
