# !/usr/bin/python3
class State:
    def __init__(self, cities):
        self.cities = cities
        self.cost = self.calculateCost()
    
    def calculateCost(self):
        cost = 0
        for i in range(len(self.cities)):
            if i < len(self.cities) - 1:
                cost += self.cities[i].map[self.cities[i+1].name]
                # print(self.cities[i+1].name)
        return cost

    def getPath(self):
        path = []
        for city in self.cities:
            path.append(city.name)
        return path
