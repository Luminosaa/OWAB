# An item is defined by :
# Name, level, 
class Item:
    def __init__(self, name: str, level: int, rarity: int, desc: str):
        self.name:str = name
        self.level:int = level
        self.rarity:int = rarity
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


# class Effect: