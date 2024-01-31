from enum import Enum

"""
TOUT EST DANS CE .PY CAR IL Y A DES BUGS AVEC LES IMPORTS
GENRE IMPOSSIBLE D'IMPORTER EFFECT ET RARITY DANS ITEM
ET PAREIL POUR IMPORT ACTION DANS EFFECT
"""


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

class Action(Enum):

	DOMMAGE_NEUTRE = 1
	BOOST_POINT_DE_VIE_PV = 20
	DEBOOST_POINT_DE_VIE_PV = 21
	SOIN_NEUTRE_VOL_DE_VIE = 24
	GAIN_MAITRISE_SOIN = 26
	BOOST_PA = 31
	GAIN_CHARAC_PASSEE_EN_PARAMETRE = 39
	PERTE_CHARAC_PASSEE_EN_PARAMETRE = 40
	BOOST_PM = 41
	DEBOOST_PA = 56
	DEBOOST_PM = 57
	GAIN_RESISTANCE_DOS = 71
	GAIN_RESISTANCE_ELEMENTAIRE = 80
	GAIN_RESISTANCE_FEU = 82
	GAIN_RESISTANCE_EAU = 83
	GAIN_RESISTANCE_TERRE = 84
	GAIN_RESISTANCE_AIR = 85
	PERTE_RESISTANCE_ELEMENTAIRE = 90
	PERTE_RESISTANCE_TERRE_SANS_CAP = 96
	PERTE_RESISTANCE_FEU_SANS_CAP = 97
	PERTE_RESISTANCE_EAU_SANS_CAP = 98
	PERTE_RESISTANCE_ELEMENTAIRE_SANS_CAP = 100
	GAIN_MAITRISE_ELEMENTAIRE = 120
	GAIN_MAITRISE_FEU = 122
	GAIN_MAITRISE_TERRE = 123
	GAIN_MAITRISE_EAU = 124
	GAIN_MAITRISE_AIR = 125
	PERTE_MAITRISE_ELEMENTAIRE = 130
	PERTE_MAITRISE_FEU = 132
	GAIN_MAITRISE_CRITIQUE = 149
	GAIN_COUP_CRITIQUE_POURCENTAGE = 150
	GAIN_PORTEE = 160
	PERTE_PORTEE = 161
	GAIN_PROSPECTION = 162
	GAIN_SAGESSE = 166
	PERTE_COUP_CRITIQUE_POURCENTAGE = 168
	GAIN_INITIATIVE = 171
	PERTE_INITIATIVE = 172
	GAIN_TACLE = 173
	PERTE_TACLE = 174
	GAIN_ESQUIVE = 175
	PERTE_ESQUIVE = 176
	GAIN_VOLONTE = 177
	GAIN_MAITRISE_DOS = 180
	PERTE_MAITRISE_DOS = 181
	GAIN_CONTROLE = 184
	BOOST_PW = 191
	DEBOOST_PW = 192
	PERTE_PW = 194
	STATE_APPLIQUE_UN_ETAT = 304
	REG_EXECUTE_LE_GROUPE_D_EFFETS = 330
	NULLEFFECT_EFFET_VIDE = 400
	SPELL_GAIN_DE_NIVEAUX_DE_SORTS_DANS_UNE_BRANCHE = 832
	AREA_RETIRE_UNE_ZONE_EN_SELECTIONNANT_LA_ZONE_COMME_CIBLE = 843
	REG_VALEUR_DU_SECOND_EFFET_FONCTION_DE_CELLE_DU_PREMIER_2_EFFETS_ENFANTS_MAX = 865
	GAIN_PARADE = 875
	PERTE_PARADE = 876
	SPELL_GAIN_DE_NIVEAU_DE_SORT_TOUS_ELEMENTS_SAUF_SUPPORT = 979
	GAIN_RESISTANCE_CRITIQUE = 988
	REG_NIVEAU_DES_ENFANTS_FONCTION_DE_LA_VALEUR_DE_L_EFFET_DECLENCHEUR = 1020
	GAIN_MAITRISE_MELEE = 1052
	GAIN_MAITRISE_DISTANCE = 1053
	GAIN_MAITRISE_BERSERK = 1055
	PERTE_MAITRISE_CRITIQUE = 1056
	PERTE_MAITRISE_MELEE = 1059
	PERTE_MAITRISE_DISTANCE = 1060
	PERTE_MAITRISE_BERSERK = 1061
	PERTE_RESISTANCE_CRITIQUE = 1062
	PERTE_RESISTANCE_DOS = 1063
	GAIN_MAITRISE_ELEMENTAIRE_DANS_UN_NOMBRE_VARIABLE_D_ELEMENTS = 1068
	GAIN_RESISTANCE_ELEMENTAIRE_DANS_UN_NOMBRE_VARIABLE_D_ELEMENTS = 1069
	DOMMAGE_LUMIERE = 1083
	SOIN_LUMIERE = 1084
	JOB_MODIFIE_LA_QUANTITE_D_OBJETS_RECOLTEE = 2001

class Effect:

    action: Action
    value: int

    def __init__(self, action: Action, value: int):
        self.action = action
        self.value = value
        return

    def __action__(self) -> Action:
        return self.action
    
    def __value__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return f"{self.action.__str__()} : {self.value}"

# An item is defined by :
# Name, level,
class Item:

    def __init__(self, name: str, level: int, rarity: Rarity, desc: str):
        self.name: str = name
        self.level: int = level
        self.rarity: Rarity = rarity
        self.desc: str = desc
        self.effects: list[Effect] = []
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

    def __str__(self) -> str:
        return f"{self.name} ({self.rarity.__str__()}) : {self.desc} \n\t{self.effects.__str__()}"

    def add_effect(self, effect: Effect):
        self.effects.append(effect)
        return
    
