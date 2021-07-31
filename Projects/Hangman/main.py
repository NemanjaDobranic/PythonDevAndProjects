from os import system, name

gallows = []

def drawScene():
    for i in range(len(gallows)):
        for j in range(len(gallows[i])):
            print(gallows[i][j],end='')
        print()

def createGallows():
    for row in range(7):
        gallows.append([])
        for column in range(12):
            if row == 0:
                if column == 3 or column == 6:
                    gallows[row].append('+')
                elif column == 4 or column == 5:
                    gallows[row].append('-')
                else:
                    gallows[row].append(' ')
            elif row == 6:
                gallows[row].append('=')
            else:
                if column == 6:
                    gallows[row].append('|')
                else:
                    gallows[row].append(' ')

def clear():
    # Windows
    if name == 'nt':
        system('cls')
    
    # for Mac and Linux
    else:
        system('clear')
        
def player2(word):
    createGallows()
    drawScene()

def player1():
    word = input('Enter a word: ')
    while len(word) == 0:
        print('Word can not be empty')
        word = input('Please try again: ')
    clear() 
    return word

def main():
    word = player1()
    player2(word)


main()
