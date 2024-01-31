import enumerations.action as Action
import enumerations.rarity as Rarity
import effect as Effect

# An item is defined by :
# Name, level, 
class Item:
    def __init__(self, name: str, level: int, rarity: Rarity, desc: str):
        self.name:str = name
        self.level:int = level
        self.rarity:Rarity = rarity
        self.desc:str = desc
        self.effects:list(Effect) = []
        return

    def __name__(self) -> str:
        return self.name

    def __level__(self) -> int:
        return self.level 
    
    def __rarity__(self) -> int:
        return self.rarity
    
    def __desc__(self) -> str:
        return self.desc

    def __effects__(self) -> list(Effect):
        return self.effects
    
    def __str__(self) -> str:
        return f"{self.name} ({self.rarity}) : {self.desc} \n\t{self.effects}"
    
    def add_effect(self, effect: Effect):
        self.effects.append(effect)
        return