#!/usr/bin/env python3
from typing import Tuple
from empire import *

def checkHinPath(path):
    if "h" in path:
        return True
    elif 'H' in path:
        return True
    else:
        return False
        
def itemOutCheck(s, item, change):
    if item == "min":
        return s.min >= change
    elif item == "gold":
        return s.gold >= change
    elif item == "oil":
        return s.oil >= change
    elif item == "uran":
        return s.mil >= change
    elif item == "civ":
        return s.civ >= change
    elif item == "shell":
        return s.shell >= change
    elif item == "gun":
        return s.gun >= change
    elif item == "petrol":
        return s.pertrol >= change
    elif item == "iron":
        return s.iron >= change
    elif item == "dust":
        return s.dust >= change
    elif item == "bar":
        return s.bar >= change
    elif item == "food":
        return s.food >= change
    elif item == "lcm":
        return s.lcm >= change
    elif item == "hcm":
        return s.hcm >= change
    elif item == "uw":
        return s.uw >= change
    elif item == "rad":
        return s.rad >= change
    return False

def itemChange(s,item,change):
    if item in itemLst:
        if item == "min":
            s.min += change
        elif item == "gold":
            s.gold += change
        elif item == "oil":
            s.oil += change
        elif item == "uran":
            s.mil += change
        elif item == "civ":
            s.civ += change
            if s.civ > 1000:
                s.civ = 1000
        elif item == "shell":
            s.shell += change
        elif item == "gun":
            s.gun += change
        elif item == "petrol":
            s.pertrol += change
        elif item == "iron":
            s.iron += change
        elif item == "dust":
            s.dust += change
        elif item == "bar":
            s.bar += change
        elif item == "food":
            s.food += change
        elif item == "lcm":
            s.lcm += change
        elif item == "hcm":
            s.hcm += change
        elif item == "uw":
            s.uw += change
        elif item == "rad":
            s.rad += change
        else :
            print(item)
            print("item is not vaild in itemChange()") 
    else:
        print(item)
        print("item is not in the item list!")

def pathToEnd(start,path):
    end = start
    for d in path:
        if d == "h":
            break
        else:
            end = moveTowhere(start,d)
    return end

def moveTowhere(start, direction):
    
    if direction == "j":
        toLocation = (start[0] + 2, start[1])
    elif direction == "g":
        toLocation = (start[0] - 2, start[1])
    elif direction == "y":
        toLocation = (start[0] - 1, start[1] - 1)
    elif direction == "u":
        toLocation = (start[0] + 1, start[1] - 1)
    elif direction == "b":
        toLocation = (start[0] - 1, start[1] + 1)
    elif direction == "n":
        toLocation = (start[0] + 1, start[1] + 1)
    elif direction == "h":
        toLocation = start
    else :
        toLocation = start
        print(direction)
        print("moveToWhere() has a unvalid direction, defa return the start")
    return toLocation

