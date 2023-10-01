import random


class RandomStructGenerator:
    def __init__(self, strucType, lenght):
        self.strucType = strucType
        self.lenght = lenght

    def CreateRandomList(self):
        '''create a list with random in values'''
        myList = []
        myList.extend([random.randint(-100, 100) for i in range(self.lenght)])
        return myList

    def CreateRandomDict(self):
        '''create a dict with random values'''
        myDict = {}
        for i in range(self.lenght):
            myDict.update({f"key{i}": random.randint(-100, 100)})
        return myDict

    def CreateRandomStruct(self):
        '''Create a random data structure'''
        return self.CreateRandomList() if self.strucType.lower() == "list" else self.CreateRandomDict()
    
    def playWithList(self,inputList):
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