# !/usr/bin/python3
class Result:
    def __init__(self):
        self.track = {}
    
    def onlyCostandName(self):
        contain = {}
        for cost in self.track:
            contain[cost] = []
            for pathObject in self.track[cost]:
                path = []
                for cityObject in pathObject:
                    path.append(cityObject.name)
                contain[cost].append(path)
        return contain
    
    def printCostandName(self):
        contain = self.onlyCostandName()
        for cost in sorted(contain):
            print(cost)
            for path in contain[cost]:
                print(path)
    
    def printCostRange(self):
        contain = self.onlyCostandName()
        lowest = ""
        highest = 0
        for cost in sorted(contain):
            if lowest == "":
                lowest = cost
                continue
            else:
                if cost < lowest:
                    lowest = cost
                    continue
            
            if cost > highest:
                highest = cost
                continue

        print(str(lowest) + " ~ " + str(highest))
