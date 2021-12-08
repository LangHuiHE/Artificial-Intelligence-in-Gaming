#!/usr/bin/env python3
from move import *
from designate import *
from distribute import *
from threshold import *
from build import *
from empire import *

class Update:
    def __init__(self,contain):
        self.empire = contain[0]
        self.sectors = self.empire['sect']
        self.ships = self.empire['ship']

    def handle(self, keyCommand, contain, action=True):
        # print(contain)

        """
        workforce = (civ*work/100 + uw + mil * 0.4) / 100.
        If workforce = 0 go away and don't update anything
        """
        if action == True:
            # print("do action")
            self.action(keyCommand,contain)
        else:
            print("do prediction AKA calculation")
            self.prediction(keyCommand,contain)

    def prediction(self,keyCommand, contain):

        if keyCommand == "move":
            print(Move([self.empire] + contain, False, True).prediction())

        elif keyCommand == "designate":
            print(Designate([self.empire] + contain))

        elif keyCommand == "distribute":
            print(Distribute([self.empire] + contain))

        elif keyCommand == "threshold":
            print(Threshold([self.empire] + contain))

        elif keyCommand == "build":
            print(Build([self.empire] + contain))

        elif keyCommand == "capital":
            print(Designate([self.empire] + contain, "c"))

        elif keyCommand == "update":
            if contain[0] == "*":
                for loca in self.sectors:
                    target = self.sectors[loca]
                    workforce = (target.civ * target.work / 100 + target.uw + target.mil * 0.4) / 100
                    if workforce > 0:
                        print(self.pre(target))
                    else:
                        print("sector " + target.location + "have 0 workforce")
            else:
                target = self.sectors[contain[0]]
                workforce = (target.civ * target.work / 100 + target.uw + target.mil * 0.4) / 100
                if workforce > 0:
                        print(self.pre(target))
                else:
                    print("sector " + target.location + "have 0 workforce")
               

    def pre(self, target):
        print(target.calculateTaxes())
        print(target.calculateFoodCost())
        print(target.calculatePopulationGrow())
        print(target.calculateMaintain())
        print(target.calculateProduction())
        print(target.calculateBuilding())
        print(self.calculateDistribution())


    def action(self,keyCommand, contain):
        if keyCommand == "move":
            Move([self.empire] + contain, False, True).act()

        elif keyCommand == "designate":
            Designate([self.empire] + contain).act()

        elif keyCommand == "distribute":
            Distribute([self.empire] + contain).act()

        elif keyCommand == "threshold":
            Threshold([self.empire] + contain).act()

        elif keyCommand == "build":
            Build([self.empire] + contain).act()

        elif keyCommand == "capital":
            Designate([self.empire] + contain).act()

        elif keyCommand == "update":
            if contain[0] == "*":

                """
                print("brefore Update:")
                for loca in self.sectors:
                    target = self.sectors[loca]
                    print(target.__dict__)
                    print()
                """

                for loca in self.sectors:
                    target = self.sectors[loca]

                    if target.des == "h":
                        self.empire['extra'].haborLoca = target.location
                    if target.nextDes == "h":
                        self.empire['extra'].nexthHaborLoca = target.location

                    #print("Taxes")
                    target.updateTaxes()
                    # print("---")
                    #print("feed")
                    target.feed()
                    # print("---")
                    #print("PopulationGrow")
                    target.updatePopulationGrow()
                    # print("---")
                    #print("Maintain")
                    target.updateMaintain()
                    # print("---")
                    #print("Production")
                    target.updateProduction()
                    # print("---")
                    #print("Building")
                    target.updateBuilding()
                    # print("---")

                              
                print("bf dist:") 
                for loca in self.sectors:
                    target = self.sectors[loca]
                    print(target.__dict__)
                    print()

                print("Distribution")
                
                self.distribution()
                
                print("\n\n\n\nafter Distribution:") 
                for loca in self.sectors:
                    target = self.sectors[loca]
                    print(target.__dict__)
                    print("")
                print("\n\n\n\n")
                
                for loca in self.sectors:
                    target = self.sectors[loca]
                    # print("---")
                    #print("Mob")
                    target.updateMob()
                    # print("---")
                    #print("Des")
                    target.updateDes()

                self.empire['extra'].capLoca = self.empire['extra'].nextCapLoca
                self.empire['extra'].haborLoca = self.empire['extra'].nexthHaborLoca

                
                print("\n\n\n\n\n\n\nafter Update:") 
                for loca in self.sectors:
                    target = self.sectors[loca]
                    print(target.__dict__)
                    print()
                print("\n\n\n\n\n\n\n") 
                
                

            else:
                target = self.sectors[contain[0]]
                print("brefore Update:")
                print(target.__dict__)
                print()

                print("Taxes")
                target.updateTaxes()
                # print("---")
                print("feed")
                target.feed()
                # print("---")
                print("PopulationGrow")
                target.updatePopulationGrow()
                # print("---")
                print("Maintain")
                target.updateMaintain()
                # print("---")
                print("Production")
                target.updateProduction()
                # print("---")
                print("Building")
                target.updateBuilding()
                # print("---")
                    
                print("Distribution")
                self.distribution()

                # print("---")
                print("Mob")
                target.updateMob()
                # print("---")
                print("Des")
                target.updateDes()
            

                """
                print("after Update:")
                print(target.__dict__)
                print()
                """

    """
    def act(self, target):
        # UDPATE every in the sector like the telegram
        
        info update-sequence

        eat food first

        population

        ship maintenance

        sector maintenance

        production

        ship building

        distribution-> push stuff first (what above the line) -> distribution to each sector (lower the line)
        (x1y1 to x2y2
         | y(2-1) | + | x(2-1)| / 2)

        updateMob 
        


        # print("Update!!!")
        print("Taxes")
        target.updateTaxes()
        # print("---")
        print("feed")
        target.feed()
        # print("---")
        print("PopulationGrow")
        target.updatePopulationGrow()
        # print("---")
        print("Maintain")
        target.updateMaintain()
        # print("---")
        print("Production")
        target.updateProduction()
        # print("---")
        print("Building")
        target.updateBuilding()
        # print("---")
        print("Distribution")
        self.distribution()
        # print("---")
        print("Mob")
        target.updateMob()
        # print("---")
        print("Des")
        target.updateDes()

    """

    
    def makeContainForDist(self, sector, on_hand, dist, contain, push=True):
        
        if push == True:
            # push stuff to harbor
            contain[1] = sector.location
            contain[3] = 0
            contain[4] = sector.dst
            # print(on_hand)
            if on_hand > dist:
                # have too much need to send habor
                contain[3] = int(on_hand - dist)
            
        else:
            # pull
            # send out thing
            # harbor = self.sectors[self.empire['extra'].harborLoca]

            contain[1] = sector.dst
            contain[3] = 0
            contain[4] = sector.location
            if dist - on_hand > 0:
                # need stuff from habor
                amount = int(dist - on_hand)
        
                contain[3] = int(dist - on_hand)
            
        """
        if self.empire['extra'].haborLoca == sector.location:
            # send stuff to habor
            if on_hand > dist:
                contain[1] = sector.location
                contain[3] = int((on_hand - dist))
                contain[4] = sector.dst
        
        if self.empire['extra'].haborLoca == sector.location:

        if on_hand < dist:
            contain[1] = sector.dst
            contain[3] = int(dist - on_hand)
            contain[4] = sector.location
        else:
            contain[1] = sector.location
            contain[3] = int((on_hand - dist))
            contain[4] = sector.dst
        """

        if sector.dst == sector.location or contain[3] < 0:
            contain[3] = 0

        # print(contain[3])
            
        if contain[3] > 200:
            contain[3] = 100
            
        return contain

    def distribution(self):
    # collect things:
        for loca in self.sectors:
            s = self.sectors[loca]
            contain = [self.empire, (),"", 0, ()]  
            """
            hasMore = [self.empire, s.location,"", 0, s.dst]
            lessThan = [self.empire, s.dst, "", 0, s.location]
            """
            if s.f_dist != s.food and s.f_dist != 0:
                contain[2] = "food"
                contain = self.makeContainForDist(s, s.food, s.f_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1
    
            if s.civ != s.c_dist and s.c_dist != 0:
                contain[2] = "civ"
                contain = self.makeContainForDist(s, s.civ, s.c_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1:
                        contain[3] -= 1

            if s.m_dist != s.mil and s.m_dist != 0:
                contain[2] = "mil"
                contain = self.makeContainForDist(s, s.mil, s.m_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.s_dist != s.shell and s.s_dist != 0:
                contain[2] = "shell"
                contain = self.makeContainForDist(s, s.shell, s.s_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.g_dist != s.gun and s.g_dist != 0:
                contain[2] = "gun"
                contain = self.makeContainForDist(s, s.gun, s.g_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.p_dist != s.petrol and s.p_dist != 0:
                contain[2] = "petrol"
                contain = self.makeContainForDist(s, s.petrol, s.p_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.i_dist != s.iron and s.i_dist != 0:
                contain[2] = "iron"
                contain = self.makeContainForDist(s, s.iron, s.i_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.d_dist != s.dust and s.d_dist != 0:
                contain[2] = "dust"
                contain = self.makeContainForDist(s, s.dust, s.d_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.b_dist != s.bar and s.b_dist != 0:
                contain[2] = "bar"
                contain = self.makeContainForDist(s, s.bar, s.b_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.o_dist != s.oil and s.o_dist != 0:
                contain[2] = "oil"
                contain = self.makeContainForDist(s, s.oil, s.o_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.l_dist != s.lcm and s.l_dist != 0:
                contain[2] = "lcm"
                contain = self.makeContainForDist(s, s.lcm, s.l_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.h_dist != s.hcm and s.h_dist != 0:
                contain[2] = "hcm"
                contain = self.makeContainForDist(s, s.hcm, s.h_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.u_dist != s.uw and s.u_dist != 0:
                contain[2] = "uw"
                contain = self.makeContainForDist(s, s.uw, s.u_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

            if s.r_dist != s.rad and s.r_dist != 0:
                contain[2] = "rad"
                contain = self.makeContainForDist(s, s.rad, s.r_dist, contain)
                if contain[3] != 0 and contain[1] == s.location:
                    while Move(contain, True).act() != True and contain[3] > 1: 
                        contain[3] -= 1

        # middle ground:
        """
        print("\n\n\n0000000000000")
        for loca in self.sectors:
            sector = self.sectors[loca]
            print(sector.__dict__)
        print("0000000000000\n\n\n")
        """

        # Send out things

        for loca in self.sectors:
            if self.sectors[loca].des != 'h':
                s = self.sectors[loca]
                contain = [self.empire, (),"", 0, ()]  
                """
                hasMore = [self.empire, s.location,"", 0, s.dst]
                lessThan = [self.empire, s.dst, "", 0, s.location]
                """
                if s.f_dist != s.food and s.f_dist != 0:
                    contain[2] = "food"
                    contain = self.makeContainForDist(s, s.food, s.f_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.civ != s.c_dist and s.c_dist != 0:
                    contain[2] = "civ"
                    contain = self.makeContainForDist(s, s.civ, s.c_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.m_dist != s.mil and s.m_dist != 0:
                    contain[2] = "mil"
                    contain = self.makeContainForDist(s, s.mil, s.m_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.s_dist != s.shell and s.s_dist != 0:
                    contain[2] = "shell"
                    contain = self.makeContainForDist(s, s.shell, s.s_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.g_dist != s.gun and s.g_dist != 0:
                    contain[2] = "gun"
                    contain = self.makeContainForDist(s, s.gun, s.g_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.p_dist != s.petrol and s.p_dist != 0:
                    contain[2] = "petrol"
                    contain = self.makeContainForDist(s, s.petrol, s.p_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.i_dist != s.iron and s.i_dist != 0:
                    contain[2] = "iron"
                    contain = self.makeContainForDist(s, s.iron, s.i_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.d_dist != s.dust and s.d_dist != 0:
                    contain[2] = "dust"
                    contain = self.makeContainForDist(s, s.dust, s.d_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.b_dist != s.bar and s.b_dist != 0:
                    contain[2] = "bar"
                    contain = self.makeContainForDist(s, s.bar, s.b_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.o_dist != s.oil and s.o_dist != 0:
                    contain[2] = "oil"
                    contain = self.makeContainForDist(s, s.oil, s.o_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.l_dist != s.lcm and s.l_dist != 0:
                    contain[2] = "lcm"
                    contain = self.makeContainForDist(s, s.lcm, s.l_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.h_dist != s.hcm and s.h_dist != 0:
                    contain[2] = "hcm"
                    contain = self.makeContainForDist(s, s.hcm, s.h_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.u_dist != s.uw and s.u_dist != 0:
                    contain[2] = "uw"
                    contain = self.makeContainForDist(s, s.uw, s.u_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

                if s.r_dist != s.rad and s.r_dist != 0:
                    contain[2] = "rad"
                    contain = self.makeContainForDist(s, s.rad, s.r_dist, contain, False)
                    if contain[3] != 0:
                        while Move(contain, True).act() != True and contain[3] > 1: 
                            contain[3] -= 1

        
    def calculateDistribution(self):
        for loca in self.sectors:
            s = self.sectors[loca]

            contain = [self.empire, (),"", 0, ()]  
            """
            hasMore = [self.empire, s.location,"", 0, s.dst]
            lessThan = [self.empire, s.dst, "", 0, s.location]
            """
            if s.civ != s.c_dist and s.c_dist != 0:
                contain[2] = "civ"
                contain = self.makeContainForDist(s, s.civ, s.c_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()
                
            if s.m_dist != s.mil and s.m_dist != 0:
                contain[2] = "mil"
                Move(contain, True).prediction()
                contain = self.makeContainForDist(s, s.mil, s.m_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.s_dist != s.shell and s.s_dist != 0:
                contain[2] = "shell"
                contain = self.makeContainForDist(s, s.shell, s.s_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.g_dist != s.gun and s.g_dist != 0:
                contain[2] = "gun"
                contain = self.makeContainForDist(s, s.gun, s.g_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.p_dist != s.petrol and s.p_dist != 0:
                contain[2] = "petrol"
                contain = self.makeContainForDist(s, s.petrol, s.p_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.i_dist != s.iron and s.i_dist != 0:
                contain[2] = "iron"
                contain = self.makeContainForDist(s, s.iron, s.i_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.d_dist != s.dust and s.d_dist != 0:
                contain[2] = "dust"
                contain = self.makeContainForDist(s, s.dust, s.d_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.b_dist != s.bar and s.b_dist != 0:
                contain[2] = "bar"
                contain = self.makeContainForDist(s, s.bar, s.b_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.f_dist != s.food and s.f_dist != 0:
                contain[2] = "food"
                contain = self.makeContainForDist(s, s.food, s.f_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.o_dist != s.oil and s.o_dist != 0:
                contain[2] = "oil"
                contain = self.makeContainForDist(s, s.oil, s.o_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()
                    
            if s.l_dist != s.lcm and s.l_dist != 0:
                contain[2] = "lcm"
                contain = self.makeContainForDist(s, s.lcm, s.l_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.h_dist != s.hcm and s.h_dist != 0:
                contain[2] = "hcm"
                contain = self.makeContainForDist(s, s.hcm, s.h_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.u_dist != s.uw and s.u_dist != 0:
                contain[2] = "uw"
                contain = self.makeContainForDist(s, s.uw, s.u_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()

            if s.r_dist != s.rad and s.r_dist != 0:
                contain[2] = "rad"
                contain = self.makeContainForDist(s, s.rad, s.r_dist, contain)
                if contain[3] != 0:
                    Move(contain, True).prediction()
