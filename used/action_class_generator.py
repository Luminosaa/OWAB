import unidecode as ud
import json as js

with open("../jsons/actions.json", 'r') as f:
    
    data = js.load(f)

with open("../utils/enumerations/action.py", 'w') as f:

    action_dict: dict = {}

    f.write("from enum import Enum\n\n")
    f.write("class Action(Enum):\n\n")

    for action in data:
        
        if action["definition"]["id"] != 42:

            effect: str = action["definition"]["effect"]
            enum_version: str = ud.unidecode(effect).replace('%', "POURCENTAGE").replace('\'', '_').replace(')', '').replace('(', '').replace(': ', '').replace(' ', '_').upper()

            action_dict[enum_version] = effect

            f.write('\t' + enum_version + " = " + str(action["definition"]["id"]) + "\n")

    f.write("\n\tdef __str__(self) -> str:\n")

    f.write("\n\t\tmatch(self):\n")

    for key, value in action_dict.items():

        f.write("\n\t\t\tcase(Action." + key + "):\n\t\t\t\treturn \"" + value + "\"")