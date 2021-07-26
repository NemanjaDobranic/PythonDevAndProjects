#OS module in Python provides functions for interacting with the operating system.
import os

def drawPlayingBoard(rows, columns):
    size = os.get_terminal_size()
    if(columns <= size[0] and rows <= size[1]):
        if(rows == columns):
            for row in range((2*rows-1)):
                for column in range(columns):
                    if row % 2 == 0:                
                        if column != columns - 1:
                            print(' |',end='')
                        else:
                            print(' ')
                    else:
                        print('-'*(2*columns -1))
                        break
            return True
        else:
            print("Rows is not equal to columns")
            return False
    else:
        return False

drawPlayingBoard(5,5)
print('\n'*2)
drawPlayingBoard(8,8)
print('\n'*2)
drawPlayingBoard(5,8)
print('\n'*2)
if(not drawPlayingBoard(1024,1024)):
    print('Playing board can not be drawn without wrapping!')

