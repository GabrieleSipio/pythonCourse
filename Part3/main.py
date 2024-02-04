'''working with data structures and classes but with exception handling'''
import sys
sys.path.append('/home/jager/Documenti/GitHub/pythonCourse')
# sys.path.append('..\\pythonCourse') when on Windows
from Classes.RandomStructGenerator import RandomStructGenerator
from Classes.FileManagement import FileManagement
import os



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
                    if (input("Want to write to files? ") == 'yes'):
                        path = "Files/FileManagement"
                        fileManager = FileManagement(path)
                        fileManager.WriteDictIntoFile(randDict)
                        fileManager.CreateZip()
                case 'ex':
                    print(f'Saving {action}')
                    test = os.listdir(path="Files/FileManagement")
                    print(f'{test}')
                case 'q':
                    break
                case _:
                    raise ValueError(f"ERR | Invalid action: {action}")
        except ValueError:
            print(f'Invalid action: {action}')


if __name__ == '__main__':
    payWithDataStructures()
