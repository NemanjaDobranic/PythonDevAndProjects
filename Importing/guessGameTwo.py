import random as r
import time as t

randNumber = r.uniform(1,10000)
upperBound = 10000
lowerBound = 1
print('Number to find:',randNumber)

start = t.time()
while True:
    guess = (upperBound + lowerBound) / 2
    if(guess == randNumber):
        print('Number',guess,'is found!')
        print('Time passed:',t.time() - start,'seconds')
        break
    elif guess < randNumber:
        lowerBound = guess
    else:
        upperBound = guess
