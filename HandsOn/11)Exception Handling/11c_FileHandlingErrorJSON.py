import json
import json.decoder
try:
    with open("D:/HCLTech_session2/DSA_TrainingClasses/LinkedList.txt","r") as f:
        data=json.load(f)
        print(data)
except FileNotFoundError:
    print("File not found")
except json.decoder.JSONDecodeError:
    print("JSON decoding error")
