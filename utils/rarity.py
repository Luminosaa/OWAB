from enum import Enum

class Rarity(Enum):

    COMMUN = 0
    INHABITUEL = 1
    RARE = 2
    MYTHIQUE = 3
    LEGENDAIRE = 4
    RELIQUE = 5
    EPIQUE = 6

    def __str__(self) -> str:

        if self == Rarity.COMMUN:
            return "Commun"
        elif self == Rarity.INHABITUEL:
            return "Inhabituel"
        elif self == Rarity.RARE:
            return "Rare"
        elif self == Rarity.MYTHIQUE:
            return "Mythique"
        elif self == Rarity.LEGENDAIRE:
            return "Légendaire"
        elif self == Rarity.RELIQUE:
            return "Relique"
        elif self == Rarity.EPIQUE:
            return "Epique"
        else:
            return "Rareté inconnue"
