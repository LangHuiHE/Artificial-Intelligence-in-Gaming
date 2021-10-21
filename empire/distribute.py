#!/usr/bin/env python3
from empire import *

class Distribute:
    def __init__(self,contain):
        self.empire = contain[0]
        self.pullTo = contain[1]
        self.pullFrom = contain[2]

    def check(self):
        if self.pullTo not in self.empire['sect']:
            print("Distribute fail! pullTo sector is not vaild")
            return False
        if self.pullFrom not in self.empire['sect']:
            print("Distribute fail! pullFrom sector is not vaild")
            return False
        return True

    def act(self):
         if self.check():
            self.empire['sect'][self.pullTo].dst = self.pullFrom
            # print(str(self.empire['sect'][self.pullTo],location) + "will pull stuff from" + str(self.empire['sect'][self.pullTo].dst))