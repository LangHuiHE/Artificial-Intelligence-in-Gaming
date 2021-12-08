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
outputfile = "command.txt"

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

        if empire['sect'] == {}:
            print("there is not sect!")
            sys.exit(1)
        
        print("start search!")

        state = search(empire)
 
        print("search is done!")
        
        if os.path.exists(outputfile):
            os.remove(outputfile)
        
        output =  open(outputfile, "w")

        lst = []

        while state.parentState != None:
            for keyCommand in state.actions.acts:
                command = state.actions.acts[keyCommand]
                pair = [(keyCommand, command)]
                lst = pair + lst

            # print(state.actions.acts)
            state = state.parentState

        # print(lst)

        formatedCommandLst = CommandFormater(lst)

        for line in formatedCommandLst:
            if line == "------------------------\n":
                break
                # print("here is the update line ------")
            if "build" in line:
                print("IT IS THE TIME!")
            line.replace("(", "")
            line.replace(")", "")

            print(line)

            output.writelines(line)
           

        output.close()

    else: 
        print("file doesn't exist!")
        sys.exit(1)

def CommandFormater(lst):
    outPut = []
    for pair in lst:
        keyCommnad = pair[0]
        command = pair[1]
        if command != []:
            for subCommand in command:
                if keyCommnad == 'update':
                    outPut.append("------------------------\n")
                elif keyCommnad == 'build':
                    outPut.append("build ship " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + " fb \n")
                elif keyCommnad == "distribute":
                    outPut.append(keyCommnad + " " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + " " + str(subCommand[1][0]) + "," +  str(subCommand[1][1]) + "\n")
                elif keyCommnad == "designate":
                    outPut.append(keyCommnad + " " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + " " + str(subCommand[1]) + "\n")
                elif keyCommnad == "capital":
                    outPut.append("designate" + " " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + " " + str(subCommand[1]) + "\n")
                    outPut.append(keyCommnad + " " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + "\n")
                elif keyCommnad == "threshold":
                    outPut.append(keyCommnad + " " + str(subCommand[1]) + " " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + " " + str(subCommand[2])+ "\n")
                elif keyCommnad == "move":
                    # print(subCommand)
                    """
                    move item source_location amount destination_location|path :
                    move amount of item from source location to destination location, or using path
                    e.g. mov civ 0,0 10 -2,0
                    """
                    outPut.append(keyCommnad + " " + str(subCommand[1]) + " " + str(subCommand[0][0]) + "," +  str(subCommand[0][1]) + " " + str(subCommand[2]) + " " + str(subCommand[3][0]) + "," +  str(subCommand[3][1]) + "\n")          
                    
    out = []

    for line in outPut:
        nl = str(line)
        nl.replace("(", "")
        nl.replace(")", "")
        out.append(nl)
     
    return out


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
        # print(len(lst))
        state = popLowestPathCost(lst)
        lst.remove(state)

        # print(len(lst))

        if state.isGoalState():
            break
            
        else:

            for loca in state.currentEmpire['sect']:
                # if state.actions != None:
                    # print(state.actions.acts)
                print(state.currentEmpire['sect'][loca].__dict__)
            print(state.currentEmpire['extra'].__dict__)
            print("-----\n\n\n\n\n\n\n\n")
       

            actionS = ActionS(copy.deepcopy(state))
            newStateLst = [state]  # all possible states after update

            for a in actionS:
                for logic in actionS[a]:
                    i = actionS[a][logic]
                    # print(i.__dict__)
                    if i != None:
                        tempLst = []
                        for each in newStateLst:
                            tempState = Result(each, i)
                            tempLst.append(tempState)
                        newStateLst = tempLst
            lst += newStateLst

    return state

# create a dict of possible Actions to take in State s
def ActionS(s):
    actionS = {}
    # Designate all sectors
    actionS['des'] = s.des()
    # Spread out population and food.
    actionS['spread'] = s.spread()

    # after move the state empire should be updated!
    """
    for loca in s.currentEmpire['sect']:
        print("after move the state empire should be updated!")
        print(s.currentEmpire['sect'][loca].__dict__)

    print("####")
    """
    # Adjust distribution network
    actionS['adjustDist'] = s.adjustDist()
    # Build`
    actionS['build'] = s.build()
    # Update
    actionS['update'] = s.update()

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

    if "move" in action.acts: # do move first
         for command in action.acts["move"]:
                if action.acts["move"] != []:
                    # print(keyCommand)
                    # print(command)
                    temp.handle("move", command)
    
    for keyCommand in action.acts:
        if keyCommand != "move": #skip move because it alreadly did or excute
            for command in action.acts[keyCommand]:
                if action.acts[keyCommand] != []:
                    # print(keyCommand)
                    # print(command)
                    temp.handle(keyCommand, command)

    # print(action.__dict__)
    next = State(copy.deepcopy(s1), copy.deepcopy(temp.empire), action)
    # print(next.__dict__)
    return next


main()
