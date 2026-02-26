import json
with open("demo_json.json","r") as f:
    data=json.load(f)
    print(data)
    print("Value:",data["Name"])
    print("Value:",data["Dept"])