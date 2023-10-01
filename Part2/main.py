'''Part 2 Lis and Dictionary specific'''
from Classes.RandomStructGenerator import RandomStructGenerator
import random
from collections import Counter




def MostOccurredCharacter(inputString):
    # basic resolution
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
        randomStruct.PlayWithList(newData)

    strucType = input("want to generate another structure or quit?\n")
