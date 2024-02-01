from utils.effect import Effect
from utils.rarity import Rarity
from utils.action import Action
from utils.type import Type

# An item is defined by :
# Name, level,
class Item:
    def __init__(self, name: str, level: int, rarity: Rarity, desc: str, type:Type):
        self.name: str = name
        self.level: int = int(level)
        self.rarity: Rarity = rarity
        self.desc: str = desc
        self.effects: list[Effect] = []
        self.type: Type = type 
        return

    def __name__(self) -> str:
        return self.name

    def __level__(self) -> int:
        return self.level

    def __rarity__(self) -> int:
        return self.rarity

    def __desc__(self) -> str:
        return self.desc

    def __effects__(self):
        return self.effects
    
    def __effects__(self):
        return self.type
    
    def __str__(self) -> str:
        return f"{self.name} ({self.type.__str__()}) ({self.rarity.__str__()}) : \n\t{[effect.__str__() for effect in self.effects]}"

    def add_effect(self, effect: Effect):
        self.effects.append(effect)
        return
    
