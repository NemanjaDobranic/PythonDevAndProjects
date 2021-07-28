"""
Options:
A) Read the file
B) Delete the file and start over
C) Append the file
D) Replace a single line
"""
import os

#fullPath = os.getcwd() + r'\File IO'
#Files = os.listdir(fullPath)
#or
Files = os.listdir('./File IO')
#print(Files)

fileName = input('Enter a file name: ')
fileNameList = fileName.split('.')
fileName = fileNameList[0]

fileName += '.txt'

def read():
    file = open('./File IO/' + fileName,'r')
    for line in file:
        print(line,end='')
    print()
    file.close()
    
def delAndStartOver():
    file = open('./File IO/' + fileName,'w')
    print('Content in',fileName,'is deleted')
    text = input('Enter new text content: ')
    file.write(text)
    print('Changes are saved')
    file.close()

def appendFile():
    file = open('./File IO/' + fileName,'a')
    while(True):
        text = input('Enter text you want to append: ')
        if(text != ''):
            file.write('\n')
            file.write(text)
            
            print('Want to add more text. ')
            while(True):
                print('To continue enter One(1) or Zero(0) for return: ',end='')
                option = input()
                if option == "1":
                    break
                elif option == "0":
                    file.close()
                    return
                else:
                    print('Invalid input!')


def write():
    file = open('./File IO/' + fileName,'w')
    text = input('Enter text you want to write: ')
    file.write(text)
    print('Changes are saved')
    file.close()

def replaceSingleLine():
    file = open('./File IO/' + fileName,'r+')   #read a file, and then write to it (overwriting any existing data), without closing and reopening
    linesList = file.readlines()
    i = 1
    for lines in linesList:
        print('Line',i,': ',end='')
        print(lines,end='')
        i += 1
    
    lineNum = 0
    while True:
        lineNum = int(input('\nEnter line number: '))
        if lineNum < 1 or lineNum > i:
            print('Invalid input')
        else:
            break
    text = input('Enter new text for editing line: ') 
    text += '\n'
    linesList[lineNum - 1] = text
    
    file.writelines(linesList)
    file.close()


def options():
    opt = '' 
    while(True):
        opt = input('Choose option [A, B, C, D, E]: ').upper()
        if opt == "A":
            read()
        elif opt == "B":
            delAndStartOver()
        elif opt == "C":
            appendFile()
        elif opt == "D":
            replaceSingleLine()
        elif opt == "E":
            exit()
        else:
            print('Invalid option!\nPlease try again')
            continue

if(fileName in Files):
    options()
else:
    write()





