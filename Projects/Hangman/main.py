from os import system, name
from copy import deepcopy
from random import randint

hangman = ['|','O','/','|','\\','|','/',' ','\\']
gallows = []
answersIsFound = False

def load_words():
    with open('Projects\Hangman\words_alpha.txt') as word_file:
        valid_words = list(word_file.read().split())
    return valid_words

def showDashedLinesAndLetters(List1, List2):
    print()
    for wordNum in range(len(List1)):
        for letterNum in range(len(List1[wordNum])):
            if List1[wordNum][letterNum] == List2[wordNum][letterNum]:
                print('_',end='')
            else:
                print(List1[wordNum][letterNum],end='')
            print(' ',end='')
        print('  ',end='')
    print() 

#number argument == how many parts will be drawn
def addHangmanPartsToGallow(number):
    counter = 0
    number -= 1
    for row in range(len(gallows)):
        for column in range(len(gallows[row])):
            if row > 0 and row < 7:
                if counter > len(hangman) - 1 or counter > number:
                    break
                
                if row == 3 or row == 5:
                    if column >=2 and column <= 4:
                        gallows[row][column] = hangman[counter]
                        if hangman[counter] == ' ':
                            number += 1
                        counter += 1
                else:
                    if column == 3:
                        gallows[row][column] = hangman[counter]
                        counter += 1

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

def checkIfPlayerWin(recognizedLetters):
    allLettersFound = True

    for word in recognizedLetters:
        for letter in word:
            if letter != '_':
                allLettersFound = False

    return allLettersFound

def refreshGame(letterList, recognizedLetters):
    clear()
    drawScene()
    showDashedLinesAndLetters(letterList, recognizedLetters)

def player2(letterList):
    wrongAnswers = 0
    recognizedLetters = deepcopy(letterList)
    
    createGallows()
    refreshGame(letterList,recognizedLetters)

    answersIsFound = False
    while wrongAnswers < (len(hangman) - 1) and answersIsFound == False:
        print('Remaining attempts:',len(hangman) - wrongAnswers - 1)
        letter = input('Enter a letter: ').upper()
        
        while(len(letter) > 1):
            refreshGame(letterList,recognizedLetters)
            print('Enter letter not word!')
            letter = input('Enter a letter: ')

        Found = False
        for wordNum in range(len(recognizedLetters)):
            for letterNum in range(len(recognizedLetters[wordNum])):
                if recognizedLetters[wordNum][letterNum] == letter:
                    Found = True
                    recognizedLetters[wordNum][letterNum] = '_'

        if Found == False:
            wrongAnswers += 1
            addHangmanPartsToGallow(wrongAnswers)
        else:
            answersIsFound = checkIfPlayerWin(recognizedLetters)
        refreshGame(letterList,recognizedLetters)

    if answersIsFound:
        print('You WON the game :)')
    else:
        print('You LOST the game :(')

def player1():
    word = input('Enter a word: ')
    while len(word) == 0:
        print('Word can not be empty')
        word = input('Please try again: ')
    clear() 
    return word.upper()

def choosePlayMode():
    print('Choose play mode:')
    print('Player 1 vs Player 2 (press one)')
    print('Player vs Computer (press two)')
    playMode = int(input('> '))
    return playMode

def computer():
    words = load_words()
    randomPos = randint(0,len(words))
    randomWord = words[randomPos]
    randomWord = str(randomWord)

    return randomWord.upper()

def main():
    playMode = choosePlayMode()
    while(playMode != 1 and playMode != 2):
        print('Incorrect input')
        playMode = choosePlayMode()

    if playMode == 1:
        word = player1()
    else:
        word = computer()

    #Convert sentence to List of letters, so list(words) of lists(letters)
    wordList = word.split()
    letterList = []
    for word in wordList:
        letterList.append(list(word))
    player2(letterList)

main()
