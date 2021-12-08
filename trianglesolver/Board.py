from math import fabs
import sys

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

mattchingDic = {}
for i in range(len(ascii_lowercase)):
    mattchingDic[ascii_lowercase[i]] = ascii_uppercase[i]
    mattchingDic[ascii_uppercase[i]] = ascii_lowercase[i]

# print(mattchingDic)


class Board:
    def __init__(self, name, row, animals) -> None:
        self.name = name
        self.row = int(row)
        self.animals = int(animals)

    def setBoard(self, patten):
        sides = {'left': [], 'right': [], 'bottom': []}

        for i in range(self.row):
            sides['left'].append(patten[i])

        for i in range(self.row, self.row*2):
            sides['right'].append(patten[i])

        for i in range(self.row*2, self.row*3):
            sides['bottom'].append(patten[i])

        self.board = sides

    def setPuzzles(self, puzzles):
        self.puzzles = puzzles

    def printBoard(self):
        print(f"name:{self.name}")
        print(f"row:{self.row}")
        print(f"animals:{self.animals}")
        print(f"board:{self.board}")
        if self.puzzles == None:
            print(f"puzzles: None")
        else:
            i = 1
            for p in self.puzzles:
                print(f"puzzle_{i}:{p.patten}")
                i += 1

    def getConflictCount(self):
        count = 0

        # leftBottonIndex = len(self.puzzles) - 1 - (self.row - 1) * 2
        # print(leftBottonIndex)

        # top first one
        if self.puzzles[0].patten[0] != mattchingDic[self.board['left'][0]]:
            count += 1
        if self.puzzles[0].patten[1] != mattchingDic[self.board['right'][0]]:
            count += 1
        if self.puzzles[0].patten[2] != mattchingDic[self.puzzles[2].patten[1]]:
            count += 1

        # # right-bottom last one
        # if self.puzzles[-1].patten[1] != mattchingDic[self.board['right'][-1]]:
        #     count += 1
        # if self.puzzles[-1].patten[2] != mattchingDic[self.board['bottom'][-1]]:
        #     count += 1
        # if self.puzzles[-1].patten[0] != mattchingDic[self.puzzles[-2].patten[2]]:
        #     count += 1

        # # reft-bottom last - (row-1)* 2
        # if self.puzzles[leftBottonIndex].patten[0] != mattchingDic[self.board['left'][-1]]:
        #     count += 1
        # if self.puzzles[leftBottonIndex].patten[2] != mattchingDic[self.board['bottom'][0]]:
        #     count += 1
        # if self.puzzles[leftBottonIndex].patten[1] != mattchingDic[self.puzzles[leftBottonIndex+1].patten[0]]:
        #     count += 1

        # row 2 1
        if self.puzzles[1].patten[0] != mattchingDic[self.board['left'][1]]:
            count += 1
        if self.puzzles[1].patten[1] != mattchingDic[self.puzzles[2].patten[0]]:
            count += 1
        if self.puzzles[1].patten[2] != mattchingDic[self.puzzles[5].patten[1]]:
            count += 1

        # row 2 2
        if self.puzzles[2].patten[0] != mattchingDic[self.puzzles[1].patten[1]]:
            count += 1
        if self.puzzles[2].patten[1] != mattchingDic[self.puzzles[0].patten[2]]:
            count += 1
        if self.puzzles[2].patten[2] != mattchingDic[self.puzzles[3].patten[0]]:
            count += 1

        # row 2 3
        if self.puzzles[3].patten[0] != mattchingDic[self.puzzles[2].patten[2]]:
            count += 1
        if self.puzzles[3].patten[1] != mattchingDic[self.board["right"][1]]:
            count += 1
        if self.puzzles[3].patten[2] != mattchingDic[self.puzzles[7].patten[1]]:
            count += 1

        if self.row == 3:
            # row 3- 0 bottom left
            if self.puzzles[4].patten[0] != mattchingDic[self.board["left"][2]]:
                count += 1
            if self.puzzles[4].patten[1] != mattchingDic[self.puzzles[5].patten[0]]:
                count += 1
            if self.puzzles[4].patten[2] != mattchingDic[self.board['bottom'][0]]:
                count += 1

            # row 3 -1
            if self.puzzles[5].patten[0] != mattchingDic[self.puzzles[4].patten[1]]:
                count += 1
            if self.puzzles[5].patten[1] != mattchingDic[self.puzzles[1].patten[2]]:
                count += 1
            if self.puzzles[5].patten[2] != mattchingDic[self.puzzles[6].patten[0]]:
                count += 1

            # row 3 2
            if self.puzzles[6].patten[0] != mattchingDic[self.puzzles[5].patten[2]]:
                count += 1
            if self.puzzles[6].patten[1] != mattchingDic[self.puzzles[7].patten[0]]:
                count += 1
            if self.puzzles[6].patten[2] != mattchingDic[self.board["bottom"][1]]:
                count += 1

            # row 3 3
            if self.puzzles[7].patten[0] != mattchingDic[self.puzzles[6].patten[1]]:
                count += 1
            if self.puzzles[7].patten[1] != mattchingDic[self.puzzles[3].patten[2]]:
                count += 1
            if self.puzzles[7].patten[2] != mattchingDic[self.puzzles[8].patten[0]]:
                count += 1

            # row 3 4 right bottom conner
            if self.puzzles[8].patten[0] != mattchingDic[self.puzzles[7].patten[2]]:
                count += 1
            if self.puzzles[8].patten[1] != mattchingDic[self.board['right'][2]]:
                count += 1
            if self.puzzles[8].patten[2] != mattchingDic[self.board['bottom'][2]]:
                count += 1

        elif self.row == 4:
            # row 3- 0
            if self.puzzles[4].patten[0] != mattchingDic[self.board['left'][2]]:
                count += 1
            if self.puzzles[4].patten[1] != mattchingDic[self.puzzles[5].patten[0]]:
                count += 1
            if self.puzzles[4].patten[2] != mattchingDic[self.puzzles[10].patten[1]]:
                count += 1

            # row 3 -1
            if self.puzzles[5].patten[0] != mattchingDic[self.puzzles[4].patten[1]]:
                count += 1
            if self.puzzles[5].patten[1] != mattchingDic[self.puzzles[1].patten[2]]:
                count += 1
            if self.puzzles[5].patten[2] != mattchingDic[self.puzzles[6].patten[0]]:
                count += 1

            # row 3 2
            if self.puzzles[6].patten[0] != mattchingDic[self.puzzles[5].patten[2]]:
                count += 1
            if self.puzzles[6].patten[1] != mattchingDic[self.puzzles[7].patten[0]]:
                count += 1
            if self.puzzles[6].patten[2] != mattchingDic[self.puzzles[12].patten[1]]:
                count += 1

            # row 3 3
            if self.puzzles[7].patten[0] != mattchingDic[self.puzzles[6].patten[1]]:
                count += 1
            if self.puzzles[7].patten[1] != mattchingDic[self.puzzles[3].patten[2]]:
                count += 1
            if self.puzzles[7].patten[2] != mattchingDic[self.puzzles[8].patten[0]]:
                count += 1

            # row 3 4
            if self.puzzles[8].patten[0] != mattchingDic[self.puzzles[7].patten[2]]:
                count += 1
            if self.puzzles[8].patten[1] != mattchingDic[self.board['right'][2]]:
                count += 1
            if self.puzzles[8].patten[2] != mattchingDic[self.puzzles[14].patten[1]]:
                count += 1

            # row 4 0 bottom left conner
            if self.puzzles[9].patten[0] != mattchingDic[self.board['left'][3]]:
                count += 1
            if self.puzzles[9].patten[1] != mattchingDic[self.puzzles[10].patten[0]]:
                count += 1
            if self.puzzles[9].patten[2] != mattchingDic[self.board['bottom'][0]]:
                count += 1

            # row 4 1
            if self.puzzles[10].patten[0] != mattchingDic[self.puzzles[9].patten[1]]:
                count += 1
            if self.puzzles[10].patten[1] != mattchingDic[self.puzzles[4].patten[2]]:
                count += 1
            if self.puzzles[10].patten[2] != mattchingDic[self.puzzles[11].patten[0]]:
                count += 1

            # row 4 2
            if self.puzzles[11].patten[0] != mattchingDic[self.puzzles[10].patten[2]]:
                count += 1
            if self.puzzles[11].patten[1] != mattchingDic[self.puzzles[12].patten[0]]:
                count += 1
            if self.puzzles[11].patten[2] != mattchingDic[self.board['bottom'][1]]:
                count += 1

            # row 4 3
            if self.puzzles[12].patten[0] != mattchingDic[self.puzzles[11].patten[1]]:
                count += 1
            if self.puzzles[12].patten[1] != mattchingDic[self.puzzles[6].patten[2]]:
                count += 1
            if self.puzzles[12].patten[2] != mattchingDic[self.puzzles[13].patten[0]]:
                count += 1

            # row 4 4
            if self.puzzles[13].patten[0] != mattchingDic[self.puzzles[12].patten[2]]:
                count += 1
            if self.puzzles[13].patten[1] != mattchingDic[self.puzzles[14].patten[0]]:
                count += 1
            if self.puzzles[13].patten[2] != mattchingDic[self.board['bottom'][2]]:
                count += 1

            # row 4 5
            if self.puzzles[14].patten[0] != mattchingDic[self.puzzles[13].patten[1]]:
                count += 1
            if self.puzzles[14].patten[1] != mattchingDic[self.puzzles[8].patten[2]]:
                count += 1
            if self.puzzles[14].patten[2] != mattchingDic[self.puzzles[15].patten[0]]:
                count += 1

            # row 4 6 bottom right conner
            if self.puzzles[15].patten[0] != mattchingDic[self.puzzles[14].patten[2]]:
                count += 1
            if self.puzzles[15].patten[1] != mattchingDic[self.board['right'][3]]:
                count += 1
            if self.puzzles[15].patten[2] != mattchingDic[self.board['bottom'][3]]:
                count += 1

        return count