class Move:
    def __init__(self, contain, dist=False, overridePath=False):
            # print(contain)
            self.empire = contain[0]
            self.start = contain[1]
            self.item = contain[2]
            self.amount = contain[3]
            self.end = contain[4]

            self.dist = dist
            self.overridePath = overridePath

            if dist:
                self.overridePath = dist
                
            if self.overridePath != True:
                self.path = contain[4]
                self.end = pathToEnd(self.start, self.path)


    def calculateMobCost(self):
        s = self.empire['sect'][self.start]
        pathCost = self.calculateTotalPathCost()
        # print("pathCost " + str(pathCost))
        if self.item == "bar":
            weight = 50
        elif self.item == "gun":
            weight = 10
        elif self.item == "rad":
            weight = 8
        elif self.item == "uw":
            weight = 2
        else :
            weight = 1

        packing = 1
        if s.eff >= 60:
            if self.item == "civ":
                packing = 10
            if s.des == "w" or s.des == "h" or self.end == self.empire['extra'].haborLoca:
                packing = 10

        # print("eff: " + str(s.eff))
        # print("item : " + self.item)
        # print(s.des + " packing " + str(packing))

        mobCost = int(self.amount * weight * pathCost / packing)
        return mobCost

    def getPathCostforOneSector(self, location):
        return 0.4 - 0.002 * self.empire["sect"][location].eff

    def calculateTotalPathCost(self):
        # assume the whole path is valid 
        # which mean it is mob avibility > the whole cost 
        # not moving to unclaimed sector

        start = self.start
        cost = 0 
        if self.overridePath:
            cost = ( 0.4 - 0.002 * self.empire['sect'][start].eff )* abs(self.end[1] - start[1]) + abs(self.end[0] - start[0]) / 2
        else:
            self.end = pathToEnd(self.start, self.end)
            for move in self.path:
                if move == "h":
                    break
                elif move in moveDirection:
                    direction = moveTowhere(start, move)
                    cost += self.getPathCostforOneSector(direction)
                    start = direction
                else:
                    print(move)
                    print("direction is not vaild")
        return int(cost)

    def check(self):
        if self.start not in self.empire['sect']:
            # print("move fail! start sector is not vaild")
            # print(self.__dict__)
            return False
        if self.item not in itemLst:
            # print("move fail! item is not vaild")
            # print(self.__dict__)
            return False
        
        if self.overridePath == False:
            if all(elt in moveDirection for elt in self.path) ==  False:
                # print("move fail! path is not vaild")
                # print(self.__dict__)
                return False

        if itemOutCheck(self.empire['sect'][self.start], self.item, self.amount) == False:
            # print(self.start, self.item, self.amount)
            # print("move fail! " + str(self.start) + " doestn't have enough " + self.item +" to"+ str(self.end))
            # print(self.__dict__)
            return False
        return True

    def prediction(self):
        if self.check():
            return self.calculateMobCost()
        else:
            return 0

    def act(self):
        if self.amount != 0:
            # print("move " + str(self.amount) + " of " + self.item + " from " + str(self.start) + " to " + str(self.end))

            s = self.empire['sect'][self.start]

            if self.start == (0, 0) or self.start == (-1, -1):
                print("\n\n\n\n\n")
                print(self.start)
                print(self.item)
                print(self.amount)
                print(self.end)
                if self.start not in self.empire['sect']:
                    print("move fail! start sector is not vaild")
                    
                if self.item not in itemLst:
                    print("move fail! item is not vaild")
                    
                
                if self.overridePath == False:
                    if all(elt in moveDirection for elt in self.path) ==  False:
                        print("move fail! path is not vaild")
                        
                if itemOutCheck(self.empire['sect'][self.start], self.item, self.amount) == False:
                    print(self.start, self.item, self.amount)
                    print("move fail! " + str(self.start) + " doestn't have enough " + self.item +" to"+ str(self.end))

                if s.mob < self.prediction():
                    print("fail")
                    print("move fail! " + str(self.start) + "  doestn't have enough mob to move "+ str(self.amount)+ " " + self.item + " to" + str(self.end))
                    print("total mob need " + str(self.prediction()) + "\nonly have " + str(s.mob))
                else:
                    print("before mob:" + str(s.mob))
                    print("move ok! " + str(self.start) + "  "+ str(self.amount)+ " " + self.item + " to" + str(self.end))
                    print("total mob need " + str(self.prediction()) + "\nleft " + str(s.mob))
                    print(str(self.start) + " move out " + self.item, self.amount)
                    print(str(self.end) + " recives "+ self.item, self.amount)
                    print("after mob: " + str(s.mob))
                    print("ok!")

                print("\n\n\n\n\n")


            if self.check():
                if s.mob < self.prediction():
                    # print("move fail! " + str(self.start) + "  doestn't have enough mob to move "+ str(self.amount)+ " " + self.item + " to" + str(self.end))
                    # print("total mob need " + str(self.prediction()) + "\nonly have " + str(s.mob))
                    return False
                else:
                    
                    # print("before mob:" + str(s.mob))
                    s.mob -= self.prediction()
                    itemOutCheck(s, self.item, self.amount)
                    itemChange(s, self.item, -self.amount)
                    itemChange(self.empire['sect'][self.end],self.item,self.amount)
                    # print("move ok! " + str(self.start) + "  "+ str(self.amount)+ " " + self.item + " to" + str(self.end))
                    # print("total mob need " + str(self.prediction()) + "\nleft " + str(s.mob))
                    # print(str(self.start) + " move out " + self.item, self.amount)
                    # print(str(self.end) + " recives "+ self.item, self.amount)
                    # print("after mob: " + str(s.mob))
                    return True
