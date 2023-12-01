import random


class RandomStructGenerator:
    def __init__(self, strucType, lenght):
        self.strucType = strucType
        self.lenght = lenght

    @property
    def strucType(self):
        return self.__strucType

    @strucType.setter
    def strucType(self, var):
        if var.lower() != "list" and var.lower() != "dict":
            raise ValueError("value must be a list or dict")
        self.__strucType = var

    @property
    def lenght(self):
        return self.__lenght

    @lenght.setter
    def lenght(self, var):
        if var < 0:
            raise ValueError("value must be positive")
        self.__lenght = var

    def __createRandomList(self):
        '''create a list with random in values'''
        myList = []
        myList.extend([random.randint(-100, 100)
                      for i in range(self.__lenght)])
        return myList

    def __createRandomDict(self):
        '''create a dict with random values'''
        myDict = {}
        for i in range(self.__lenght):
            myDict.update({f"key{i}": random.randint(-100, 100)})
        return myDict
    
    def __negativeToPositive(self, x):
        '''check if an element is negative and makes it positive'''
        return x * -1 if x < 0 else x
    
    def __takeEven(self, inputDict):
        '''takes the even numbers of a dict'''
        return {key: val for key, val in inputDict.items() if not val % 2}

    def __takeOdd(self, inputDict):
        '''takes the odd numbers of a dict'''
        return {key: val for key, val in inputDict.items() if val % 2}
    
    def CreateRandomStruct(self):
        '''Create a random data structure'''
        return self.__createRandomList() if self.strucType.lower() == "list" else self.__createRandomDict()

    def PlayWithList(self, inputList):
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

    def PlayWithDictionary(self, inputDict):
        print(f'play with dict {inputDict}')
        evenDict = self.__takeEven(inputDict)
        print(f'Even dict {evenDict}')
        oddDict = self.__takeOdd(inputDict)
        print(f'Odd dict {evenDict}')
        balancedDict = {k: self.__negativeToPositive(v) for k, v in inputDict.items()}
        print(f"balanced dictionary:\n{balancedDict}")
        balancedEvenDict = {k: self.__negativeToPositive(v) for k, v in evenDict.items()}
        print(f"balanced even dictionary:\n{balancedEvenDict}")
        balancedOddDict = {k: self.__negativeToPositive(v) for k, v in oddDict.items()}
        print(f"balanced odd dictionary:\n{balancedOddDict}")