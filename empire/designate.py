#!/usr/bin/env python3
from empire import *

class Designate:
    def __init__(self,contain, des=""):
        # print(contain)
        self.empire = contain[0]
        self.sector = contain[1]
        if len(contain) > 2:
            des = contain[2]
        if des != "":
            self.newDes = des
        else:
            self.newDes = contain[2]
            
    def check(self):
        if self.sector not in self.empire['sect']:
            print("designate fail! sector is not vaild")
            return False
        if self.newDes not in sectorTypes:
            print("designate fail! newDesis not vaild")
            return False
        return True

    def act(self):
         if self.check():
            # Not really need more info
            # how eff affects the rebuild
            self.empire['sect'][self.sector].nextDes = self.newDes
            if self.newDes == "c":
                 self.empire['sect'][self.sector].isCap = True