import json as js

with open("actions.json", 'r') as f:
    data = js.load(f)

d: dict = {}

for action in data:
    
    d[action["definition"]["id"]] = action["definition"]["effect"]



for key, value in d.items():
    print(f"{value.upper()} = {key}")
