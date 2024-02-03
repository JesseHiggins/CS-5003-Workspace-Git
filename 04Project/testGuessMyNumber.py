''' guess my number game
    Jesse Higgins
    1/29/2024
'''
import random
import math

def guessHighLow(number):
    ''' compares guess to number and prints if it is high or low and returns difference
        params: none
        return: previousdifference
    '''
    guess = int(input("Guess a number 1 - 100: "))
    while guess < 1 or guess > 100:
        guess = int(input("Please guess a number 1 - 100: "))
    if guess < number:
            print("Too low")
    if guess > number:
            print("Too high")
    previousdifference = abs(number - guess)
    return previousdifference, guess

def guessHotCold(previousdifference, number, guess):
    ''' compares difference in guess to previous difference and prints hot or cold
        params: previousdifference
        return: none
    '''
    while guess < 1 or guess > 100:
        guess = int(input("Please guess a number 1 - 100: "))
    difference = abs(number - guess)
    if difference < previousdifference:
         print("Hot")
    if difference > previousdifference:
         print("Cold")

def main():

    number = random.randint(0,100)
    previousdifference, guess = guessHighLow(number)
    while number != guess:
        guessHotCold(previousdifference, number, guess)
        previousdifference, guess = guessHighLow(number)
    if guess == number:
        print("Correct!")

if __name__ == "__main__":
    main()