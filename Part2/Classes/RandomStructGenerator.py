import random


class RandomStructGenerator:
    def __init__(self, strucType, lenght):
        self.strucType = strucType
        self.lenght = lenght

    def CreateRandomList(self):
        '''create a list with random in values'''
        myList = []
        for i in range(self.lenght):
            myList.append(random.randint(-100, 100))
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
