#!/usr/bin/env python3
import sys
import os
import pickle
from datetime import datetime
from empire import *
#
# empire : { dataType : { location : sector }}

if os.path.exists("empire.p"):
    fin = open("empire.p", "rb")
    empire = pickle.load(fin)
    fin.close()
else:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    # print("Current Time =", current_time)
    empire = {"sect":{},"ship":{}}

dataType = ""

for line in sys.stdin.readlines():
    line = line.strip()
    words = line.split()

    if words[0] in ("xdump", "XDUMP"):
        if words[1] == "sect":
            dataType = words[1]
        elif words[1] == "ship":
            dataType = words[1]
        continue
   
    if len(words) < 16:
        continue
    
    if dataType == "":
        print("missing dataType exit!")
        sys.exit(1)
    
    if dataType == "sect":
        location = (int(words[1]), int(words[2]))
        temp = Sector(words)
        empire[dataType][location] = temp
    elif dataType == "ship":
        temp = Ship(words)
        uID = words[0]
        empire[dataType][uID] = temp
    

for t in empire:
    for location in empire[t]:
        print(empire[t][location].__dict__)

fout = open("empire.p", "wb")
pickle.dump(empire,fout)
fout.close()
