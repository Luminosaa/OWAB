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

    DOMMAGE_NEUTRE = 1
    BOOST_POINT_DE_VIE = 20
    DEBOOST_POINT_DE_VIE = 21
    SOIN_NEUTRE = 24
    GAIN_MAITRISE_SOIN = 26
    BOOST_PA = 31
    GAIN_CHARAC


# class Effect:
class Effect:

    def __init__(self, )