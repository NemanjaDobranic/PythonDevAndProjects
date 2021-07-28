numOfParticipant = int(input('Enter number of participants: '))
Participants = []

counter = 0

while(counter < numOfParticipant):
    Participant = []

    name = input('Please, enter your name: ')
    Participant.append(name)
    country = input('Please, enter your country of origin: ')
    Participant.append(country)
    age = int(input('Please enter your age: '))
    Participant.append(age)

    Participants.append(Participant)
    counter += 1

outputFile = open('participants.txt','w')
for participant in Participants:
    for info in participant:
        outputFile.write(str(info))
        outputFile.write(' ')
    outputFile.write('\n')
outputFile.close()

inputList = []
inputFile = open('participants.txt','r')
for line in inputFile:
    infoAboutPart = line.strip('\n').split()    #strip Remove spaces (default) at the beginning and at the end of the string
    inputList.append(infoAboutPart)             #split separates strings into list based on spacing (default)

Age = {}

for participant in inputList:
    tempAge = int(participant[-1])    #-1 last element in list
    if tempAge in Age:
        Age[tempAge] += 1
    else:
        Age[tempAge] = 1

Oldest = 0
Youngest = 100
mostOccuringAge = 0
counter = 0
for age in Age:
    if Oldest < age:
        Oldest = age
    if Youngest > age:
        Youngest = age
    if(Age[age] > counter):
        counter = Age[age]
        mostOccuringAge = age

print('Oldest participant is',Oldest,'years old.')
print('Youngest participant is',Youngest,'years old.')
print('The biggest age group is',mostOccuringAge,'years old with',counter,'members.')

Countries = {}

for participant in inputList:
    tempCountry = participant[1]
    if tempCountry in Countries:
        Countries[tempCountry] += 1
    else:
        Countries[tempCountry] = 1
        
print('Countries that attended:',Countries)
