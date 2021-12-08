import os
import math
from readPuzzlesData import *
import time
from State import *
import copy
import random

################################################

timeLimit = 120
row = 4
animals = "05"
pI = "02"
overrideName = f"puzzle-{str(row)}-{animals}-{pI}"
# print(overrideName)
method = "annealing"
# method = "bfs"

################################################


def randomStart(board):
    # if board.row == 3:
    #     lst = random.choices(board.puzzles, k=6)
    # elif board.row == 4:
    #     lst = random.choices(board.puzzles, k=10)
    # for p in lst:
    # p.rotate()
    random.choices(board.puzzles, k=len(board.puzzles))
    return board


def getNeighbor(state):
    lst = []

    tempLst = []
    # swipe two puzzles loop over get all the combination
    for j in range(len(state.board.puzzles)):
        for k in range(len(state.board.puzzles)):
            key = (min(j, k), max(j, k))
            if j != k and key not in tempLst:
                tempLst.append(key)
                s1 = copy.deepcopy(state)
                s1.board.puzzles[j], s1.board.puzzles[k] = s1.board.puzzles[k], s1.board.puzzles[j]
                lst.append(s1)
    # print(tempLst)
    # print(len(lst))

    # rotate oen puzzle
    # which one
    for j in range(len(state.board.puzzles)):
        for i in range(1, 3):
            s2 = copy.deepcopy(state)
            # how rotate time 1 to 2
            s2.board.puzzles[j].rotate(i)
            lst.append(s2)

    # print(len(lst))

    random.shuffle(lst)
    return lst


def localSearchHillClimbing(board):
    start = time.time()
    time.process_time()
    elapsed = 0

    copyBoard = copy.deepcopy(board)
    state = State(randomStart(copyBoard))
    # print(s.board)
    oldCount = state.board.getConflictCount()
    q = [state]

    lowestCount = oldCount
    bestState = state

    gettingWorse = 0

    while elapsed < timeLimit:
        elapsed = time.time() - start
        state = q.pop()
        # for nextS in getNeighbor(state):
        nextS = random.choice(getNeighbor(state))
        newCount = nextS.board.getConflictCount()
        if newCount == 0:
            break
        if newCount <= oldCount:
            gettingWorse = 0
            q.append(nextS)
            state = nextS
            oldCount = newCount
            if lowestCount > newCount:
                lowestCount = newCount
                bestState = nextS

        # print(f"conflict count {newCount}")

        if gettingWorse > 6:
            # print(f"restart from bestState {lowestCount}")
            s = State(randomStart(copy.deepcopy(bestState).board))
            oldCount = s.board.getConflictCount()
            q = [s]
            gettingWorse = 0
        else:
            gettingWorse += 1
        if q == []:
            # print("ran out of states")
            s = State(randomStart(copy.deepcopy(bestState).board))
            oldCount = s.board.getConflictCount()
            q = [s]
            # gettingWorse = 0

    if newCount > lowestCount:
        nextS = bestState
        newCount = lowestCount
    return nextS, newCount


def temperature(fraction):
    """ Example of temperature dicreasing as the process goes on."""
    return max(0.01, min(1, 1 - fraction))


top = 10000
tem = 10000
low = 0.1
b = 0.9999


def localSearchAnnealing(board):
    start = time.time()
    time.process_time()
    elapsed = 0

    copyBoard = copy.deepcopy(board)
    state = State(randomStart(copyBoard))
    # print(s.board)
    oldCount = state.board.getConflictCount()

    # lowestCount = oldCount
    bestState = state

    global tem
    lT = tem

    while elapsed < timeLimit:
        # while True:
        improved = True
        elapsed = time.time() - start

        while improved or lT > low:
            improved = False

            neighbors = getNeighbor(state)[:9]

            for i in range(len(neighbors)):
                # fraction = i / float(10)
                # t = temperature(fraction)

                nextS = neighbors[i]

                newCount = nextS.board.getConflictCount()

                if newCount == 0:
                    print(f"***  found the solution! for {board.name}  ***")
                    return nextS, newCount

                u = newCount - oldCount
                x = -u / lT

                try:
                    ans = math.exp(x)
                except OverflowError:
                    break

                if u < 0:
                    state = nextS
                    oldCount = newCount
                    improved = True

                    # if lowestCount > newCount:
                    #     lowestCount = newCount
                    #     bestState = nextS

                elif round(random.uniform(0, 1), 10) < ans:
                    state = nextS
                    oldCount = newCount
                    improved = True

                    # if lowestCount > newCount:
                    #    lowestCount = newCount
                    #     bestState = nextS

                # print(f"conflict count  {lT} {oldCount} {newCount}")

            lT *= b

        state = State(randomStart(bestState.board))
        # print(s.board)
        # oldCount = lowestCount
        lT = tem

    # if newCount > lowestCount:
        # return bestState, lowestCount
    # else:
    return nextS, newCount

