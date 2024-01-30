from enum import Enum

# An item is defined by :
# Name, level, 
class Item:
    def __init__(self, name: str, level: int, rarity: Rarity, desc: str):
        self.name:str = name
        self.level:int = level
        self.rarity:Rarity = rarity
        self.desc:str = desc
        self.effects:list(Effect) = []

    def getName(self) -> str:
        return self.name

    def getLevel(self) -> int:
        return self.level 
    
    def getRarity(self) -> int:
        return self.rarity
    
    def getRarityString(self) -> str:
        s = ""
        if (self.rarity == 0):
            s = "Commun"
        elif (self.rarity == 1):
            s = "Rare"
        # TO DO 
        return s 

# Rarity class
class Rarity(Enum):

    COMMON = 0
    INHABITUEL = 1
    RARE = 2
    MYTHIQUE = 3
    LEGENDARY = 4
    RELIQUE = 5
    EPIQUE = 6

    def __str__(self) -> str:

        if self.rarity == Rarity.COMMON:
            return "Commun"
        elif self.rarity == Rarity.INHABITUEL:
            return "Inhabituel"
        elif self.rarity == Rarity.RARE:
            return "Rare"
        elif self.rarity == Rarity.MYTHIQUE:
            return "Mythique"
        elif self.rarity == Rarity.LEGENDARY:
            return "Légendaire"
        elif self.rarity == Rarity.RELIQUE:
            return "Relique"
        elif self.rarity == Rarity.EPIQUE:
            return "Epique"
        else:
            return "Rareté inconnue"

class EffectType(Enum):

    HP = 20
    HEALING_MASTERY = 26
    AP = 31
    MP = 41
    CRITICAL_RESISTANCE = 71/988
    REAR_RESISTANCE = 71/988
    ELEMENTAL_RESISTANCE = 80
    RESISTANCE_FIRE = 82
    RESISTANCE_WATER = 83
    RESISTANCE_EARTH = 84
    RESISTANCE_AIR = 85
    ELEMENTAL_MASTERY = 120
    CRITICAL_MASTERY = 149
    CRITICAL_HIT = 150
    RANGE = 160
    LOCK = 173
    DODGE  = 175
    REAR_MASTERY = 180
    CONTROL = 184
    WP = 191
    BLOCK = 875
    MELEE_MASTERY = 1052
    DISTANCE_MASTERY = 1053
    BERSERK_MASTERY = 1055
    MASTERY_OF_2_ELEMENTS = 1068 #Param[2] = 2
    MASTERY_OF_3_ELEMENTS = 1068 #Param[2] = 3
    RESISTANCE_OF_1_ELEMENT = 1069 #Param[2] = 1


# class Effect:
class Effect:

    def __init__(self, )