"""
Return to your first homework assignments, when you described your favorite song. 
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through 
each item in the dictionary and prints out it's key and then it's value.

Extra Credit:
Create a function that allows someone to guess the value of any key in the dictionary, 
and find out if they were right or wrong. This function should accept two parameters: Key and Value. 
If the key exists in the dictionary and that value is the correct value, 
then the function should return true. In all other cases, it should return false.
"""
SongDict = {
    'performer' : 'Paramore',
    'album' : 'After Laughter',
    'song' : 'Hard Times',
    'year of release' : 2017,
    'genre' : 'New wave / Post-punk',
    'nominations' : 'Teen Choice Award for Choice Music – Rock Song',
    'duration in seconds' : 182,
    'main vocal' : 'Hayley Williams'
}

SongDict['duration in minutes'] = SongDict['duration in seconds'] / 60
SongDict['info'] = SongDict['main vocal'] + ' (born December 27, 1988) is an American singer, songwriter, musician\n\
who is best known as the lead vocalist and primary songwriter\n\
of the rock band Paramore.'
SongDict['songwriters'] = SongDict['main vocal'] + ' and ‎Taylor York'

for key in SongDict:
    print(key + ': ',end='')
    print(SongDict[key])

def guessValueOfKey(key, value):
    key = key.lower()
    if key in SongDict:
        guess = SongDict[key]
        if(isinstance(guess, int)):
            guess = str(guess)
        else:
            guess = guess.lower()
            value = value.lower()
        if(value ==  guess): 
            return True
        else:
            return False
    return False

print(guessValueOfKey('Performer','Paramore'))
print(guessValueOfKey('Year of release', 2021))
print(guessValueOfKey('Songss', 'Hard Times'))
print(guessValueOfKey('Main vocal','Hayley Williams'))

print(guessValueOfKey(input('Enter the topic: '), input('Enter your guess: ')))