"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
Extra credit:
Print all prime numbers

Important: Prime numbers are 3 and 5, so 3 is Fizz and Prime and 5 is Buzz and Prime. 1 is not prime number
"""

def isPrimeNumber(number):
    isPrime = True

    if number == 1:
        isPrime = False
        return isPrime

    for counter in range(2,number):
        if number % counter == 0:
            isPrime = False
            return isPrime

    return isPrime

for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print(str(number) + " FizzBuzz")
    elif number % 3 == 0:
        if not isPrimeNumber(number):
            print(str(number) + " Fizz")
        else: 
            print(str(number) + " Fizz and Prime")
    elif number % 5 == 0:
        if not isPrimeNumber(number):
            print(str(number) + " Buzz")
        else:
            print(str(number) + " Buzz and Prime")
    elif isPrimeNumber(number):
        print(str(number) + " Prime")
    else:
        print(number)


    