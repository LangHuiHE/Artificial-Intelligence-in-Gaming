#!/usr/bin/env python3
from Action import *
from State import *
from update import *
from empire import *
import sys
import os
import pickle

# importing copy module
import copy

sourceName = "empire.p"
outputfile = "command.text"

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
        
        print("search is done!")
        
        if os.path.exists(outputfile):
            os.remove(outputfile)
        
        output =  open(outputfile, "w")

        command = []

        while state.parentState != None:
            print(state.actions.__dict__)
            state = state.parentState

        for line in command:
            output.writelines(line + "\n")
           

        output.close()

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
    state = State(None, empire,None)

    lst = []

    lst.append(state)

    while lst != []:
        state = popLowestPathCost(lst)
        lst.remove(state)

        print(len(lst))

        if state.isGoalState():
            print(state.__dict__)
            print(state.actions.__dict__)
            break
            
        else:
            actionS = ActionS(state)
            for a in actionS:
                for i in a.values():
                    if i.acts.values != []:
                        nextS = Result(state, i)
                        lst.append(nextS)
            """
            print("##################################")
            for i in lst:
                print(i)
                print("-")
            """

    return state

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

    """
    print("---\nv")
    for a in actionS:
        print(a['a1'].__dict__)
    print("^\n---")
    """

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
    print(action.__dict__)
    next = State(copy.deepcopy(s1), temp.empire, action)
    
    return next


main()
