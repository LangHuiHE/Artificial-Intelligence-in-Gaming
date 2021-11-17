# !/usr/bin/python3
from os import stat
from readMain import *
from State import *
from Result import *
import copy
import random
import time

#####################################################################
# Strategy 1: Best Next location

def nextClosest(start, exclusion=[]):
    temp = {}
    for n in start.map.keys():
        if n not in exclusion:
            temp[n] = start.map[n]
    
    name = min(temp, key=temp.get)
    return (name, temp[name])

def findCityInCitiesByName(cities, cityName):
    for c in cities:
        if c.name == cityName:
            return c

    print("Can't find City :" + cityName)
    return None


def bestNext(cities):
    """
    for i in range(size):
        path = [cities[i]]
        exclusion= [cities[i].name]

        while len(path) < len(cities):
            # start = cities[i]
            nextName = nextClosest(path[len(path)-1], exclusion)
            exclusion.append(nextName)
            path.append(findCityInCitiesByName(cities, nextName))

        state = State(path)
        cost = state.calculateCost()
        if cost in result.track:
            if path != result.track[cost]:
                result.track[cost].append(path)
        else:
            result.track[cost] = [path]
    """
    start = random.choice(cities)
    path = [start]
    exclusion= [start.name]
    cost = 0
    while len(path) < len(cities):
        # start = cities[i]
        nextName, toNextdist = nextClosest(path[len(path)-1], exclusion)
        exclusion.append(nextName)
        path.append(findCityInCitiesByName(cities, nextName))
        cost += toNextdist
        # print(toNextdist,cost)

    
    exclusion.append(start.name)
    path.append(start)
    cost += path[len(path)-2].map[start.name]

    state = State(path)
    stateCost =  state.calculateCost()
    if cost != stateCost:
        print(cost, stateCost)

    return (cost, exclusion)

def bestNextMethod(result, cities, seconds):
    start = time.time()
    time.process_time()
    elapsed = 0

    while elapsed < seconds:
        elapsed = time.time() - start
                
        cost, path = bestNext(cities)
        if result.track["l"] == -1 or result.track["l"] > cost:
            result.track["l"] = cost
            result.track['path'] = path
        elif result.track["h"] < cost:
            result.track["h"] = cost
   


#####################################################################
# Strategy 2: Best of all neighbors
def bestNextMethod(result, cities, seconds):
    start = time.time()
    time.process_time()
    elapsed = 0

    while elapsed < seconds:
        elapsed = time.time() - start
                
        cost, path = bestNext(cities)
        if result.track["l"] == -1 or result.track["l"] > cost:
            result.track["l"] = cost
            result.track['path'] = path
        elif result.track["h"] < cost:
            result.track["h"] = cost

#####################################################################

