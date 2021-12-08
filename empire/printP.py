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
            if t == "extra":
                print(empire[t].__dict__)
            else:
                for location in empire[t]:
                    print(empire[t][location].__dict__)   
        
    else:
        sys.exit(1)

main()