'''Python course part 1'''
import json
import random


def NegativeToPositive(x):
    '''check if an element is negative and makes it positive'''
    return x * -1 if x < 0 else x


def TakeEven(inputDict):
    '''takes the even numbers of a dict'''
    return {key: [idx for idx in val if not idx % 2]  
          for key, val in inputDict.items()}  


def TakeOdd(inputDict):
    '''takes the odd numbers of a dict'''
    return {key: (lambda val: val % 2) for key, val in inputDict.items()}


def CreateRandomDict(dictLenght):
    '''create a dict with random values'''
    myDict = {}
    for i in range(dictLenght):
        myDict.update({f"key{i}": random.randint(-100, 100)})
    return myDict


helloWorld = "Hello World!"
print(helloWorld)
tries = 1
print(tries)
print(f"{helloWorld} this is string interpolation attempt {tries}")
dictLenght = int(input("instert dict lenght: "))
aDict = CreateRandomDict(dictLenght)
evenDict = TakeEven(aDict)
oddDict = TakeOdd(aDict)
path = "Files/data.json"
pathEven = "Files/dataEven.json"
pathOdd = "Files/dataOdd.json"
jsonString = json.dumps(aDict)
with open(path, "w+") as jsonFile:
    jsonFile.write(jsonString)
with open(pathEven, "w+") as jsonFile:
    print(f"even values in dict:\n{evenDict}")
    jsonFile.write(json.dumps(evenDict, indent=4))
with open(pathOdd, "w+") as jsonFile:
    print(f"odd values in dict:\n{oddDict}")
    jsonFile.write(json.dumps(oddDict, indent=4))
with open(path, "r+") as jsonFile:
    jsonContent = jsonFile.read()
    aDict = json.loads(jsonContent)
    print(f"current dict {aDict}")
    checkPositives = all(value > 0 for value in (aDict.values()))
    message = "All positives!" if checkPositives else "Not all positives!"
    print(f"updated dict {aDict}")
    print(message)
    if not checkPositives:
        aDict = {k: NegativeToPositive(v) for k, v in aDict.items()}
        evenDict = {k: NegativeToPositive(v) for k, v in evenDict.items()}
        oddDict = {k: NegativeToPositive(v) for k, v in oddDict.items()}
        print(f"balanced dictionary:\n{aDict}")
        print(f"balanced even dictionary:\n{evenDict}")
        print(f"balanced odd dictionary:\n{oddDict}")
with open(path, "w+") as jsonFile:
    jsonFile.write(json.dumps(aDict, indent=4))
with open(pathEven, "w+") as jsonFile:
    jsonFile.write(json.dumps(evenDict, indent=4))
with open(pathOdd, "w+") as jsonFile:
    jsonFile.write(json.dumps(oddDict, indent=4))
