# HanSolo Class
class HanSolo:

    def __init__(self, planets, hyper_table):
        self.planets = planets
        self.hyperTable = hyper_table
        self.jumps = []

    def getPlanetIndex(self, name):
        return self.planets.index(name) if name in self.planets else "planet not in available planets"

    def getPlanetName(self, index):
        return self.planets[index] if index <= len(self.planets) else f"index {index} is too large try index lower than {len(self.planets)}"

    def getMinEnergyTargetPlanet(self, planet):
        if planet in self.planets:
            planet_table = self.hyperTable[self.getPlanetIndex(planet)]
        else:
            return f"Planet {planet} is not available" 
        # get maximum for case
        value = max(planet_table)
        
        for i in planet_table:
            # if values is -1 just continue to next iteration
            if i == -1:
                continue
            # value is lower than actual maximum replace it 
            if i < value:
                value = i
        return self.getPlanetName(planet_table.index(value))

    def getAllPossiblejumps(self, sourceID, energyConsumed):
        if sourceID <= len(self.planets):
            planet_table = self.hyperTable[sourceID]
        else:
            return f"Planet with id {sourceID} is not available" 

        for i in range(len(self.planets)):
            if i == sourceID:
                continue
            else:
                new_jump = Jump(sourceID, i, energyConsumed + planet_table[i])
                self.jumps.append(new_jump)

        return self.jumps

    def printJumps(self, jumpsArray):
        for i in jumpsArray:
            print(f"{self.planets[i.targetID]} via {self.planets[i.sourceID]} for {i.energyConsumed}")

    def getMinEnergyJump(self, jumpsArray):
        item_energy = jumpsArray[0].energyConsumed
        for i in jumpsArray:
            if i.energyConsumed < item_energy:
                item_energy = i.energyConsumed 
        for i in jumpsArray:
            if i.energyConsumed == item_energy:
                return i 
                
    def removeJump(self, jumpsArray, jump):
        return list(filter(lambda x: x != jump, jumpsArray))

        
        

# Jump Class
class Jump:

    def __init__(self, sourceID, targetID, energyConsumed):
        self.sourceID = sourceID
        self.targetID = targetID
        self.energyConsumed = energyConsumed
        
# TEST 
han_solo = HanSolo(["Tatooine", "Naboo", "Hoth", "Devaron", "Dantooine", "Alderaan"],  
                    [[-1, 40, 20, 150, 130, 218],
                     [40, -1, 135, 70, 45, 198],
                     [20, 135, -1, 20, 60, 166],
                     [150, 70, 20, -1, 112, 62],
                     [130, 45, 60, 112, -1, 15],
                     [218, 198, 166, 62, 15, -1]])


# CASE getPlanetIndex
print("")
print("--- CASE getPlanetIndex ---")

tatooine_index = han_solo.getPlanetIndex("Tatooine")
naboo_index = han_solo.getPlanetIndex("Naboo")
alderaan_index = han_solo.getPlanetIndex("Alderaan")
non_exist_planet = han_solo.getPlanetIndex("Moon")

print(f"Index of planet Tatooine is {tatooine_index}")
print(f"Index of planet Naboo is {naboo_index}")
print(f"Index of planet Alderaan is {alderaan_index}")
print(f"Case Moon: {non_exist_planet}")


# CASE getPlanetName
print("")
print("--- CASE getPlanetName ---")

index_2 = han_solo.getPlanetName(2)
index_4 = han_solo.getPlanetName(4)
index_0 = han_solo.getPlanetName(0)
non_exist_index = han_solo.getPlanetName(8)

print(f"Name of planet on index 2 {index_2}")
print(f"Name of planet on index 4 {index_4}")
print(f"Name of planet on index 0 {index_0}")
print(f"Name of planet on index 8 {non_exist_index}")

# CASE getPlanetName
print("")
print("--- CASE getMinEnrgyTargetPlanet ---")

naboo_test = han_solo.getMinEnergyTargetPlanet("Naboo")
hoth_test = han_solo.getMinEnergyTargetPlanet("Hoth")
devaron_test = han_solo.getMinEnergyTargetPlanet("Devaron")
bad_test = han_solo.getMinEnergyTargetPlanet("Moon")

print(f"Test for planet Naboo: {naboo_test}")
print(f"Test for planet Hoth: {hoth_test}")
print(f"Test for planet Devaron: {devaron_test}")
print(f"Bad test for planet Moon: {bad_test}")

# CASE getAllPossibleJumps with printJumps
print("")
print("--- CASE getAllPossibleJumps ---")

# with 100 enrgy   
id1_test = han_solo.getAllPossiblejumps(1, 100)
han_solo.printJumps(id1_test)

# CASE getMinEnergyJump using jumps from id1_test
bestJump = han_solo.getMinEnergyJump(id1_test)

print(f"{bestJump.sourceID}, {bestJump.targetID}, {bestJump.energyConsumed}")

# CASE removeJump using jumps from id1_test and first jump as test case

jump = id1_test[0]

print("Before removing")
han_solo.printJumps(id1_test)

print("after removing")
han_solo.printJumps(han_solo.removeJump(id1_test, jump))




