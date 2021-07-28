import sys 
from termcolor import colored, cprint

import colorama #to display color instead of characters
colorama.init()

listColumn = []
listTable = []
redCircle = colored('O', 'red', attrs=['bold'])
greenCircle = colored('O', 'green', attrs=['bold'])

for i in range(7):
    listColumn = []
    for j in range(6):
        listColumn.append('O')
    listTable.append(listColumn)

def drawTable():
    print_whiteCircle_on_Blue = lambda x: cprint(x, 'grey', 'on_blue',end='')

    for row in range(6):
        for tableColumn in range(15):
            column = int(tableColumn / 2)
            if tableColumn % 2 == 0:
                print_whiteCircle_on_Blue(' ')
            else:
                print_whiteCircle_on_Blue(listTable[column][row])   
        print()
    print()

def checkWin(row, column, coloredCircle):
    #vertical check
    vertCounter = 0
    for i in range (4):
        try:
            if listTable[column][row + i] == coloredCircle:
                vertCounter += 1
        except IndexError:
            continue
        
    if vertCounter == 4:
        if coloredCircle == redCircle:
            cprint("Player 1 won", 'red', attrs=['bold','blink'], file=sys.stderr)
            return True
        else:
            cprint("Player 2 won", 'red', attrs=['bold','blink'], file=sys.stderr)
            return True

def putCircle(column, coloredCircle):
    columnList = listTable[column]
    length = len(columnList)
    for i in range(length - 1, -1, -1):
        if(columnList[i] == 'O'):
            columnList[i] = coloredCircle
            if checkWin(i, column, coloredCircle):
                drawTable()
                exit()
            break

player = 1
while True:
    drawTable()
    column = int(input('Enter column: '))
    if column > 0 and column < 8:
        column -= 1
        if listTable[column][0] != redCircle and listTable[column][0] != greenCircle:
            if(player == 1):
                putCircle(column, redCircle)     
                player = 2
            else:
                putCircle(column, greenCircle) 
                player = 1
        else:
            cprint(str(column + 1) + ". column is full!", 'red', attrs=['bold'], file=sys.stderr)
    else:
        cprint("Invalid input !", 'red', attrs=['bold'], file=sys.stderr)
