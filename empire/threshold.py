#!/usr/bin/env python3
from empire import *

class Threshold:
    def __init__(self,contain):
        self.empire = contain[0]
        self.sector = contain[1]
        self.item = contain[2]
        self.quantity = contain[3]

    def check(self):
        if self.sector not in self.empire['sect']:
            print("Threshold fail! sector is not vaild")
            return False
        if self.item not in itemLst:
            print("Threshold fail! item is not vaild")
            return False
        return True

    def doThreshold(self):
        s = self.empire['sect'][self.sector]
        if self.item == "civ":
            s.c_dist = self.quantity
        elif self.item == "min":
            s.m_dist = self.quantity
        elif self.item == "gold":
            s.g_dist = self.quantity
        elif self.item == "shell":
            s.s_dist = self.quantity
        elif self.item == "petrol":
            s.p_dist = self.quantity 
        elif self.item == "iron":
            s.i_dist = self.quantity
        elif self.item == "dust":
            s.d_dist = self.quantity  
        elif self.item == "bar":
            s.b_dist = self.quantity
        elif self.item == "food":
            s.f_dist = self.quantity
        elif self.item == "oil":
            s.o_dist = self.quantity                                                           
        elif self.item == "lcm":
            s.l_dist = self.quantity
        elif self.item == "hcm":
            s.h_dist = self.quantity 
        elif self.item == "uw":
            s.u_dist = self.quantity                  
        elif self.item == "rad":
            s.r_dist = self.quantity
        else:
            print("unvaild item" + self.item)
            
    def act(self):
        if self.check():
            self.doThreshold()