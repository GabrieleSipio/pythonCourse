'''Part 2 Lis and Dictionary specific'''
from Classes.RandomStructGenerator import RandomStructGenerator
import random


def sortEven(item):
    '''Sort only even items in a list.'''
    return item % 2 == 0

strucType = "list"
while (strucType.lower() != "quit"):
    strucType = input("what data structure you want to generate?\n")
    lenght = int(input(f"how long the {strucType.lower()} must be?\n"))
    randomStruct = RandomStructGenerator(strucType, lenght)
    newData = randomStruct.CreateRandomStruct()
    print(newData)
    if (strucType.lower() == "list"):
        print(f"reversed list:\n{newData[::-1]}")
        newData.sort()
        print(f"sorted list:\n{newData}")
        first,second,*other = newData
        print(f'Unpacked list {first}, {second}, {other}')
        print(f'old list {newData}')
        print(f'list before pop {other}')
        print(f'removed item {other.pop(random.randint(0,len(other)-1))}')
        print(f'list after pop {other}')
        newData.sort(key=sortEven)
        print(f'sort Even {newData}')

    strucType = input("want to generate another structure or quit?\n")
