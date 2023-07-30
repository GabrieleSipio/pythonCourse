'''Part 2 Lis and Dictionary specific'''
from Classes.RandomStructGenerator import RandomStructGenerator


strucType = "list"
while (strucType.lower() != "quit"):
    strucType = input("what data structure you want to generate?\n")
    lenght = int(input(f"how long the {strucType.lower()} must be?\n"))
    randomStruct = RandomStructGenerator(strucType, lenght)
    newData = randomStruct.CreateRandomStruct()
    print(newData)
    if(strucType.lower() == "list"):
        print(f"reversed list:\n{newData[::-1]}")
    strucType = input("want to generate another structure or quit?\n")
