from random import randint

randNumber = randint(1,100) #[1,100]

while True:
    guess = int(input('Please enter your guess: '))
    if(guess == randNumber):
        print('Your guess is correct')
        break
    elif guess < randNumber:
        print('Too low')
    else:
        print('Too  high')