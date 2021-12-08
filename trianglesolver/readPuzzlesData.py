import os
from Board import *
from puzzle import *

def readPuzzles(name):

    if os.path.exists(name):
        fin = open(name, "r")
        container = []
        rawPuzzle = []

        for l in fin.readlines():
            word = l.replace("\n", "")
            if word == "" or len(word) > 3:
                continue
            if len(word) == 3:
                rawPuzzle.append(word)
            else:
                container.append(word)

        # print(container)
        # print(rawPuzzle)
        board = Board(name, container[0], container[1])
        # print(container[2:])
        board.setBoard(container[2:])
        p = []

        for r in rawPuzzle:
            puzzle = Puzzle(r)
            p.append(puzzle)

        board.setPuzzles(p)
        return board
    else:
        print(f"file Name {name} doesn't exist")
        sys.exit(0)

# readPuzzles()