# somthing is wrong for getCOnflictInfo()

    def getConflictInfo(self):
        infoLst = []

        leftBottonIndex = len(self.puzzles) - 1 - (self.row - 1) * 2
        # if test[0].direction == "down" or test[-1].direction == "down" or test[leftBottonIndex].direction == "down":
        # return False

        # top first one
        if self.puzzles[0].patten[0] != mattchingDic[self.board['left'][0]] or self.puzzles[0].patten[1] != mattchingDic[self.board['right'][0]] or self.puzzles[0].patten[2] != mattchingDic[self.puzzles[2].patten[1]]:
            infoLst.append("topFirst")

        # right-bottom last one
        if self.puzzles[-1].patten[1] != mattchingDic[self.board['right'][-1]] or self.puzzles[-1].patten[2] != mattchingDic[self.board['bottom'][-1]] or self.puzzles[-1].patten[0] != mattchingDic[self.puzzles[-2].patten[2]]:
            infoLst.append("right-bottom")

        # left-bottom last - (row-1)* 2
        if self.puzzles[leftBottonIndex].patten[0] != mattchingDic[self.board['left'][-1]] or self.puzzles[leftBottonIndex].patten[2] != mattchingDic[self.board['bottom'][0]] or self.puzzles[leftBottonIndex].patten[1] != mattchingDic[self.puzzles[leftBottonIndex+1].patten[0]]:
            infoLst.append("left-bottom")

        # row 2 1
        if self.puzzles[1].patten[0] != mattchingDic[self.board['left'][1]] or self.puzzles[1].patten[1] != mattchingDic[self.puzzles[2].patten[0]] or self.puzzles[1].patten[2] != mattchingDic[self.puzzles[5].patten[1]]:
            infoLst.append("row 2 1")
        # row 2 2
        # no need to check the middle one
        # row 2 3
        if self.puzzles[3].patten[0] != mattchingDic[self.puzzles[2].patten[2]] or self.puzzles[3].patten[1] != mattchingDic[self.board["right"][1]] or self.puzzles[3].patten[2] != mattchingDic[self.puzzles[7].patten[1]]:
            infoLst.append("row 2 3")

        if self.row == 3:
            # row 3- 0 bottom left check before
            # row 3 -1 skip
            # row 3 2
            if self.puzzles[6].patten[0] != mattchingDic[self.puzzles[5].patten[2]] or self.puzzles[6].patten[2] != mattchingDic[self.board["bottom"][1]] or self.puzzles[6].patten[1] != mattchingDic[self.puzzles[7].patten[0]]:
                infoLst.append("row 3 2")
            # row 3 3 skip
            # row 3 4 right bottom conner

        elif self.row == 4:
            # row 3- 0
            if self.puzzles[3].patten[0] != mattchingDic[self.board['left'[2]]] or self.puzzles[4].patten[1] != mattchingDic[self.puzzles[5].patten[0]] or self.puzzles[4].patten[2] != mattchingDic[self.puzzles[10].patten[1]]:
                infoLst.append("row 3 0")
            # row 3 -1 skip
            # row 3 2
            if self.puzzles[6].patten[0] != mattchingDic[self.puzzles[5].patten[2]] or self.puzzles[6].patten[2] != mattchingDic[self.puzzles[12].patten[1]] or self.puzzles[6].patten[1] != mattchingDic[self.puzzles[7].patten[0]]:
                infoLst.append("row 3 2")
            # row 3 3 skip
            # row 3 4
            if self.puzzles[8].patten[0] != mattchingDic[self.puzzles[7].patten[2]] or self.puzzles[8].patten[1] != mattchingDic[self.board['right'][2]] or self.puzzles[8].patten[2] != mattchingDic[self.puzzles[14].patten[1]]:
                infoLst.append("row 3 4")

            # row 4 0 bottom left conner
            # row 4 1 skip
            # row 4 2
            if self.puzzles[11].patten[0] != mattchingDic[self.puzzles[10].patten[2]] or self.puzzles[11].patten[1] != mattchingDic[self.puzzles[12].patten[0]] or self.puzzles[11].patten[2] != mattchingDic[self.board['bottom'][1]]:
                infoLst.append("row 4 2")
            # row 4 3 skip
            # row 4 4
            if self.puzzles[13].patten[0] != mattchingDic[self.puzzles[12].patten[2]] or self.puzzles[13].patten[1] != mattchingDic[self.puzzles[14].patten[0]] or self.puzzles[13].patten[2] != mattchingDic[self.board['bottom'][2]]:
                infoLst.append("row 4 4")
            # row 4 5 skip
            # row 4 6 bottom right conner
        return infoLst

    def tryPuzzleInSpot(self, puzzles, index):
        if index == 0:
            if puzzles[0].patten[0] != mattchingDic[self.board['left'][0]] or puzzles[0].patten[1] != mattchingDic[self.board['right'][0]]:
                return False
        elif index == 1:
            if puzzles[1].patten[0] != mattchingDic[self.board['left'][1]]:
                return False
        elif index == 2:
            if puzzles[2].patten[0] != mattchingDic[puzzles[1].patten[1]] and puzzles[2].patten[1] != mattchingDic[puzzles[0].patten[2]]:
                return False
        elif index == 3:
            if puzzles[3].patten[0] != mattchingDic[puzzles[2].patten[2]] and puzzles[3].patten[1] != mattchingDic[self.board["right"][1]]:
                return False

        elif self.row == 3:
            if index == 4:
                if puzzles[4].patten[0] != mattchingDic[self.board["left"][2]] and puzzles[4].patten[2] != mattchingDic[self.board['bottom'][0]]:
                    return False
            elif index == 5:
                if puzzles[5].patten[0] != mattchingDic[puzzles[4].patten[1]] and puzzles[5].patten[1] != mattchingDic[puzzles[1].patten[2]]:
                    return False
            elif index == 6:
                if puzzles[6].patten[0] != mattchingDic[puzzles[5].patten[2]] and puzzles[6].patten[2] != mattchingDic[self.board["bottom"][1]]:
                    return False
            elif index == 7:
                if puzzles[7].patten[0] != mattchingDic[puzzles[6].patten[1]] and puzzles[7].patten[1] != mattchingDic[puzzles[3].patten[2]]:
                    return False
            elif index == 8:
                if puzzles[8].patten[0] != mattchingDic[puzzles[7].patten[2]] and puzzles[8].patten[1] != mattchingDic[self.board['right'][2]] and puzzles[8].patten[2] != mattchingDic[self.board['bottom'][2]]:
                    return False

        elif self.row == 4:
            if index == 4:
                if puzzles[4].patten[0] != mattchingDic[self.board['left'][2]]:
                    return False
            elif index == 5:
                if puzzles[5].patten[0] != mattchingDic[puzzles[4].patten[1]] and puzzles[5].patten[1] != mattchingDic[puzzles[1].patten[2]]:
                    return False
            elif index == 6:
                if puzzles[6].patten[0] != mattchingDic[puzzles[5].patten[2]]:
                    return False
            elif index == 7:
                if puzzles[7].patten[0] != mattchingDic[puzzles[6].patten[1]] and puzzles[7].patten[1] != mattchingDic[puzzles[3].patten[2]]:
                    return False
            elif index == 8:
                if puzzles[8].patten[0] != mattchingDic[puzzles[7].patten[2]] and puzzles[8].patten[1] != mattchingDic[self.board['right'][2]]:
                    return False
            elif index == 9:
                if puzzles[9].patten[0] != mattchingDic[self.board['left'][3]] and puzzles[9].patten[2] != mattchingDic[self.board['bottom'][0]]:
                    return False
            elif index == 10:
                if puzzles[10].patten[0] != mattchingDic[puzzles[9].patten[1]] and puzzles[10].patten[1] != mattchingDic[puzzles[4].patten[2]]:
                    return False
            elif index == 11:
                if puzzles[11].patten[0] != mattchingDic[puzzles[10].patten[2]] and puzzles[11].patten[2] != mattchingDic[self.board['bottom'][1]]:
                    return False
            elif index == 12:
                if puzzles[12].patten[0] != mattchingDic[puzzles[11].patten[1]] and puzzles[12].patten[1] != mattchingDic[puzzles[6].patten[2]]:
                    return False
            elif index == 13:
                if puzzles[13].patten[0] != mattchingDic[puzzles[12].patten[2]] and puzzles[13].patten[2] != mattchingDic[self.board['bottom'][2]]:
                    return False
            elif index == 14:
                if puzzles[14].patten[0] != mattchingDic[puzzles[13].patten[1]] and puzzles[14].patten[1] != mattchingDic[puzzles[8].patten[2]]:
                    return False
            elif index == 15:
                if puzzles[15].patten[0] != mattchingDic[puzzles[14].patten[2]] and puzzles[15].patten[1] != mattchingDic[self.board['right'][3]] and puzzles[15].patten[2] != mattchingDic[self.board['bottom'][3]]:
                    return False

        return True
