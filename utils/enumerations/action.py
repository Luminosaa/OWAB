from enum import Enum

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

	def __str__(self) -> str:

		match(self):

			case(Action.DOMMAGE_NEUTRE):
				return "Dommage : Neutre"
			case(Action.BOOST_POINT_DE_VIE_PV):
				return "Boost : Point de vie (PV)"
			case(Action.DEBOOST_POINT_DE_VIE_PV):
				return "Deboost : Point de vie (PV)"
			case(Action.SOIN_NEUTRE_VOL_DE_VIE):
				return "Soin : Neutre (Vol de vie)"
			case(Action.GAIN_MAITRISE_SOIN):
				return "Gain : Maîtrise Soin"
			case(Action.BOOST_PA):
				return "Boost : PA"
			case(Action.GAIN_CHARAC_PASSEE_EN_PARAMETRE):
				return "Gain : charac passée en paramètre"
			case(Action.PERTE_CHARAC_PASSEE_EN_PARAMETRE):
				return "Perte : charac passée en paramètre"
			case(Action.BOOST_PM):
				return "Boost : PM"
			case(Action.DEBOOST_PA):
				return "Deboost : PA"
			case(Action.DEBOOST_PM):
				return "Deboost : PM"
			case(Action.GAIN_RESISTANCE_DOS):
				return "Gain : Résistance Dos"
			case(Action.GAIN_RESISTANCE_ELEMENTAIRE):
				return "Gain : Résistance Élémentaire"
			case(Action.GAIN_RESISTANCE_FEU):
				return "Gain : Résistance Feu"
			case(Action.GAIN_RESISTANCE_EAU):
				return "Gain : Résistance Eau"
			case(Action.GAIN_RESISTANCE_TERRE):
				return "Gain : Résistance Terre"
			case(Action.GAIN_RESISTANCE_AIR):
				return "Gain : Résistance Air"
			case(Action.PERTE_RESISTANCE_ELEMENTAIRE):
				return "Perte : Résistance Élémentaire"
			case(Action.PERTE_RESISTANCE_TERRE_SANS_CAP):
				return "Perte : Résistance Terre (sans cap)"
			case(Action.PERTE_RESISTANCE_FEU_SANS_CAP):
				return "Perte : Résistance Feu (sans cap)"
			case(Action.PERTE_RESISTANCE_EAU_SANS_CAP):
				return "Perte : Résistance Eau (sans cap)"
			case(Action.PERTE_RESISTANCE_ELEMENTAIRE_SANS_CAP):
				return "Perte : Résistance Élémentaire (sans cap)"
			case(Action.GAIN_MAITRISE_ELEMENTAIRE):
				return "Gain : Maîtrise Élémentaire"
			case(Action.GAIN_MAITRISE_FEU):
				return "Gain : Maîtrise Feu"
			case(Action.GAIN_MAITRISE_TERRE):
				return "Gain : Maîtrise Terre"
			case(Action.GAIN_MAITRISE_EAU):
				return "Gain : Maîtrise Eau"
			case(Action.GAIN_MAITRISE_AIR):
				return "Gain : Maîtrise Air"
			case(Action.PERTE_MAITRISE_ELEMENTAIRE):
				return "Perte : Maîtrise Élémentaire"
			case(Action.PERTE_MAITRISE_FEU):
				return "Perte : Maîtrise Feu"
			case(Action.GAIN_MAITRISE_CRITIQUE):
				return "Gain : Maîtrise Critique"
			case(Action.GAIN_COUP_CRITIQUE_POURCENTAGE):
				return "Gain : Coup Critique (%)"
			case(Action.GAIN_PORTEE):
				return "Gain : Portée"
			case(Action.PERTE_PORTEE):
				return "Perte : Portée"
			case(Action.GAIN_PROSPECTION):
				return "Gain : Prospection"
			case(Action.GAIN_SAGESSE):
				return "Gain : Sagesse"
			case(Action.PERTE_COUP_CRITIQUE_POURCENTAGE):
				return "Perte : Coup Critique (%)"
			case(Action.GAIN_INITIATIVE):
				return "Gain : Initiative"
			case(Action.PERTE_INITIATIVE):
				return "Perte : Initiative"
			case(Action.GAIN_TACLE):
				return "Gain : Tacle"
			case(Action.PERTE_TACLE):
				return "Perte : Tacle"
			case(Action.GAIN_ESQUIVE):
				return "Gain : Esquive"
			case(Action.PERTE_ESQUIVE):
				return "Perte : Esquive"
			case(Action.GAIN_VOLONTE):
				return "Gain : Volonté"
			case(Action.GAIN_MAITRISE_DOS):
				return "Gain : Maîtrise Dos"
			case(Action.PERTE_MAITRISE_DOS):
				return "Perte : Maîtrise Dos"
			case(Action.GAIN_CONTROLE):
				return "Gain : Contrôle"
			case(Action.BOOST_PW):
				return "Boost : PW"
			case(Action.DEBOOST_PW):
				return "Deboost : PW"
			case(Action.PERTE_PW):
				return "Perte : PW"
			case(Action.STATE_APPLIQUE_UN_ETAT):
				return "State : Applique un état"
			case(Action.REG_EXECUTE_LE_GROUPE_D_EFFETS):
				return "REG : execute le groupe d'effets"
			case(Action.NULLEFFECT_EFFET_VIDE):
				return "NullEffect : Effet Vide"
			case(Action.SPELL_GAIN_DE_NIVEAUX_DE_SORTS_DANS_UNE_BRANCHE):
				return "Spell : Gain de niveaux de sorts dans une branche"
			case(Action.AREA_RETIRE_UNE_ZONE_EN_SELECTIONNANT_LA_ZONE_COMME_CIBLE):
				return "Area : Retire une zone en sélectionnant la zone comme cible"
			case(Action.REG_VALEUR_DU_SECOND_EFFET_FONCTION_DE_CELLE_DU_PREMIER_2_EFFETS_ENFANTS_MAX):
				return "REG : valeur du second effet fonction de celle du premier (2 effets enfants max)"
			case(Action.GAIN_PARADE):
				return "Gain : Parade"
			case(Action.PERTE_PARADE):
				return "Perte : Parade"
			case(Action.SPELL_GAIN_DE_NIVEAU_DE_SORT_TOUS_ELEMENTS_SAUF_SUPPORT):
				return "Spell : Gain de niveau de sort tous éléments (sauf support)"
			case(Action.GAIN_RESISTANCE_CRITIQUE):
				return "Gain : Résistance Critique"
			case(Action.REG_NIVEAU_DES_ENFANTS_FONCTION_DE_LA_VALEUR_DE_L_EFFET_DECLENCHEUR):
				return "REG : niveau des enfants fonction de la valeur de l'effet déclencheur"
			case(Action.GAIN_MAITRISE_MELEE):
				return "Gain : Maîtrise Mêlée"
			case(Action.GAIN_MAITRISE_DISTANCE):
				return "Gain : Maîtrise Distance"
			case(Action.GAIN_MAITRISE_BERSERK):
				return "Gain : Maîtrise Berserk"
			case(Action.PERTE_MAITRISE_CRITIQUE):
				return "Perte : Maîtrise Critique"
			case(Action.PERTE_MAITRISE_MELEE):
				return "Perte : Maîtrise Mêlée"
			case(Action.PERTE_MAITRISE_DISTANCE):
				return "Perte : Maîtrise Distance"
			case(Action.PERTE_MAITRISE_BERSERK):
				return "Perte : Maîtrise Berserk"
			case(Action.PERTE_RESISTANCE_CRITIQUE):
				return "Perte : Résistance Critique"
			case(Action.PERTE_RESISTANCE_DOS):
				return "Perte : Résistance Dos"
			case(Action.GAIN_MAITRISE_ELEMENTAIRE_DANS_UN_NOMBRE_VARIABLE_D_ELEMENTS):
				return "Gain : Maîtrise Élémentaire dans un nombre variable d'éléments"
			case(Action.GAIN_RESISTANCE_ELEMENTAIRE_DANS_UN_NOMBRE_VARIABLE_D_ELEMENTS):
				return "Gain : Résistance Élémentaire dans un nombre variable d'éléments"
			case(Action.DOMMAGE_LUMIERE):
				return "Dommage : Lumière"
			case(Action.SOIN_LUMIERE):
				return "Soin : Lumière"
			case(Action.JOB_MODIFIE_LA_QUANTITE_D_OBJETS_RECOLTEE):
				return "Job : Modifie la quantité d'objets récoltée"