#!/usr/bin/env python3

class PokeBall:
    def __init__(self, names=[]):
        self.all = []
        if names != []:
            self.all = names
    
    def addPokemon(self, name):
        self.all.append(name)