def checkData():
    sum = 0
    x = "0 99 71 23 33 47 32 32 55 6 7 20 7 20 76 45 8 44 30 79 22 21 25 92 48 57 17 6 7 81 24 2 55 73 45 16 22 44 16 47 6 26 42 51 39 0 25 31 34 44 25 49 11 0 13 12 64 79 0 12 113 26 104 20 31 17 61 32 18 27 73 34 10 20 2 35 15 17 35 74 21 8 70 27 80 24 17 95 9 57 137 34 1 49 38 35 19 37 98 44 23 35 1 55 63 43 1 37 18 40 21 9 44 79 80 63 116 59 114 57 5 72 51 87 38 44 74 10 75 19 12 38 15 39 105 7 27 57 5 17 15 6 60 24 5 76 43 53 50 35 39 9 25 53 12 48 23 83 35 13 65 48 93 33 50 17 4 6 18 103 11 65 24 2 24 5 49 13 15 5 86 3 25 70 37 11 35 46 22 46 28 2 55 22 11 46 20 100 67 39 15 38 42 24 70 3 34 64 8 13 23 1 28 8 39 43 63 10 53 68 78 93 38 13 22 12 43 18 73 32 89 8 39 6 17 11 14 5 30 28 96 44 33 14 7 69 25 59 37 8 54 41 61 16 18 6 44 28 56 82 100 74 31 22 30 63 75 12 34 10 59 7 12 5 42 34 62 14 33 39 14 4 35 12 85 45 37 50 30 86 70 72 109 12 1 17 56 47 60 67 8 27 56 62 4 13 19 20 78 70 51 15 30 7 35 47 85 11 40 70 36 70 24 11 1 43 3 82 75 53 20 26 32 37 71 1 20 86 56 32 27 50 66 18 3 8 9 52 53 19 16 41 58 24 10 31 0 30 24 69 14 14 15 16 22 1 9 4 47 31 38 5 10 35 5 9 20 26 39 101 26 94 122 53 21 38 55 64 52 89 44 34 63 39 60 15 30 51 79 50 27 52 28 37 91 47 26 6 29 0 79 24 54 8 1 67 43 37 41 95 50 43 136 89 7 28 2 21 65 13 43 85 81 68 116 5 49 19 76 2 1 4 54 25 43 16 25 24 57 34 38 58 19 18 54 29 16 68 37 34 15 40 1 57 37 17 6 93 66 80 15 15 0 95 24 5 31 17 15 69 4 58 26 31 0 37 91 15 15 66 26 59 33 23 118 52 8 26 68 64 83 15 91 82 92 62 24 42 56 26 27 17 55 1 87 50 14 9 45 7 60 71 0 28 28 43 75 129 86 54 56 84 69 66 10 59 36 14 88 68 46 24 5 90 24 40 31 8 39 15 13 3 81 6 21 12 3 68 58 55 28 28 45 8 3 40 88 65 13 89 12 15 43 5 8 4 30 37 34 95 54 37 66 80 76 62 21 35 27 99 16 53 34 14 89 94 51 71 16 30 0 26 67 87 36 36 18 32 64 18 86 36 21 30 28 54 85 32 42 4 72 23 21 89 35 9 55 2 66 56 12 60 33 36 49 45 89 15 0 29 100 16 26 30 74 13 5 14 22 31 34 29 30 33 32 73 68 32 40 34 45 40 9 65 67 76 49 15 18 9 26 13 84 31 33 12 11 114 24 10 14 2 4 26 5 66 26 47 103 12 2 71 111 38 35 0 11 21 26 39 47 60 49 1 18 40 59 2 89 34 7 31 7 34 1 66 6 28 0 29 30 79 82 94 2 117 13 72 47 13 19 1 34 3 37 31 86 48 33 85 14 23 50 9 17 22 30 58 51 15 41 10 8 17 71 19 13 76 5 13 102 17 51 104 72 43 6 76 31 37 29 54 56 16 63 27 61 17 88 66 10 36 58 13 17 10 37 36 14 23 76 18 15 135 29 9 19 53 1 72 26 27 1 36 49 46 87 25 22 3 60 0 3 68 9 61 35 45 69 79 93 2 15 0 9 12 104 29 62 4 103 93 48 4 9 12 38 74 19 98 44 9 10 18 56 28 54 16 56 8 40 10 15 49 20 61 5 19 19 8 38 69 14 28 98 27 58 41 64 56 51 12 10 27 21 42 16 28 18 9 5 86 69 19 11 11 38 70 19 8 41 15 19 57 117 27 69 105 24 35 3 22 44 20 22 19 57 20 107 7 47 26 6 65 56 39 74 23 2 30 6 72 15 25 51 82 1 17 16 17 58 21 30 38 30 55 50 18 16 15 90 3 1 16 11 3 72 40 25 33 22 34 56 42 71 61 58 52 15 95 77 74 29 28 14 44 4 33 15 45 76 93 34 59 58 79 16 1 71 116 8 44 52 27 70 14 17 61 41 65 13 44 30 85 36 58 78 39 76 59 103 5 106 14 11 11 6 99 26 0 64 8 74 37 83 8 2 36 33 33 60 92 25 24"
    lst = x.split()
    test = []
    for s in lst:
        sum += int(s)
        test.append(int(s))
    print(sum) 

    # result = Result()
    cities = read(filesList[11])
    i = 0
    for name in cities[0].map.keys():
        if cities[0].map[name] != int(lst[i]):
            print("fail " + name)
        i += 1
    print(i)

