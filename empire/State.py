from update import *
from Action import *
import copy

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

        a = 0
        m = 0
        h = 0
        j = 0
        k = 0

        for sect in sects:
            if sect.des == "c" and sect.location == self.currentEmpire['extra'].capLoca:
                excluse.append(sect.location)
            if sect.des != "c":
                if sect.des == "a":
                    a += 1
                if sect.des == "m":
                    m += 1
                if sect.des == "h":
                    h += 1
                if sect.des == "j":
                    j += 1
                if sect.des == "k":
                    k += 1
                excluse.append(sect.location)

        # Logic One
        totalA = round(len(sects) / 5) - a # 2
        totalM = round(len(sects) / 2.5) - m #4
        if len(sects) < 2:
            totalM = 0
        
        action1 = Action()

        if len(excluse) < 10:
            # fert first:
            
            orderByFert = self.orderBy("fert")
            action1.acts['designate'] = []
            action1.acts['capital'] = []

            if totalA > 0: 
                for i in range(totalA):
                    action1.acts['designate'].append([orderByFert[i].location, "a"])
                    excluse.append(orderByFert[i].location)

            # mine second
            if totalM > 0:
                orderByMine = self.orderBy("min",excluse)
                for i in range(totalM):
                    action1.acts['designate'].append([orderByMine[i].location, "m"])
                    excluse.append(orderByMine[i].location)

            # coa 
            orderByCoa = self.orderBy("coa",excluse)
            if len(orderByCoa) > 0 and h != 1:
                action1.acts['designate'].append([orderByCoa[0].location, "h"])
                self.currentEmpire['extra'].nexthHaborLoca = orderByCoa[0].location
                excluse.append(orderByCoa[0].location)

            # j
            orderByGrade = self.gradeSector(excluse, True)
            if len(orderByGrade) > 0 and j != 1:
                action1.acts['designate'].append([orderByGrade[0].location, "j"])
                excluse.append(orderByGrade[0].location)

            # k
            orderByGrade = self.gradeSector(excluse, True)
            if len(orderByGrade) > 0 and k != 1:
                action1.acts['designate'].append([orderByGrade[0].location, "k"])
                excluse.append(orderByGrade[0].location)

            # cap
            orderByGrade = self.gradeSector(excluse, False)
            if len(orderByGrade) > 0 and len(excluse) < 10:
                action1.acts['capital'].append([orderByGrade[0].location, "c"])
                self.currentEmpire['extra'].nextCapLoca = orderByGrade[0].location
                excluse.append(orderByGrade[0].location)


        """
        hasA = 0
        hasM = 0
        hasCap = 0
        hasJ = 0
        hasK = 0
        hasH = 0

        poor = 0

        for sect in sects:
            if sect.avail < 400 or sect.food < 50:
                poor += 1
            else:
                if sect.des == "c" and sect.location == self.currentEmpire['extra'].capLoca:
                    excluse.append(sect.location)
                    hasCap += 1
                if sect.des != "c":
                    excluse.append(sect.location)
                    if sect.des == "a":
                        hasA += 1
                    elif sect.des == "m":
                        hasM += 1
                    elif sect.des == "j":
                        hasJ += 1
                    elif sect.des == "k":
                        hasK += 1
                    elif sect.des == "h":
                        hasH += 1
        
        # print(excluse)
        # print(self.currentEmpire['extra'].capLoca)

        # Logic One
        action1 = Action()
        action1.acts['designate'] = []
        action1.acts['capital'] = []

        totalA = round(len(sects) / 5) - hasA # 2
        totalM = round(len(sects) / 2.5) - hasM #4
        if len(sects) < 2:
            totalM = 0
        
        
        # POOR condition:!
        if poor > 0:
            # solution for extreme case
            # set one of the place as habor and rest of them as A 
            # make sure food and avil is up then re des all 

            orderByCoa = self.orderBy("coa",excluse)
            if len(orderByCoa) > 0 and hasH < 1:
                for sect in orderByCoa:
                    if hasH < 1 and sect.des != "h" and sect.nextDes != "h":
                        action1.acts['designate'].append([sect.location, "h"])
                        hasH = 1
                        self.currentEmpire['extra'].nexthHaborLoca = sect.location
                        excluse.append(sect.location)

            for sect in sects:
                if sect.location != self.currentEmpire['extra'].nexthHaborLoca and sect.des != "a" and sect.nextDes != "a" and sect.fert > 30:
                    action1.acts['designate'].append([sect.location, "a"])
                    excluse.append(sect.location)
            
            if 10 - len(excluse) > 1:
                orderByMine = self.orderBy("min",excluse)
                for i in range(9 - len(excluse)):
                    if orderByMine[i].des != "m": 
                        action1.acts['designate'].append([orderByMine[i].location, "m"])
                        excluse.append(orderByMine[i].location)
                # print(excluse)
            # cap
            if len(excluse) == 9:
                orderByGrade = self.gradeSector(excluse, False)
                if len(orderByGrade) > 0 and hasCap < 1 and orderByGrade[0].des != 'c':
                    action1.acts['capital'].append([orderByGrade[0].location, "c"])
                    action1.acts['designate'].append([orderByGrade[0].location, "c"])
                    excluse.append(orderByGrade[0].location)

        else:
            if poor == 0:
                hasA = 0
                hasM = 0
                hasCap = 0
                hasJ = 0
                hasK = 0
                hasH = 0
                excluse = [] # after the poor extreme case so need to re des for all

                action1.acts['designate'] = []
                action1.acts['capital'] = []

                totalA = round(len(sects) / 5) - hasA # 2
                totalM = round(len(sects) / 2.5) - hasM #4
                if len(sects) < 2:
                    totalM = 0

            if len(excluse) < 10:
                # fert first:
                
                orderByFert = self.orderBy("fert")

                for i in range(totalA):
                    if orderByFert[i].des != "m": 
                        action1.acts['designate'].append([orderByFert[i].location, "a"])
                        excluse.append(orderByFert[i].location)
                # print(excluse)

                # coa 
                orderByCoa = self.orderBy("coa",excluse)
                if len(orderByCoa) > 0 and hasH < 1:
                    if orderByCoa[0].des != "h": 
                        action1.acts['designate'].append([orderByCoa[0].location, "h"])
                        excluse.append(orderByCoa[0].location)
                # print(excluse)
                
                # mine second
                orderByMine = self.orderBy("min",excluse)
                for i in range(totalM):
                    if orderByMine[i].des != "m": 
                        action1.acts['designate'].append([orderByMine[i].location, "m"])
                        excluse.append(orderByMine[i].location)
                # print(excluse)

                # j
                orderByGrade = self.gradeSector(excluse, True)
                if len(orderByGrade) > 0 and hasJ < 1 and orderByGrade[0] != "j":
                    action1.acts['designate'].append([orderByGrade[0].location, "j"])
                    excluse.append(orderByGrade[0].location)
                # print(excluse)

                # k
                orderByGrade = self.gradeSector(excluse, True)
                if len(orderByGrade) > 0 and hasK < 1 and orderByGrade[0].des != "k":
                    action1.acts['designate'].append([orderByGrade[0].location, "k"])
                    excluse.append(orderByGrade[0].location)
                # print(excluse)

                # cap
                orderByGrade = self.gradeSector(excluse, False)
                if len(orderByGrade) > 0 and hasCap < 1 and orderByGrade[0].des != "c":
                    action1.acts['capital'].append([orderByGrade[0].location, "c"])
                    action1.acts['designate'].append([orderByGrade[0].location, "c"])
                    excluse.append(orderByGrade[0].location)
                # print(excluse)

            
            for a in action1.acts:
                print(a)
                print(action1.acts[a])
       """
        index = 0
        for i in self.orderBy("mine"):
            if index < m :
                if i.des != "a" and i.des != "h" and i.des != "j" and i.des != "k" and i.des != "c":
                    if i.iron > 200 and i.lcm < 40:
                        action1.acts['designate'].append([i.location, "j"])
                        
                    elif i.iron > 200 and i.hcm < 30:
                        action1.acts['designate'].append([i.location, "k"])
                    
                    else:
                        action1.acts['designate'].append([i.location, "m"])
                index += 1


        return {"a1":action1}

    # Spread out population and food
    def spread(self):
        sects = self.currentEmpire['sect']
        temp = Update([self.currentEmpire])
        # logic one
        action1 = Action()
        action1.acts['move'] = []

        # spread ppl first then food
        orderByFoodDes = self.orderBy("food")
        totalFood = -10
        for sect in orderByFoodDes:
            totalFood += sect.food
        evenFood = round(totalFood / 10)

        if evenFood > 30:
            evenFood = 30

        orderByPopuDes = self.orderBy("popu")
        totalPpl = -10
        for sect in orderByPopuDes:
            totalPpl += sect.civ
        evenPpl = round(totalPpl/ 10)

        if evenPpl > 20:
            evenPpl = 20
        # print(evenPpl)


        for i in range(len(sects)):
            commandPpl = []
            commandFood = []

            if evenPpl < self.orderBy("popu")[0].civ and evenPpl > 1 and self.orderBy("popu")[0].location != self.orderBy("popu",[], False)[0].location:
                commandPpl = [self.orderBy("popu")[0].location, 'civ', evenPpl, self.orderBy("popu",[], False)[0].location]

            if evenFood < self.orderBy("food")[0].food and evenFood > 1 and self.orderBy("food")[0].location != self.orderBy("food", [], False)[0].location:
                commandFood = [self.orderBy("food")[0].location, 'food', evenFood, self.orderBy("food", [], False)[0].location]
            
            if commandPpl != []:
                action1.acts['move'].append(commandPpl)
                # excute it rn
                temp.handle("move", commandPpl)
            if commandFood != []:
                action1.acts['move'].append(commandFood)
                # excute it rn
                temp.handle("move",  commandFood)
        """
        # do move right now:
        for command in action1.acts["move"]:
            print(command)
            temp.handle("move", command)
        """
        """
        print(action1.acts['move'])
        print("before finish spread")
        for loca in temp.sectors:
            print("after move the state empire should be updated!")
            print(temp.sectors[loca].__dict__)
        """
        # update self.empire


        self.currentEmpire['sect'] = temp.sectors

        return {"a1":action1}

    def adjustDist(self):
        sects = self.currentEmpire['sect']

        action1 = Action()
        action1.acts['distribute'] = []
        action1.acts['threshold'] = []

        if self.currentEmpire['extra'].haborLoca == 0 and self.currentEmpire['extra'].nexthHaborLoca == 0:
            print("habor is not des yet!")

        if  self.currentEmpire['extra'].haborLoca != 0 or self.currentEmpire['extra'].nexthHaborLoca != 0:
            if self.currentEmpire['extra'].haborLoca != 0:
                habor = sects[self.currentEmpire['extra'].haborLoca]
            else:
                habor = sects[self.currentEmpire['extra'].nexthHaborLoca]

            
            # check dist
            for loca in sects:
                sector = sects[loca]
                if sector.location != habor.location:

                    if sector.dst != habor.location:
                        # first time set up dist
                        action1.acts['distribute'].append([sector.location, habor.location])

                    ironBase = 100
                    ironBase *= int(sector.civ / 300)
                    haborIron = habor.iron
                    haborLcm = habor.lcm
                    haborHcm = habor.hcm
                    haborFood = habor.food

                    if ironBase > 250:
                        ironBase = 250
                    if haborIron > 250:
                        haborIron = 250

                    foodCost = int(sector.calculateFoodCost())

                    if sector.des == "a":
                        foodCost *= 1.5
                    else:
                        foodCost *= 3
                    if foodCost > haborFood/5:
                        foodCost = int(sector.calculateFoodCost())
                    if foodCost > haborFood/5:
                        foodCost = haborFood/5

                    # if foodCost < 50:
                        # foodCost += 40

                    if foodCost > sector.f_dist:
                        action1.acts['threshold'].append([sector.location, "food", int(foodCost)])
                    
                    """
                    if  sector.calculateFoodCost() > sector.f_dist + sector.food:
                        action1.acts['threshold'].append([sector.location, "food", foodCost])
                    
                    # not to dist ppl
                    pplBase = sector.civ + int(habor.civ / 2)
                    if pplBase > 400:
                        pplBase = 0
                    if pplBase != sector.c_dist:
                         
                        action1.acts['threshold'].append([sector.location, "civ", pplBase])
                    """

                    if sector.des == "m":
                        if 1 != sector.i_dist:
                            action1.acts['threshold'].append([sector.location, "iron", 1])
                    if sector.des == "j":
                        if 1 != sector.l_dist:
                            action1.acts['threshold'].append([sector.location, "lcm", 1])
                        if haborLcm < 50:
                            if haborIron / 3 != sector.i_dist:
                                action1.acts['threshold'].append([sector.location, "iron", int(haborIron / 3)])
                        else:
                            action1.acts['threshold'].append([sector.location, "iron", 1])

                    if sector.des == "k":
                        if 1 != sector.h_dist:
                            action1.acts['threshold'].append([sector.location, "hcm", 1])
                        if haborLcm < 30:
                            if haborIron / 3 * 2 != sector.i_dist:
                                action1.acts['threshold'].append([sector.location, "iron", int(haborIron / 3 * 2)])
                        else:
                            action1.acts['threshold'].append([sector.location, "iron", 1])

                    # else:
                        # action1.acts['threshold'].append([sector.location, "civ", 0])


                    # production = sector.calculateProduction()

                    # print(production)


        return {'a1':action1}

    def build(self):
        sects = self.currentEmpire['sect']

        action1 = Action()
        action1.acts['build'] = []
        if len(self.orderBy("habor")) != 0:
            habor = sects[self.orderBy("habor")[0].location]

            #                           lcm hcm avail tech $
            # fb   fishing boat          25  15    75    0 $180
            if habor.lcm >= 25 and habor.hcm >= 15 and habor.avail >= 75:
                action1.acts['build'].append([habor.location])

        return {'a1':action1}


    def orderBy(self, what,excluse=[],des=True):
        orderedLst = []
        temp = copy.deepcopy(self.currentEmpire['sect'])

        # print(excluse)
        if excluse != []:
            for loca in excluse:
                if loca in temp:
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
        elif what == "coaA":
             orderedLst = sorted(sects, key = lambda sect : sect.coa + sect.avail , reverse=des)
        elif what == "mine":
             orderedLst = sorted(sects, key = lambda sect : sect.des == "m" , reverse=des)   

        else:
            print("need code for "+what+"\n")
            return None

        return orderedLst

    def gradeSector(self,excluse=[],des=True):
        orderedLst = []
        temp = copy.deepcopy(self.currentEmpire['sect'])
        
        if excluse != []:
            for loca in excluse:
                if loca in temp:
                    del temp[loca]

        sects = temp.values()

        orderedLst = sorted(sects, key = lambda sect : sect.fert + sect.min + sect.ocontent + sect.uran + sect.coa, reverse=des)

        return orderedLst

    def isGoalState(self):
        nation = self.currentEmpire

        if len(nation['sect']) < 10:
            # print("don't have 10 sector")
            return False

        for loca in nation['sect']:
            sect = nation['sect'][loca]
            if sect.civ < 1000:
                # print("don't have 1000 people")
                # print(sect.des)
                # print("civ")
                # print(sect.civ)
                return False
        
        if len(nation['ship']) < 1:
            # print("dont have ship")
            return False

        for uid in nation['ship']:
            ship = nation['ship'][uid]
            if ship.type == 0:
                return True
        
        return False

