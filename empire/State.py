from typing import OrderedDict, Tuple
from update import *
from Action import *

class State:
    def __init__(self, parent, current, actions):
        self.parentState = parent
        self.currentEmpire = current
        self.actions = actions
        if self.parentState == None and self.actions == None:
            self.pathCost = 0
        else:
            self.pathCost = self.actions.calCost() + self.parentState.pathCost

    def update(self):
        a = Action()
        a.acts = {'update':"*"}
        return {"a1":a}

    def des(self):
        """
        self.coa = int(words[15]) #1 is coa 0 is not
        self.nextDes = int(words[16])
        self.min = int(words[17])
        self.gold = int(words[18])
        self.fert = int(words[19])
        self.ocontent = int(words[20])
        self.uran = int(words[21])
        """
        sects = self.currentEmpire['sect'].values()
        excluse = []
        for sect in sects:
            if sect.des == "c" and sect.isCap:
                excluse.append(sect.location)
            if sect.des != "c":
                excluse.append(sect.location)

        # Logic One
        totalA = round(len(sects) / 5) # 2
        totalM = round(len(sects) / 2.5) #4
        if len(sects) < 2:
            totalM = 0
        
        action1 = Action()

        if len(excluse) < 10:
            # fert first:
            
            orderByFert = self.orderBy("fert")
            action1.acts['designate'] = []
            action1.acts['capital'] = []

            for i in range(totalA):
                action1.acts['designate'].append([orderByFert[i].location, "a"])
                excluse.append(orderByFert[i].location)

            # mine second
            orderByMine = self.orderBy("min",excluse)
            for i in range(totalM):
                action1.acts['designate'].append([orderByMine[i].location, "m"])
                excluse.append(orderByMine[i].location)

            # coa 
            orderByCoa = self.orderBy("coa",excluse)
            if len(orderByCoa) > 0:
                action1.acts['designate'].append([orderByCoa[0].location, "h"])
                excluse.append(orderByCoa[0].location)

            # j
            orderByGrade = self.gradeSector(excluse, True)
            if len(orderByGrade) > 0:
                action1.acts['designate'].append([orderByGrade[0].location, "j"])
                excluse.append(orderByGrade[0].location)

            # k
            orderByGrade = self.gradeSector(excluse, True)
            if len(orderByGrade) > 0:
                action1.acts['designate'].append([orderByGrade[0].location, "k"])
                excluse.append(orderByGrade[0].location)

            # cap
            orderByGrade = self.gradeSector(excluse, False)
            if len(orderByGrade) > 0:
                action1.acts['capital'].append([orderByGrade[0].location, "c"])
                excluse.append(orderByGrade[0].location)

        return {"a1":action1}

    # Spread out population and food
    def spread(self):
        sects = self.currentEmpire['sect']
        # logic one
        action1 = Action()
        action1.acts['move'] = []

        # spread ppl first then food
        orderByFoodDes = self.orderBy("food")
        orderByFoodIns = self.orderBy("food",[], False)

        orderByPopuDes = self.orderBy("popu")
        orderByPopuIns = self.orderBy("popu", [], False)

        for i in range(len(sects)):
            evenPpl = round( (orderByPopuDes[i].civ - orderByPopuIns[i].civ) / 2)
            if evenPpl < orderByPopuDes[i].civ and evenPpl > 1 and orderByPopuIns[i].civ < 250:
                action1.acts['move'].append([orderByPopuDes[i].location, 'civ', evenPpl, orderByPopuIns[i].location])

            evenFood = round( (orderByFoodDes[i].food - orderByFoodIns[i].food) / 2)
            if evenFood < orderByPopuDes[i].food and evenFood > 1 and orderByFoodIns[i].food < 200:
                action1.acts['move'].append([orderByPopuDes[i].location, 'food', evenFood, orderByPopuIns[i].location])

        return {"a1":action1}


    def adjustDist(self):
        sects = self.currentEmpire['sect']

        action1 = Action()
        action1.acts['distribute'] = []
        action1.acts['threshold'] = []
        habor = sects[self.orderBy("habor")[0].location]


        # check dist
        for loca in sects:
            sector = sects[loca]
            if sector.location != habor.location:

                if sector.dst != habor.location:
                    # first time set up dist
                    action1.acts['distribute'].append([sector.location, habor.location])

                foodTimes = int(sector.civ)
                if foodTimes > 200:
                    foodTimes = 200
                ironBase = 100
                ironBase *= int(sector.civ / 300)
                haborIron = habor.iron
                if ironBase > 250:
                    ironBase = 250
                if haborIron > 250:
                    haborIron = 250

                if sector.des == "a":
                    foodCost = int(sector.calculateFoodCost() * foodTimes)
                else: 
                    foodCost = int(sector.calculateFoodCost() * foodTimes * 1.5)

                if foodCost > sector.f_dist:
                    action1.acts['threshold'].append([sector.location, "food", foodCost])
                    
                pplBase = sector.civ + int(habor.civ / 2)
                if pplBase < 400:
                    action1.acts['threshold'].append([sector.location, "civ", pplBase])

                if sector.des == "m":
                    action1.acts['threshold'].append([sector.location, "iron", ironBase])
                elif sector.des == "j":
                    action1.acts['threshold'].append([sector.location, "lcm", 1])
                    action1.acts['threshold'].append([sector.location, "iron", haborIron * 1])
                elif sector.des == "k":
                    action1.acts['threshold'].append([sector.location, "hcm", 1])
                    action1.acts['threshold'].append([sector.location, "iron", haborIron * 2])

                # else:
                    # action1.acts['threshold'].append([sector.location, "civ", 0])


                production = sector.calculateProduction()

                print(production)



        return {'a1':action1}

    def build(self):
        sects = self.currentEmpire['sect']

        action1 = Action()
        action1.acts['build'] = []
        habor = sects[self.orderBy("habor")[0].location]

        #                           lcm hcm avail tech $
        # fb   fishing boat          25  15    75    0 $180
        if habor.lcm >= 25 and habor.hcm >= 15 and habor.avail >= 75:
            action1.acts['build'].append([habor.location])

        return {'a1':action1}


    def orderBy(self, what,excluse=[],des=True):
        orderedLst = []
        temp = self.currentEmpire['sect'].copy()

        # print(excluse)

        if excluse != []:
            for loca in excluse:
                del temp[loca]

        sects = temp.values()

        # print(len(sects))

        if what == "food":
            orderedLst = sorted(sects, key = lambda sect : sect.food, reverse=des)
        elif what == "fert":
            orderedLst = sorted(sects, key = lambda sect : sect.fert, reverse=des)
        elif what == "min":
            orderedLst = sorted(sects, key = lambda sect : sect.min, reverse=des)
        elif what == "iron":
            orderedLst = sorted(sects, key = lambda sect : sect.iron, reverse=des)
        elif what == "popu":
            orderedLst = sorted(sects, key = lambda sect : sect.civ + sect.mil, reverse=des)        
        elif what == "lcm":
            orderedLst = sorted(sects, key = lambda sect : sect.lcm, reverse=des)
        elif what == "hcm":
            orderedLst = sorted(sects, key = lambda sect : sect.hcm, reverse=des)
        elif what == "coast":
            orderedLst = sorted(sects, key = lambda sect : sect.coa, reverse=des)
        elif what == "habor":
            orderedLst = sorted(sects, key = lambda sect : sect.des == 'h', reverse=des)
        elif what == "coa":
             orderedLst = sorted(sects, key = lambda sect : sect.coa == 1, reverse=des)

        else:
            print("need code for "+what+"\n")
            return None

        return orderedLst

    def gradeSector(self,excluse=[],des=True):
        orderedLst = []
        temp = self.currentEmpire['sect'].copy()
        
        if excluse != []:
            for loca in excluse:
                del temp[loca]

        sects = temp.values()

        orderedLst = sorted(sects, key = lambda sect : sect.fert + sect.min + sect.ocontent + sect.uran + sect.coa, reverse=des)

        return orderedLst

