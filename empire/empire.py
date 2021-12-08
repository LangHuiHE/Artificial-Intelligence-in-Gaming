#!/usr/bin/env python3


global empire
gEmpire = {}
global itemLst
itemLst = ["min", "gold", "oil", "uran", "civ", "mil", "shell", "gun", "petrol", "iron", "dust", "bar", "food", "lcm", "hcm", "uw", "rad"]
global moveDirection 
moveDirection = ["j","g","y","u","b","n", "h"]
global sectorTypes
sectorTypes = ["b","h","m","a","c","j","k","u","p","i","g"]
global mapDirection
mapDirection ="     y u\n   g      j\n     b n"
global sectMaximunMob
sectMaximunMob = 127
global sectMaxGainMob
sectMaxGainMob = 60
global obrate
obrate = .03
global babyeat
babyeat = 0.00005
global etu
etu = 10
global civtaxrate
civtaxrate = 1
global uwtaxrate
uwtaxrate = 0.1
global milpayrate
milpayrate = 5
global bankint
bankint = 12
global government_salaries
government_salaries = 1
global tlev
tlev = 5
global unit_maintenance
unit_maintenance = 340
global sect_maintenance
sect_maintenance = 60
global ship_maintenance
ship_maintenance = 250
global money
money = 100
global bwork
bwork = 100

class Extra:
    def __init__(self, words):
        self.haborLoca = words[0]
        self.nexthHaborLoca = words[1]
        self.capLoca = words[2]
        self.nextCapLoca = words[3]

# empire : { dataType : { location : sector }}

