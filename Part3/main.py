'''working with data structures and classes but with exception handling'''
import sys
sys.path.append('/home/jager/Documenti/GitHub/pythonCourse')
from Classes.RandomStructGenerator import RandomStructGenerator
def payWithDataStructures():
    action = ''
    while action!= 'q':
        try:
            action = input('- Generate List and do some stuff (l)\n- Generate Dictionary and do stuff (d)\n- Do an excercise (ex)\n- Quit the program (q)\n- Enter action: ')
            if action == 'q':
                break
            elif action.lower() == 'l':
                print(f'Excecuting {action}')
                strLenght = input('Enter the length of the list: ')
                listGenerator = RandomStructGenerator("list",int(strLenght))
                randList = listGenerator.CreateRandomList()
                listGenerator.PlayWithList(randList)
            elif action =='d':
                print(f'Saving {action}')
            elif action =='ex':
                print(f'Saving {action}')
            else:
                raise ValueError(f"ERR | Invalid action: {action}")
        except ValueError:
            print(f'Invalid action: {action}')

if __name__ == '__main__':
    payWithDataStructures()