# idkkkkkkkkkkkkkk


def dfs(board):
    start = time.time()
    time.process_time()
    elapsed = 0

    while elapsed < timeLimit:
        elapsed = time.time() - start

        s = State(randomStart(copy.deepcopy(board)))
        count = s.board.getConflictCount()

        if count == 0:
            return s, count
        q = [s]

        while q != []:
            nextS = q.pop()
            if len(nextS.solving) != len(nextS.board.puzzles):

                noUsed = []
                for p in nextS.board.puzzles:
                    if p not in nextS.solving:
                        noUsed.append(p)

                for p in noUsed:
                    for rotate in range(0, 3):
                        rp = copy.deepcopy(p)
                        rp.rotate(rotate)

                        pLst = nextS.solving[:] + [rp]

                        # print(len(nextS.solving))

                        if nextS.board.tryPuzzleInSpot(pLst, len(nextS.solving)):
                            replicatedState = copy.deepcopy(nextS)
                            replicatedState.solving.append(rp)
                            q.append(replicatedState)

            count = nextS.board.getConflictCount()
            if len(nextS.solving) == len(nextS.board.puzzles) and count == 0:
                nextS.board.puzzles = nextS.solving
                return nextS, count

    return None, -1


def bfs(board):
    start = time.time()
    time.process_time()
    elapsed = 0

    while elapsed < timeLimit:
        elapsed = time.time() - start

        s = State(randomStart(copy.deepcopy(board)))
        count = s.board.getConflictCount()

        if count == 0:
            return s, count
        q = [s]

        while q != []:
            nextS = q.pop()
            if len(nextS.solving) != len(nextS.board.puzzles):

                noUsed = []
                for p in nextS.board.puzzles:
                    if p not in nextS.solving:
                        noUsed.append(p)

                for p in noUsed:
                    for rotate in range(0, 3):
                        rp = copy.deepcopy(p)
                        rp.rotate(rotate)

                        pLst = nextS.solving[:] + [rp]

                        # print(len(nextS.solving))

                        if nextS.board.tryPuzzleInSpot(pLst, len(nextS.solving)):
                            replicatedState = copy.deepcopy(nextS)
                            replicatedState.solving.append(rp)
                            q.append(replicatedState)

            count = nextS.board.getConflictCount()
            if len(nextS.solving) == len(nextS.board.puzzles) and count == 0:
                nextS.board.puzzles = nextS.solving
                return nextS, count

    return None, -1


def Search():
    solved = {}
    path = "puzzles"

    # path += f"/{row}"

    # for final
    path += "/exam-puzzles-2021"

    # iterate through all file
    if overrideName == "":
        for fileName in os.listdir(path):
            filePath = os.path.join(path, fileName)
            board = readPuzzles(filePath)
            board.printBoard()
            solved[board.name] = None

            # s, conflictCount = localSearchHillClimbing(board)
            if method == "annealing":
                s, conflictCount = localSearchAnnealing(board)
            elif method == "bfs":
                s, conflictCount = bfs(board)
            else:
                print(f"doesn't support mehtod {method}")
                sys.exit(0)

            if conflictCount == 0:
                solved[board.name] = s.board
            else:
                print("-------")
                print(f"conflictCount : {conflictCount}")
                # print(s.board.printBoard())
    else:
        filePath = os.path.join(path, overrideName)
        board = readPuzzles(filePath)
        board.printBoard()
        solved[board.name] = None

        # s, conflictCount = localSearchHillClimbing(board)
        if method == "annealing":
            s, conflictCount = localSearchAnnealing(board)
        elif method == "bfs":
            s, conflictCount = bfs(board)
        else:
            print(f"doesn't support mehtod {method}")
            sys.exit(0)

        if conflictCount == 0:
            solved[board.name] = s.board
        else:
            print("-------")
            print(f"conflictCount : {conflictCount}")
            print(s.board.printBoard())

    print("-------")

    for n in solved.keys():
        if solved[n] != None:
            solved[n].printBoard()
        else:
            print(f"{n} : {solved[n]}")


Search()
