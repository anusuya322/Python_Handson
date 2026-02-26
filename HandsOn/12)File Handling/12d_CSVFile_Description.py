import json
with open("items.json", "r") as file:
    data = json.load(file)
for item in data:
    if item["price"] > 50:
        print(item["description"])