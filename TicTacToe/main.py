def drawTable(field):
    for row in range(5):
        if(row % 2 == 0):
            valueRow = int(row / 2)
            for column in range(5):
                valueColumn = int(column / 2)
                if(column == 4):
                    print(field[valueRow][valueColumn])
                    continue
                if(column % 2 == 0):
                    print(field[valueRow][valueColumn],end='')
                else:
                    print('|',end='')
        else:
            print('-----')

def checkWin(field, row, column):
    value = field[row][column]

    diagCounter = 0
    vertCounter = 0
    horzCounter = 0
    if(row == column):
        diagCounter = 0
        for i in range(3):
            j=i
            if(value == field[i][j]):
                diagCounter +=1
    elif(row == 2 - column):
        diagCounter = 0
        for i in range(3):
            j = 2 - i
            if(value == field[i][j]):
                diagCounter +=1
    
    for i in range(3):
            if value == field[row][i]:
                horzCounter += 1
            if value == field[i][column]:
                vertCounter += 1

    won = False
    if(diagCounter == 3):
        won = True
    elif(vertCounter == 3):
        won = True
    elif(horzCounter == 3):
        won = True

    if(won):
        if(value == 'X'):
                print('Player 1 won')
        else:
                print('Player 2 won')
        exit()
    elif(MoveNumber == 9):
        print('Draw (tie)')
        exit()

FieldsList = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
Player = 1
MoveNumber = 0
while True:
    print('Player',Player)
    MoveRow = int(input('Enter a row: '))
    MoveColumn = int(input('Enter a column: '))
    
    if(MoveRow > 0 and MoveRow < 4 and MoveColumn > 0 and MoveColumn < 4):
        MoveRow -=1
        MoveColumn -=1
        if Player == 1:
            if FieldsList[MoveRow][MoveColumn] == ' ':
                FieldsList[MoveRow][MoveColumn] = 'X' 
                drawTable(FieldsList)
                MoveNumber += 1
                checkWin(FieldsList,MoveRow,MoveColumn)
                Player = 2
        else:
            if FieldsList[MoveRow][MoveColumn] == ' ':
                FieldsList[MoveRow][MoveColumn] = 'O'
                drawTable(FieldsList)
                MoveNumber += 1
                checkWin(FieldsList,MoveRow,MoveColumn)
                Player = 1  


    