from urllib3 import Retry
from utils.item import Item, Rarity, Effect, Action, Type
from ortools.linear_solver import pywraplp
import json
from utils.action import Action

class WakfuSolver():
    def __init__(self):
        self.items : list(Item) = []
        self.solver: pywraplp.Solver = pywraplp.Solver.CreateSolver("SAT")
        if not self.solver:
            print("Error : invalid solver")
            exit(0)
        self.objective: pywraplp.Objective = self.solver.Objective()
        self.__parseItems()
        for item in self.items:
            item.setSolverVar(self.solver.IntVar(0, 1, item.name))


    # Map item type (used in parseItems)
    def __parseType(self, item) -> type:
        itemTypeId = item["definition"]["item"]["baseParameters"]["itemTypeId"]
        if itemTypeId in [101, 111, 114, 117, 223, 253, 519]:
            return Type.FIRST_WEAPON_2_HANDS
        elif itemTypeId in [108, 110, 113, 115, 254, 518]:
            return Type.FIRST_WEAPON_1_HAND
        elif itemTypeId in [112, 189, 520]:
            return Type.SECOND_WEAPON
        elif itemTypeId == 103:
            return Type.RING 
        elif itemTypeId == 119:
            return Type.LEGS 
        elif itemTypeId == 120:
            return Type.NECK 
        elif itemTypeId == 132:
            return Type.BACK
        elif itemTypeId == 133:
            return Type.BELT
        elif itemTypeId == 134:
            return Type.HEAD
        elif itemTypeId == 136:
            return Type.CHEST
        elif itemTypeId == 138:
            return Type.SHOULDERS
        else:
            return Type.AUTRE
    
    # Parse item list (used int __init__)
    def __parseItems(self):
        with open("jsons/items.json", "r") as f:
            items = json.load(f)
        action_dict: dict = {str(member.value): name for name, member in Action.__members__.items()}
        for item in items:
            name: str = item["title"]["fr"]
            level: int = item["definition"]["item"]["level"]
            rarity: Rarity = [name if member.value == item["definition"]["item"]["baseParameters"]["rarity"] else Rarity.COMMUN for name, member in Rarity.__members__.items()][0]
            desc: str = item["description"]["fr"] if "description" in item else "Pas de description"
            type = self.__parseType(item)
            if type == Type.AUTRE:
                continue
            if len(item["definition"]["equipEffects"]) == 0:
                continue
            objet: Item = Item(name, level, rarity, desc, type)
            for effect in item["definition"]["equipEffects"]:
                action: Action = action_dict[str(effect["effect"]["definition"]["actionId"])] if str(effect["effect"]["definition"]["actionId"]) in action_dict else None
                valeur: int = effect["effect"]["definition"]["params"][0] if len(effect["effect"]["definition"]["params"]) > 0 else 0
                if (effect["effect"]["definition"]["actionId"] in [1068, 1069]):
                    effet: Effect = Effect(action, valeur, effect["effect"]["definition"]["params"][2])
                else:
                    effet: Effect = Effect(action, valeur)
                objet.add_effect(effet)
            self.items.append(objet)

    def __items__(self):
        return self.items        

    # Remove all item with lower level than limitMin from the solver 
    def minLevelItem(self, limitMin:int):
        i = 0
        while (i < len(self.items)):
            if self.items[i].__level__() < limitMin:
                self.items.pop(i)
            else:
                i+=1

    # Remove all item with higher level than limitMax from the solver 
    def maxLevelItem(self, limitMax:int):
        i = 0
        while (i < len(self.items)):
            if self.items[i].__level__() > limitMax:
                self.items.pop(i)
            else:
                i+=1

    def uniqueContraint(self):
        type_map = {}
        type_map[Rarity.RELIQUE] = []
        type_map[Rarity.EPIQUE] = []
        # Init a map by type 
        for type, member in Type.__members__.items():
            type_map[member] = []
        # Fill the map
        for item in self.items:
            type_map[item.__type__()].append(item.__solverVar__())
            if item.__rarity__() == Rarity.EPIQUE:
                type_map[Rarity.EPIQUE].append(item)
            elif item.__rarity__() == Rarity.RELIQUE:
                type_map[Rarity.RELIQUE].append(item)
        
        
        # Add constraint for each type 
        for type, member in Type.__members__.items():
            self.solver.Add(sum(type_map[member]) <= 1)

    def addConstraint(self, stat:str, value:str, max:bool=True):
        return 0


    def maximize(self, stat: str):
        self.uniqueContraint()
        for item in self.items:
            self.objective.SetCoefficient(item.__solverVar__(), item.getEffectValue(stat))
        self.objective.SetMaximization()

    def solve(self):
        self.solver.Solve()
        print("Objective value =", self.objective.Value())
        for item in self.items:
            if (item.__solverVar__().solution_value() != 0):
                print(item)


if __name__ == "__main__":
    WS = WakfuSolver()
    WS.minLevelItem(0)
    WS.maxLevelItem(50)
    WS.maximize("GAIN_PORTEE")
    WS.solve()

