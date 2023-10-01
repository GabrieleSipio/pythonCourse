'''Part 2 Lis and Dictionary specific'''
from Classes.RandomStructGenerator import RandomStructGenerator
import random
from collections import Counter


def playWithList(inputList):
    print(f"reversed list:\n{inputList[::-1]}")
    inputList.sort()
    print(f"sorted list:\n{inputList}")
    first, second, *other = inputList
    print(f'Unpacked list {first}, {second}, {other}')
    print(f'old list {inputList}')
    print(f'list before pop {other}')
    print(f'removed item {other.pop(random.randint(0,len(other)-1))}')
    print(f'list after pop {other}')
    # oppositeList = list(map(lambda x: x * -1, newData))
    oppositeList = [x * -1 for x in inputList]
    # evenList = list(filter(lambda x: x % 2 == 0, newData))
    evenList = [x for x in inputList if x % 2 == 0]
    # unevenList = list(filter(lambda x: not x % 2 == 0, newData))
    unevenList = [x for x in inputList if not x % 2 == 0]
    print(f'original list {inputList}')
    print(f'opposite list {oppositeList}')
    print(f'even list {evenList}')
    print(f'uneven list {unevenList}')
    oppositeList.sort()
    
    evenList.sort()
    unevenList.sort()
    print(f'opposite sorted list {oppositeList}')
    print(f'even sorted list {evenList}')
    print(f'uneven sorted list {unevenList}')
    print(f'zipped list {list(zip(evenList, unevenList))}')

def MostOccurredCharacter(inputString):
    # charDict = {}
    # for letter in inputString:
    #     if (letter not in charDict):
    #         charDict.update({letter: 1})
    #     else:
    #         charDict[letter] += 1
    charDict = dict(Counter(inputString))
    print(f'Letter occurrences {charDict}')
    new_val = max(charDict, key= lambda x: charDict[x])
    print(f'Most occured letter ({new_val}: {charDict[new_val]})')

strucType = "list"
while (strucType.lower() != "quit"):
    strucType = input("what data structure you want to generate?\n")
    if (strucType.lower() == "ex"):
        sentence = "This is a common intyerview question."
        MostOccurredCharacter(sentence.replace(" ", ""))
    lenght = int(input(f"how long the {strucType.lower()} must be?\n"))
    randomStruct = RandomStructGenerator(strucType, lenght)
    newData = randomStruct.CreateRandomStruct()
    print(newData)
    if (strucType.lower() == "list"):
        playWithList(newData)

    strucType = input("want to generate another structure or quit?\n")
