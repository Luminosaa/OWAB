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

        if self.rarity == Rarity.COMMUN:
            return "Commun"
        elif self.rarity == Rarity.INHABITUEL:
            return "Inhabituel"
        elif self.rarity == Rarity.RARE:
            return "Rare"
        elif self.rarity == Rarity.MYTHIQUE:
            return "Mythique"
        elif self.rarity == Rarity.LEGENDAIRE:
            return "Légendaire"
        elif self.rarity == Rarity.RELIQUE:
            return "Relique"
        elif self.rarity == Rarity.EPIQUE:
            return "Epique"
        else:
            return "Rareté inconnue"