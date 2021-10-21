#!/usr/bin/env python3
import sys
import os
import pickle
from empire import *

def main():
    if os.path.exists("empire.p"):
        fin = open("empire.p", "rb")
        empire = pickle.load(fin)
        fin.close()

        if empire == {}:
            print("can't load the empire object!")
            sys.exit(1)

        for t in empire:
            for location in empire[t]:
                print(empire[t][location].__dict__)  
        print("-----") 

        empire['ship'] = []
        
        lst = []
        for loca in empire['sect']:
            if empire["sect"][loca].countryNumber != 37:
                lst.append(loca)
        
        for loca in lst:
            del empire['sect'][loca]

        for loca in empire['sect']:
            empire["sect"][loca].des = "c"
            empire["sect"][loca].civ = 200
            empire["sect"][loca].food = 200
            empire["sect"][loca].iron = 0
            empire["sect"][loca].lcm = 0
            empire["sect"][loca].hcm = 0
            empire["sect"][loca].nextDes = ""
            empire["sect"][loca].dst = loca
            empire["sect"][loca].c_dist = 0
            empire["sect"][loca].m_dist = 0
            empire["sect"][loca].g_dist = 0
            empire["sect"][loca].s_dist = 0 
            empire["sect"][loca].p_dist = 0 
            empire["sect"][loca].i_dist = 0
            empire["sect"][loca].d_dist = 0  
            empire["sect"][loca].b_dist = 0
            empire["sect"][loca].f_dist = 0
            empire["sect"][loca].o_dist = 0                                                           
            empire["sect"][loca].l_dist = 0
            empire["sect"][loca].h_dist = 0 
            empire["sect"][loca].u_dist = 0                  
            empire["sect"][loca].r_dist = 0

            empire["sect"][loca].money = 100
            empire["sect"][loca].isCap = False
        
        for t in empire:
            for location in empire[t]:
                print(empire[t][location].__dict__)   

        fout = open("empire.p", "wb")
        pickle.dump(empire,fout)
        fout.close()
        
    else:
        sys.exit(1)


main()