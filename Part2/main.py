'''Part 2 Lis and Dictionary specific'''
from Classes.RandomStructGenerator import RandomStructGenerator
import random


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
        first, second, *other = newData
        print(f'Unpacked list {first}, {second}, {other}')
        print(f'old list {newData}')
        print(f'list before pop {other}')
        print(f'removed item {other.pop(random.randint(0,len(other)-1))}')
        print(f'list after pop {other}')
        # oppositeList = list(map(lambda x: x * -1, newData))
        oppositeList = [x * -1 for x in newData]
        # evenList = list(filter(lambda x: x % 2 == 0, newData))
        evenList = [x for x in newData if x % 2 == 0]
        # unevenList = list(filter(lambda x: not x % 2 == 0, newData))
        unevenList = [x for x in newData if not x % 2 == 0]
        print(f'original list {newData}')
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

    strucType = input("want to generate another structure or quit?\n")
