#!/usr/bin/env python3

import sys
import os
import pickle
from PokeBall import *
import random
import time
import math
import itertools
# import threading

goodTeam = []

timeAllowed = 120

fileList = ["data/l.matrix.p", "data/h.matrix.p"]
fileIndex = 0

methods = ["BestNext", "Annealing"]
method = 1

bestNextmany = 50   # best for l is 80

annealingMany = 10  # best for l is 10
top = 10000
tem = 10000
low = 0.1
b = 0.999

rd = 0

if rd == 0:
    rd = True
elif rd == 1:
    rd = False

pokeScore = {}


def read_data(matrix_filename):
    fin = open(matrix_filename, "rb")
    data = pickle.load(fin)
    fin.close()
    return data


def getAll(data_file):
    if not os.path.exists(data_file):
        raise Exception("{} does not exist.".format(data_file))

    data = read_data(data_file)
    names, matrix = data
    ball = PokeBall(names)

    return ball, matrix


def randomStart(all, number=5, old=[]):
    new = random.sample(all, number)
    while new == old:
        new = random.sample(all, number)
    return new


def getTeamScore(matrix, all, team):
    allScore = []

    score = []

    for t in team:
        if t in pokeScore:
            score.append(pokeScore[t])
        else:
            temp = []
            for defender in all:
                key = (t, defender)
                temp.append(matrix[key])
            pokeScore[t] = temp
            score.append(temp)

    # sortedLst = sorted(score)

    for i in range(len(pokeScore[team[0]])):
        bestforthis = 0
        secondBest = 0
        for size in range(len(team)):
            if bestforthis < pokeScore[team[size]][i]:
                secondBest = bestforthis
                bestforthis = pokeScore[team[size]][i]
            elif secondBest < pokeScore[team[size]][i]:
                secondBest = pokeScore[team[size]][i]
        allScore.append((bestforthis + secondBest)/2)

    # print(allScore)

    # allScore.append(sorted(score)[-2])
    """
    for defender in all:
        score = []
        for attacker in team:
            key = (attacker, defender)
            score.append(matrix[key])
        allScore.append(sorted(score)[-2])
    """
    return allScore


def averageTeamScore(matrix, all, team):
    scores = getTeamScore(matrix, all, team)
    return sum(scores) / len(scores)


def isGoodTeam(matrix, all, team):
    score = getTeamScore(matrix, all, team)
    for s in score:
        if s < 500:
            return False
    return True


def winningDiff(scores):
    temp = []
    for s in scores:
        temp.append(s - 500)
    return sum(temp) / len(temp)


def getNeighbors(all, team, many=0):
    neighbors = []
    for i in range(len(team)):
        for poke in all:
            if poke != team[i]:
                temp = team[:]
                temp[i] = poke
                neighbors.append(temp)
    if rd:
        neighbors = random.sample(neighbors, len(neighbors))

    if many == 0 or many > len(neighbors):
        return neighbors
    else:
        return neighbors[:many]


#####################################################################

# Strategy 1: Best of Next neighbors
def bestNextMethod(all, matrix):
    team = randomStart(all)
    oldScore = sum(getTeamScore(matrix, all, team))
    # oldScore = winningDiff(getTeamScore(matrix, all, team))
    improved = True

    many = bestNextmany

    while improved:
        improved = False
        goDown = 0
        for t in getNeighbors(all, team, many):
            if goDown > 7:
                break
            score = sum(getTeamScore(matrix, all, t))
            # score = winningDiff(getTeamScore(matrix, all, t))

            """
            if isGoodTeam(matrix, all, t):
                goodTeam.append(t)
                # print(oldScore, score)

            if score > oldScore:
                team = t
                oldScore = score
                improved = True
                break
           
            """
            good = isGoodTeam(matrix, all, t)
            # print(f"old score: {oldScore} score: {score}")
            if good or score > oldScore:
                if good:
                    goodTeam.append(t)
                team = t
                improved = True
                oldScore = score
                if many < 200:
                    many += 10
                goDown = 0
                break
            goDown += 1

    return team


#####################################################################

# Strategy 2: Simulated Annealing
def annealingMethod(all, matrix):
    team = randomStart(all)
    oldScore = sum(getTeamScore(matrix, all, team))
    # oldScore = winningDiff(getTeamScore(matrix, all, team))

    many = annealingMany

    improved = True

    global tem
    lT = tem

    while improved or lT > low:
        # print(tem)
        improved = False
        for t in getNeighbors(all, team, 9):

            score = sum(getTeamScore(matrix, all, t))
            # score = winningDiff(getTeamScore(matrix, all, t))
            u = score - oldScore
            x = -u / lT

            if isGoodTeam(matrix, all, t):
                goodTeam.append(t)

            # print(x)  # e get way to big
            try:
                ans = math.exp(x)
            except OverflowError:
                break

            if u > 0:
                team = t
                oldScore = score
                improved = True

            elif random.random() <= ans:
                # lT = tem
                team = t
                oldScore = score
                improved = True
        lT *= b
    # print(t)
    return t


#####################################################################


def hillClimb(all, matrix, seconds, method=0):
    start = time.time()
    time.process_time()
    elapsed = 0
    teamList = []
    # counter = 0

    while elapsed < seconds:
        elapsed = time.time() - start
        if method == 0:
            teamList.append(bestNextMethod(all, matrix))
        elif method == 1:
            teamList.append(annealingMethod(all, matrix))

        # counter += 1
        # print(f"method called {counter} times")
    return teamList


def Search():

    print("Total time allowed: " + str(timeAllowed) + " seconds")

    file = fileList[fileIndex]
    print(file)
    print("----")

    ball, matrix = getAll(file)

    print(methods[method])
    if method == 0:
        print(
            f"Best next method will only take the first {bestNextmany} random : {rd} neighbors each time")
    elif method == 1:
        print(
            f"Annealing will only take the first {annealingMany} random : {rd} neighbors each time")
        print(
            f"highest temperature: {top} \nlowest temperature: {low}\nb : {b}")

    teamList = hillClimb(ball.all, matrix, timeAllowed, method)

    lst = []
    print(len(teamList))
    for team in teamList:
        if team not in lst and isGoodTeam(matrix, ball.all, team):
            lst.append(team)
    print(lst)

    print("---Good Team---")
    dic = {}
    for team in goodTeam+lst:
        key = " ".join(team)
        if key not in dic and isGoodTeam(matrix, ball.all, team):
            # print("".join(team))
            dic[key] = winningDiff(
                getTeamScore(matrix, ball.all, team))
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

    if dic == {}:
        print("There is not good team")
    else:
        print(f"good team count: {len(dic.keys())}")
        print("team | the average of (each score - 500)")
        for (team, diffScore) in dic.items():
            print(team + " | " + str(diffScore))


Search()
