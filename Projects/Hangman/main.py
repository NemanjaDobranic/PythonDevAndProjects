from os import system, name

hangman = ['|','O','|','|','/','\\']
gallow = [[''],['+'],['='],['+'],[''],[''],['']]
def drawGallows():
    for row in range(7):
        for column in range(12):
            if row == 0:
                if column == 3 or column == 6:
                    print('+',end='')
                elif column == 4 or column == 5:
                    print('-',end='')
                else:
                    print(' ',end='')
            elif row == 6:
                print('=',end='')
            else:
                if column == 6:
                    print('|',end='')
                else:
                    print(' ',end='')
        print()

def clear():
    # Windows
    if name == 'nt':
        system('cls')
    
    # for Mac and Linux
    else:
        system('clear')
        
def player2(word):
    drawGallows()
    

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
