'''Python course part 1'''
import json

helloWorld = "Hello World!"
print(helloWorld)
x = 1
print(x)
print(f"{helloWorld} this is string interpolation attempt {x}")
aDict = {"a": 54, "b": 87, "c": 56, "d": 875}
jsonString = json.dumps(aDict)
with open("data.json", "w+") as jsonFile:
    jsonFile.write(jsonString)
with open("data.json", "r+") as jsonFile:
    jsonContent = jsonFile.read()
    aDict = json.loads(jsonContent)
    print(f"current dict {aDict}")
newValue = int(input("insert new value: "))
with open("data.json", "w+") as jsonFile:
    aDict.update({"e": newValue})
    print(f"updated dict {aDict}")
    checkPositives = all(value > 0 for value in (aDict.values()))
    message = "All positives!" if checkPositives else "Not all positives!"
    print(message)
    newJsonString = json.dumps(aDict, indent=4)
    jsonFile.write(newJsonString)