#####################################################################
# Strategy 3: single swipe OR Best-first neighbor?
def neighbors(state, improvedCounter, method=0):
    lst = []

    if method == 0: # single swipe
        j, k = 0, 0
        while j == k:
            j = random.randint(1, len(state.cities)-2)
            k = random.randint(1, len(state.cities)-2)
        state.cities[j], state.cities[k] =  state.cities[k], state.cities[j]
        lst.append(state)


    elif method == 1: # double swipe
        while state.cities == state.cities:
            j, k = 0, 0
            while j == k:
                j = random.randint(1, len(state.cities)-2)
                k = random.randint(1, len(state.cities)-2)
            state.cities[j], state.cities[k] =  state.cities[k], state.cities[j]
            while j == k:
                j = random.randint(1, len(state.cities)-2)
                k = random.randint(1, len(state.cities)-2)
            state.cities[j], state.cities[k] =  state.cities[k], state.cities[j]
        lst.append(state)

    return lst

def swipe(cities, improvedCounter):
    s = State(cities)
    u = s.calculateCost()
    improved = True
    oldImprovedCounter = improvedCounter
    while improved:
        # print(improvedCounter, u)
        improved = False
        for n in neighbors(s, improvedCounter, 0):
            cost = n.calculateCost()
            if  cost > u:
                u = cost
                s = n
                improved = True
                improvedCounter += 1
    if improvedCounter == oldImprovedCounter:
        improvedCounter -= 1
    return s,u, improvedCounter

def randomCities(cities):
    l = copy.deepcopy(cities)
    random.shuffle(l)
    return l

def swipeMethod(result, cities, seconds):
    temp = randomCities(cities)
    temp.append(temp[0])

    start = time.time()
    time.process_time()
    elapsed = 0

    lastEla = 0
    improvedCounter = 0

    while elapsed < seconds:
        
        elapsed = time.time() - start
        
        if elapsed - lastEla < 13 and improvedCounter < 5:
            temp = randomCities(temp)
            temp.append(temp[0])
            lastEla = elapsed
            improvedCounter = 0

        if elapsed - lastEla >= 15 and improvedCounter > (elapsed - lastEla) * 1.2:
            improvedCounter += 2
        
        s, u, improvedCounter = swipe(temp, improvedCounter)
        

    result.track["l"] = u
    result.track["path"] = s.getPath()

#####################################################################

filesList = [
    "uk12_main.txt",       #0
    "sgb128_main.txt",     #1
    "barsoom128_main.txt", #2
    "barsoom129_main.txt", #3
    "barsoom130_main.txt", #4
    "barsoom256_main.txt", #5
    "barsoom257_main.txt", #6
    "barsoom258_main.txt", #7
    "barsoom512_main.txt", #8
    "barsoom513_main.txt", #9
    "barsoom514_main.txt", #10
    "barsoom1024_main.txt" #11
]

#####################################################################

def Search():
    # checkData()
    # only for the barsoom128_main.txt

    seconds = 120
    print("Total time allowed: " + str(seconds) + " seconds")

    fileIndex = 0
    file = filesList[fileIndex]
    print(file)
    cities = read(file)

    print("Utility/Score is calculated by the sum of total distance traveling")
    print("The lower number is the better")

    # for i in range(12):
        # print(cities[i].map)

    result = Result()
    result.track["h"] = 0
    result.track['l'] = -1
    result.track['path'] = []
    swipeMethod(result, cities, seconds)
    print(result.track)

    print("\nYou can CONTROL+C to forced stop the program\n")
    print("\nNow start using the best next/closest city as next city")
    result.track["h"] = 0
    result.track['l'] = -1
    result.track['path'] = []
    bestNextMethod(result, cities, seconds)
    print(result.track)
    
Search()