class Sector:
    def __init__(self, words):
        self.countryNumber = int(words[0])
        self.location = (int(words[1]),int(words[2]))

        if words[3] == '5':
            self.des = "c"
        elif words[3] == '10':
            self.des = "m"
        elif words[3] == "12":
            self.des = "h"            
        elif words[3] == '15':
            self.des = "a"
        elif words[3] == '17':
            self.des = "j"
        elif words[3] == '18':
            self.des = "k"
        else :
            # ("dump can't convert des")
            self.des = "c"
        '''
        12 -> h
        10 -> m
        15 -> a
        5 -> c
        17 -> j
        18 -> k

        '''
        self.eff = int(words[4])
        self.mob = int(words[5])
        # skip 5 zero
        self.dst = (int(words[11]), int(words[12]))
        self.avail = int(words[13])
        self.work = int(words[14])
        self.coa = int(words[15]) #1 is coa 0 is not

        # self.nextDes = int(words[16])
        if words[16] == '5':
            self.nextDes = "c"
        elif words[16] == '10':
            self.nextDes = "m"
        elif words[16] == "12":
            self.nextDes = "h"            
        elif words[16] == '15':
            self.nextDes = "a"
        elif words[16] == '17':
            self.nextDes = "j"
        elif words[16] == '18':
            self.nextDes = "k"
        else :
            self.nextDes = words[16]

        self.min = int(words[17])
        self.gold = int(words[18])
        self.fert = int(words[19])
        self.ocontent = int(words[20])
        self.uran = int(words[21])
        # skip one idk what is 37
        self.civ = int(words[23])
        self.mil = int(words[24])
        self.shell = int(words[25])
        self.gun = int(words[26])
        self.petrol = int(words[27])
        self.iron = int(words[28])
        self.dust = int(words[29])
        self.bar = int(words[30])
        self.food = int(words[31])
        self.oil = int(words[32])
        self.lcm = int(words[33])
        self.hcm = int(words[34])
        self.uw = int(words[35])
        self.rad = int(words[36])
        self.c_dist = int(words[37])
        self.m_dist = int(words[38])
        self.s_dist = int(words[39])
        self.g_dist = int(words[40])
        self.p_dist = int(words[41])
        self.i_dist = int(words[42])
        self.d_dist = int(words[43])
        self.b_dist = int(words[44])
        self.f_dist = int(words[45])
        self.o_dist = int(words[46])
        self.l_dist = int(words[47])
        self.h_dist = int(words[48])
        self.u_dist = int(words[49])
        self.r_dist = int(words[50])
        self.c_del = int(words[51])
        self.m_del = int(words[52])
        self.s_del = int(words[53])
        self.g_del = int(words[54])
        self.p_del = int(words[55])
        self.i_del = int(words[56])
        self.d_del = int(words[57])
        self.b_del = int(words[58])
        self.f_del = int(words[59])
        self.o_del = int(words[60])
        self.l_del = int(words[61])
        self.h_del = int(words[62])
        self.u_del = int(words[63])
        self.r_del = int(words[64])
        self.fallout = int(words[65])
        self.access = int(words[66])
        self.road = int(words[67])
        self.rail = int(words[68])
        self.dfense = int(words[69])

        # self.isCap = False
        self.money = money

    def feed(self):
        cost = self.calculateFoodCost()
        # print(cost)
        if self.food > cost:
                self.food -= cost
                # should I set the avail to 1263 after feed?
                self.avail = 1263
                self.eff = 100
        else:
            # don;t have enough food
            self.food = 0
            self.avail = 0

    def calculateFoodCost(self):
        foodCost = int((self.civ + self.mil) * 0.05)
        if foodCost == 0:
            foodCost = 1
        return foodCost

    def updateMob(self):
        # how about eff and work?

        if self.mob + sectMaxGainMob > sectMaximunMob:
            self.mob = int(sectMaximunMob)
        else:
            self.mob += int(sectMaxGainMob)

    def updateDes(self):
        # how about eff and work?
        """
        From src/lib/update/sect.c:

        avail = sect.avail / 2 * 100

        if sect.newdes != sect.des:

        build = 4 * avail / sect-chr.bwork

        if build < sect.effic:

            sect.effic -= build

        else:

            build = sect.effic

            sect.effic = 0

            sect.des = sect.newdes

        avail -= build / 4 * sect-chr.bwork

        if sect.newdes == sect.des:

        delta = avail / sect-chr.bwork

        build = min(delta, 100 - sect.effic)

        sect.effic += build

        avail -= build * sect-chr.bwork

        

        sect.avail = sect.avail / 2 + avail / 100 

        """
        if self.nextDes != self.des:
            self.eff = 0
            self.des = self.nextDes
            avail = self.avail / 2 * 100
            avail -= 100 / 4 * bwork
            # print("updateDes")
            # print(self.eff)
            # print(avail)
            """
            avail = self.avail / 2 * 100
            build = 4 * avail / bwork / 10
            print("updateDes")
            print(build)
            if build < self.eff:
                self.eff -= int(build)
            else:
                build = self.eff
                self.eff = 0
                self.des = self.nextDes
            avail -= build / 4 * bwork
            """
            self.avail = int(self.avail / 2 + avail / 100)
            # print(self.avail)

    def calculatePopulationGrow(self):
        """
        set q = etu * civ * obrate
        the number of births possible in other sectors
        If q is bigger than food / (2 * babyeat) set q to food / (2 * babyeat)
                food available to mature this many babies into civilians
        If q is bigger than 999 - civ set q to 999 - civ
                enough room for that many
        Set food = food - q * babyeat
        Set civ = civ + q
        """
        q = self.civ * obrate * etu
        if q > self.food / (2 * babyeat):
            q = self.food / (2 * babyeat)
        if q > 1000 - self.civ:
            q = 1000 - self.civ
        return q

    def updatePopulationGrow(self):
        q = int(self.calculatePopulationGrow())
        self.food -= int(q * babyeat)
        # print(q)
        self.civ += q
        if self.civ > 1000:
            self.civ = 1000

    def calculateTaxes(self):
        """
        /* pay taxes */
        Collect the taxes, pay the military
        civ_tax = (int) (.5 + (civs * eff * etu * civtaxrate / 100.));
        if (conquered) civ_tax /= 4.;
        uw_tax  = (int) (.5 + (uws  * eff * etu * uwtaxrate  / 100.));
        mil_pay = (int) (mil * etu * milpayrate);

        nat_money -= mil_pay
        nat_money += civ_tax + uw_tax
        """
        taxes = {}
        taxes['civ_tax'] = int(.5 + (self.civ * self.eff * etu * civtaxrate / 100.))
        taxes["uw_tax"]  = (int) (.5 + (self.uw  * self.eff * etu * uwtaxrate  / 100.))
        taxes["mil_pay"] = (int) (self.mil * etu * milpayrate)
        return taxes

    def updateTaxes(self):
        taxes = self.calculateTaxes()
        # find out where is the money store? 
        self.money -= int(taxes["mil_pay"])
        self.money += int(taxes['civ_tax'] + taxes["uw_tax"])

    def updateEff(self):
        # print(self.des, self.nextDes)
        avail = self.avail / 2 * 100
        if self.nextDes != self.des:
            delta = avail / bwork
            build = min(delta, 100 - self.eff)
            self.eff += int(build)
            avail -= build * bwork 

        self.avail = int(self.avail / 2 + avail / 100)
    
    def calculateProduction(self):
        """
        /* production */
        If effic is less than 60 skip the rest.

        If desig is bank then accrue  etu * bankint  interest per gold bar
        If desig is capital pay etu * $1 for government salaries
        If desig is enlistment sector, then convert civilians to military
                newmil = (etu * (mil + 10) * 0.05);
                nat_money -= newmil * 3;
        If this sector produces something (mines, research labs, etc.)
            calculate how much can be produced (see "info Products")
                (Note that the amount that can be produced is limited by "work")
            produce it
            pay for it (money, iron, gold mineral, oil, etc.)

            productionLst = cost raw materials dep gain
        


        production_efficiency = sect.effic / 100.0 (to make a floating point number in range [0.0, 1.0])
        if there is a natural resource involved:
            production_efficiency *= sect.resource / 100.0 (where resource is min, fert, etc.)

        worker_limit = sect.avail * production_efficiency / product.bwork;
        material_consume = min(material_limit, worker_limit)
        output = material_consume * prodeff

        sect.product (where product is the correct item produced) += output
        sect.consumed_items -= output/amount_used_per_output_item
        sect.avail -= product.bwork * material_consume / production_efficiency;
        """

        self.updateEff()

        productionLst = {}
        if self.eff >= 60:
            """
            prodeff = self.eff / 100
            amount_used_per_output_item = 0
            material_limit = 100000

            if self.des in ['a', 'm', 'o', "c"]:
                if self.des == "a":
                    prodeff *= self.fert / 100
                elif self.des == "m":
                    prodeff *= self.min / 100
                elif self.des == "o":
                    prodeff *= self.ocontent / 100
                elif self.des == "c":
                    productionLst["money"] = - (etu * government_salaries)
                
            else:
                if self.des == "j":
                    material_limit = self.iron
                    amount_used_per_output_item = 1
                elif self.des == "k":
                    amount_used_per_output_item = 2
                    material_limit = self.iron / amount_used_per_output_item

            worker_limit = self.avail * prodeff / bwork

            material_consume = min(material_limit, worker_limit)

            output = int(material_consume * prodeff)
            
            print(prodeff, worker_limit, material_consume)

            productionLst["gain"] = output
            if amount_used_per_output_item != 0:
                productionLst['cost'] = {'iron': output / amount_used_per_output_item}
            
            if output < 1:
                productionLst['cost'] = {'avail': int(bwork * material_consume / prodeff)}

            """
            prodeff = self.eff / 100

            if self.des == "b":
                productionLst["gain"] = etu * self.gold * bankint
            elif self.des == "c":
                productionLst["money"] = -(etu * government_salaries)
            elif self.des == "m":
                productionLst["gain"] = int(self.avail * prodeff * self.min / 100 / 4)
            elif self.des == "d":
                productionLst["gain"] = self.dust * self.work
                productionLst["dep"] = 20
            elif self.des == "a":
                foodGorw =  self.fert * .2 * etu
               
                harvested = (self.civ + self.mil / 5) + 0.002

                effact = (self.eff) * (tlev + 10) / (100 * (tlev + 20))
                additionalFood = (self.civ + self.mil / 5) * effact * self.eff / 1000

                totalGorw = foodGorw + additionalFood
                # not sure if it extra gorw or extra gain

                if totalGorw > harvested:
                    totalFood = harvested
                else:
                    totalFood = totalGorw
                productionLst["gain"] = int(totalFood)

            elif self.des == "o":
                productionLst["dep"] = 10
                productionLst["gain"] = self.ocontent * self.work / (tlev + 10) / ( tlev +20)
            elif self.des == "r":
                productionLst["dep"] = 35
                productionLst['gain'] = self.uran * self.work / (tlev-40) / (tlev-30)
            elif self.des == "s":
                # shells s  $3     2l  1h   (tech-20)/(tech-10)
                baseCost = (tlev-20)/(tlev-10)
                maxProdcal = int(self.work / baseCost)
                while True:
                    if self.lcm > 2 * maxProdcal and self.hcm > maxProdcal and money > maxProdcal * 3:
                        break
                    else:
                        maxProdcal -= 1  
                productionLst['cost'] = 3 * maxProdcal
                productionLst['gain'] = maxProdcal
                productionLst["raw"] = {'lcm':  2 * maxProdcal, 'hcm':maxProdcal}
            elif self.des == "j":
                # lcm l  $0     1i   (tech+10)/(tech+20)
                if self.iron > 0:
                    baseCost = (tlev+10)/(tlev+20)
                    maxProdcal = int(self.work / baseCost)
                    while True:
                        if self.iron > maxProdcal or maxProdcal == 0:
                            break
                        else:
                            maxProdcal -= 1  
                    productionLst['gain'] = maxProdcal
                    productionLst["raw"] = {'iron': maxProdcal}

            elif self.des == "k":
                # hcm h  $0     2i    (tech+10)/(tech+20)
                if self.iron > 0:
                    baseCost = (tlev+10)/(tlev+20)
                    maxProdcal = int(self.work / baseCost)
                    while True:
                        if self.iron > 2 * maxProdcal or maxProdcal == 0:
                            break
                        else:
                            maxProdcal -= 1  
                    productionLst['gain'] = maxProdcal
                    productionLst["raw"] = {'iron': 2 * maxProdcal}
           

        return productionLst

    def updateProduction(self):
        production = self.calculateProduction()

        if len(production) > 0:
            if self.des == "b":
                self.money += int(production["gain"])
            elif self.des == "c":
                self.money -= int(production["money"])
            elif self.des == "m":
                self.iron += int(production["gain"])
            elif self.des == "d":
                self.dust += int(production["gain"])
                self.gold -= int(production["dep"])
            elif self.des == "a":
                self.food += int(production["gain"])
            elif self.des == "o":
                self.ocontent -= int(production["dep"])
                self.oil += int(production["gain"])
            elif self.des == "r":
                self.uran -= int(production["dep"])
                self.rad += int(production['gain'])
            elif self.des == "s":
                self.money -= int(production['cost'])
                self.shell += int(production['gain'])
                self.lcm -= int(production["raw"]["lcm"])
                self.hcm -= int(production["raw"]["hcm"])
            elif self.des == "j":
                self.lcm += int(production['gain'])
                self.iron -= int(production["raw"]['iron'])
            elif self.des == "k":
                self.hcm += int(production['gain'])
                self.iron -= int(production["raw"]['iron'])

    def calculateMaintain(self):
        # .001 * cost of thing * ETUs/update
        return int(.001 * etu * sect_maintenance)

    def updateMaintain(self):
        self.money -= int(self.calculateMaintain())

    def calculateBuilding(self):
        return
    
    def updateBuilding(self):
        return
    

    

class Ship:
    def __init__(self,words):
        self.uid = int(words[0])
        self.owner = int(words[1])
        self.location = (int(words[2]),int(words[3]))
        self.type = int(words[4])
        self.eff = int(words[5])
        self.mob = int(words[6])
        self.off = int(words[7])
        self.tech = int(words[8])
        self.opx = int(words[9]) 
        self.opy = int(words[10])
        self.mission = int(words[11])
        self.radius = int(words[12])
        self.fleet= words[13] 
        self.civ = int(words[14])
        self.mil = int(words[15])
        self.shell = int(words[16])
        self.gun = int(words[17])
        self.petrol = int(words[18])
        self.iron = int(words[19])
        self.dust = int(words[20])
        self.bar = int(words[21])
        self.food = int(words[22])
        self.oil = int(words[23])
        self.lcm = int(words[24])
        self.hcm = int(words[25])
        self.uw = int(words[26])
        self.rad = int(words[27])
        self.access = int(words[28])
        self.name = words[29]
        self.rflags = words[30]
        self.rpath = words[31]
    
    def calculateMaintain(self):
        # .001 * cost of thing * ETUs/update
        return int(.001 * etu * ship_maintenance)

    def updateMaintain(self):
        self.money -= self.calculateMaintain()


