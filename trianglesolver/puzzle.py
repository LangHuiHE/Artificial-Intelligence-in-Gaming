import sys


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


class Puzzle:
    def __init__(self, patten) -> None:
        self.patten = Convert(patten)
        # no direction need bc the puzzle has three sides and hard code to check direction
        # when it comes to put together

    def rotate(self, n):
        self.patten = self.patten[n:] + self.patten[:n]
