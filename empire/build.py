#!/usr/bin/env python3
from pickle import APPEND
from empire import *

class Build:
    def __init__(self,contain):
        self.empire = contain[0]
        self.sector = contain[1]

    def check(self):
        if self.sector not in self.empire['sect']:
            print("Build fail! sector is not vaild")
            return False
        return True

    def buildFishBoatCheck(self):
        #                           lcm hcm avail tech $
        # fb   fishing boat          25  15    75    0 $180
        s = self.empire['sect'][self.sector]
        if s.des != 'h':
            print("you only able to build a in harbors")
            return False
        if s.lcm < 25:
            print("you have to have at least 25 lcm")
            return False
        if s.hcm < 15:
            print("you have to have at least 15 hcm")
            return False
        if s.avail < 75:
            print("you have to have at least 75 avail")
            return False
        # skip money part
        
        return True
    
    def buildFishingBoat(self):
        if self.buildFishBoatCheck():
            habor = self.empire['sect'][self.sector]
            habor.lcm -= 25
            habor.hcm -= 15
            habor.avail -= 75
            print("build a new fishing boat")

            words = ["1", str(habor.countryNumber), str(habor.location[0]), str(habor.location[1]), "0"]
            for i in range (24):
                words.append("1")
            words.append("shouble be return")
            words.append("")
            words.append("")
            self.empire['ship'] = {1 : Ship(words)}
            return True
        return False
        
    def act(self):
        if self.check():
            self.buildFishingBoat()