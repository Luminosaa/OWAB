from enum import Enum

# A class that describe the type of an equipement (shield, sword, helmet...) 
class Type(Enum):
    FIRST_WEAPON_2_HANDS = 0
    FIRST_WEAPON_1_HAND = 1
    SECOND_WEAPON = 4
    RING = 2
    LEGS = 3
    NECK = 4
    BACK = 5
    BELT = 6
    HEAD = 7
    CHEST = 8
    SHOULDERS = 9 
    AUTRE = 10 

    def __str__(self):
        if self == Type.FIRST_WEAPON_2_HANDS:
            return "Arme à 2 mains"
        if self == Type.FIRST_WEAPON_1_HAND:
            return "Arme à 1 main"
        if self == Type.SECOND_WEAPON:
            return "Bouclier/Dague"
        if self == Type.RING:
            return "Anneau"
        if self == Type.LEGS:
            return "Jambieres"
        if self == Type.NECK:
            return "Amulette"
        if self == Type.BACK:
            return "Cape"
        if self == Type.BELT:
            return "Ceinture"
        if self == Type.HEAD:
            return "Casque"
        if self == Type.CHEST:
            return "Plastron"
        if self == Type.SHOULDERS:
            return "Epaulieres"
        if self == Type.AUTRE:
            return "Autre"