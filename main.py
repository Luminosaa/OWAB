from utils.item import Item, Rarity, Effect, Action
import json

if __name__ == "__main__":

    with open("jsons/items.json", "r") as f:
        items = json.load(f)

    objets = []

    for item in items:

        name: str = item["title"]["fr"]
        level: int = item["definition"]["item"]["level"]
        rarity: Rarity = [name if member.value == item["definition"]["item"]["baseParameters"]["rarity"] else Rarity.COMMUN for name, member in Rarity.__members__.items()][0]
        desc: str = item["description"]["fr"]

        objet: Item = Item(name, level, rarity, desc)
        print(objet.__str__())

        for effect in item["definition"]["equipEffects"]:

            print(effect.keys())

            action: Action = [name if member.value == effect["effect"]["definition"]["id"] else Action.DOMMAGE_NEUTRE for name, member in Action.__members__.items()][0]
            valeur: int = effect["effect"]["definition"]["params"][0]
            effet: Effect = Effect(action, int(effect["effect"]["definition"]["params"][0]["value"]))

            objet.add_effect(effet)

    for objet in objets:
        print(objet.__str__())

    # test = Item("test", 1, Rarity.COMMUN, "test item")
    # test.add_effect(Effect(Action.GAIN_MAITRISE_ELEMENTAIRE_DANS_UN_NOMBRE_VARIABLE_D_ELEMENTS, 10).__str__())
    # print(test.__str__())