from utils.item import Item, Rarity, Effect, Action
import json

if __name__ == "__main__":

    with open("jsons/items.json", "r") as f:
        items = json.load(f)

    objets = []

    action_dict: dict = {str(member.value): name for name, member in Action.__members__.items()}

    for item in items:

        name: str = item["title"]["fr"]
        level: int = item["definition"]["item"]["level"]
        rarity: Rarity = [name if member.value == item["definition"]["item"]["baseParameters"]["rarity"] else Rarity.COMMUN for name, member in Rarity.__members__.items()][0]
        desc: str = item["description"]["fr"] if "description" in item else "Pas de description"

        objet: Item = Item(name, level, rarity, desc)

        for effect in item["definition"]["equipEffects"]:

            action: Action = action_dict[str(effect["effect"]["definition"]["actionId"])] if str(effect["effect"]["definition"]["actionId"]) in action_dict else None

            valeur: int = effect["effect"]["definition"]["params"][0] if len(effect["effect"]["definition"]["params"]) > 0 else 0
            effet: Effect = Effect(action, valeur)

            objet.add_effect(effet)

        objets.append(objet)


    for objet in objets:
        print(objet.__str__())

    print(len(objets))