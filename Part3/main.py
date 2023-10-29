'''working with data structures and classes but with exception handling'''
from Classes.RandomStructGenerator import RandomStructGenerator
import os
import sys
sys.path.append('/home/jager/Documenti/GitHub/pythonCourse')


def payWithDataStructures():
    action = ''
    while action != 'q':
        try:
            action = input(
                '- Generate List and do some stuff (l)\n- Generate Dictionary and do stuff (d)\n- Do an excercise (ex)\n- Quit the program (q)\n- Enter action: ')
            match action.lower():
                case 'l':
                    print(f'Excecuting {action}')
                    strLenght = input('Enter the length of the list: ')
                    listGenerator = RandomStructGenerator(
                        "list", int(strLenght))
                    randList = listGenerator.CreateRandomStruct()
                    # print(listGenerator.__lenght)
                    listGenerator.PlayWithList(randList)
                case 'd':
                    print(f'Executing {action}')
                    dictLenght = input('Enter the lenght of the dictionary: ')
                    dictGenerator = RandomStructGenerator(
                        "dict", int(dictLenght))
                    randDict = dictGenerator.CreateRandomStruct()
                    dictGenerator.PlayWithDictionary(randDict)
                case 'ex':
                    print(f'Saving {action}')
                    test = os.path.isdir("Files")
                    print(f'{test}')
                case 'q':
                    break
                case _:
                    raise ValueError(f"ERR | Invalid action: {action}")
        except ValueError:
            print(f'Invalid action: {action}')


if __name__ == '__main__':
    payWithDataStructures()
