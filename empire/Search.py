#!/usr/bin/env python3
from Action import *
from State import *
from update import *
from empire import *
import sys
import os
import pickle

sourceName = "empire.p"

def main():
    if os.path.exists(sourceName):
        fin = open(sourceName, "rb")
        empire = pickle.load(fin)
        # for location in sectors:
            # print(sectors[location].__dict__)
        fin.close()
        
        if empire == {}:
            print("can't load the empire object!")
            sys.exit(1)
        
        print("start search!")
        state = search(empire)
        print("search done!")
        print(state.__dict__)

    else: 
        print("file doesn't exist!")
        sys.exit(1)

def popLowestPathCost(lst):
    lowest = lst[0]
    for i in lst:
        if lowest.pathCost > i.pathCost:
            lowest = i
    return lowest

def search(empire):
    initState = State(None, empire,None)

    lst = []

    lst.append(initState)

    while lst != []:
        state = popLowestPathCost(lst)
        lst.remove(state)

        if Goal(state):
            return state
        else:
            actionS = ActionS(state)
            for a in actionS:
                for i in a.values():
                    # print(i.acts)
                    if i.acts.values != []:
                        nextS = Result(state, i)
                        lst.append(nextS)
            """
            print("##################################")
            for i in lst:
                print(i)
                print("-")
            """

# create a list of possible Actions to take in State s
def ActionS(s):
    actionS = []
    # Designate all sectors
    actionS.append(s.des())
    # Spread out population and food.
    actionS.append(s.spread())
    # Adjust distribution network
    actionS.append(s.adjustDist())
    # Build
    actionS.append(s.build())
    # Update
    actionS.append(s.update())

    
    print("---\nv")
    for a in actionS:
        print(a['a1'].__dict__)
    print("^\n---")
    

    return actionS

# create a new State object s2, with Action a
def Result(s1, action):
    temp = Update([s1.currentEmpire])

    for keyCommand in action.acts:
        for command in action.acts[keyCommand]:
            if action.acts[keyCommand] != []:
                # print(keyCommand)
                # print(command)
                temp.handle(keyCommand, command)
    
    return State(s1, temp.empire, action)


def Goal(s):
    nation = s.currentEmpire

    if len(nation['sect']) < 10:
        return False

    for loca in nation['sect']:
        sect = nation['sect'][loca]
        if sect.civ != 1000:
            return False
    
    if len(nation['ship']) < 1:
        return False

    for loca in nation['ship']:
        ship = nation['ship'][loca]
        if ship.type == 0:
            return True
    
    return False


main()
