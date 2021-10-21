#!/usr/bin/env python3

class Action:
    def __init__(self):
        self.acts = {}

    def checkUpdateinActs(self):
        if "update" in self.acts.keys():
            return True
        return False

    def calCost(self):
        if self.checkUpdateinActs():
            return 1.0
        else:
            counter = 0
            for keyCommand in self.acts:
                for command in self.acts[keyCommand]:
                    counter += 1
            return .01 * counter
    
