#!/usr/bin/env python3
import sys
import os
import pickle
from empire import *
from update import *

sourceName = "empire.p"
saveName = "prediction.p"

# empire : { dataType : { location : sector }}

#gEmpire = {}

commandlst = ['move', 'designate', 'distribute', 'threshold', 'build', 'captial', "update","override","*"]

def main():
    if os.path.exists(sourceName):
        fin = open(sourceName, "rb")
        global gEmpire 
        gEmpire = pickle.load(fin)
        # for location in sectors:
            # print(sectors[location].__dict__)
        fin.close()
        
        if gEmpire == {}:
            print("can't load the empire object!")
            sys.exit(1)
        
        while True:
            line = input("command?")
            line = line.strip()
            line = line.lower()
            words = line.split()
            if len(words) > 0:
                handler(words)
    else: 
        print("file doesn't exist!")
        sys.exit(1)

def handler(words):
        """
        - move
        - designate
        - distribute
        - threshold
        - build ship

        - capital
        - UPDATE
        - others as needed
        commandlst = ['move', 'designate', 'distribute', 'threshold', 'captial']
        """

        keyCommand = words[0]
        temp = Update([gEmpire])

        if keyCommand == "move":
            contain = [(0,0),"food", 100, "gh"]
            temp.handle("move",contain)
        elif keyCommand in lazyCommandCollection("designate", 3):
            contain = [(1,-1), "a"]
            temp.handle("designate",contain)
        elif keyCommand in lazyCommandCollection("distribute", 4):
            contain = [(1,-1), (2,0)]
            temp.handle("distribute",contain)
        elif keyCommand in lazyCommandCollection("threshold", 6):
            contain = [(1,-1), "food", 5000]
            temp.handle("threshold",contain)
        elif keyCommand == "build":
            if words[1] == "ship" :
                contain = [(1,-1)]
                temp.handle("Build",contain)
        elif keyCommand in lazyCommandCollection("capital", 3):
            contain = [(3,3)]
            temp.handle("Build",contain)
        elif keyCommand == "update":
            if len(words) < 2 or words[1] == "*" :
                temp.handle("update",["*"])
            else:
                # need to supply specific sector location, current default (0,0)
                temp.handle("update",[(0,0)])
        elif keyCommand == "override":
            print("current temp empire and all the commands saved to " + saveName)

            fout = open(saveName, "wb")
            pickle.dump(temp,fout)
            fout.close()

        if keyCommand in ["help", "info"]:
            commandInfo(words) 
        elif keyCommand in lazyCommandCollection("print", 3):
            commandPrintEmpire()
        elif keyCommand in lazyCommandCollection("quit", 1) or keyCommand in lazyCommandCollection("bye", 2) or keyCommand in lazyCommandCollection('exit', 2):
            print("bye!")
            sys.exit(0)

def lazyCommandCollection(word, size):
    lst = []
    while len(word) >= size:
        lst.append(word)
        word = word[:-1]
    return lst

def commandInfo(words):

    if len(words) < 2 or words[1] == "*":
        for command in commandlst:
            printInfo(command)
    else :
        printInfo(words[1])



def printInfo(keyWord):
    print(keyWord)
    if keyWord == "move":
        print("move | from(sector) | item | quantity | path")
    elif keyWord in lazyCommandCollection("designate", 3):
        print("designate | sector | designate")
    elif keyWord in lazyCommandCollection("distribute", 4):
        print("distribute | sector | from which sector")
    elif keyWord in lazyCommandCollection("threshold", 6):
        print("threshold | sector | item | quantity")
    elif keyWord == "build":
        print("build ship | sector | ship tyep")
    elif keyWord in lazyCommandCollection("captial", 3):
        print("captial | sector")
    elif keyWord == "update":
        print("update just a update")
    elif keyWord == "override":
        print("current temp empire and all the commands will be saved to " + saveName)
    elif keyWord == "*":
        print("print out all the sub topics")
    else:
        print("I don't understand" + keyWord)
        print("this is all the supoorted command")
        print(commandlst)
    print("---")

def commandPrintEmpire():
    print(" Sectors:")
    for location in gEmpire["sect"]:
        print(gEmpire["sect"][location].__dict__)
    print("------------------------")
    print(" Ships::")
    for location in gEmpire["ship"]:
        print(gEmpire["ship"][location].__dict__)
    print("------------------------")

main()
