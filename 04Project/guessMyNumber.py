''' Guess my number game
    Jesse Higgins
    1/29/2024
'''
#Import Libraries
import random
import math
import sys

def guessHighLow(number, guess, max):
    ''' compares guess to number and prints if it is high or low and returns difference
        params: none
        return: previousdifference
    '''
    if guess < number:
            print("Too low")
    if guess > number:
            print("Too high")
    previousdifference = abs(number - guess)
    return previousdifference

def guessHotCold(previousdifference, number, guess, max):
    ''' compares difference in guess to previous difference and prints hot or cold
        params: previousdifference
        return: none
    '''
    difference = abs(number - guess)
    if difference < previousdifference:
         print("Hot")
    if difference > previousdifference:
         print("Cold")

def main():

    max = 100
    #max = int(sys.argv[1])

    #Assigns random value 1-max to number
    number = random.randint(0, max)

    #Asks for user input for guess
    guess = int(input("Guess a number 0 - " + str(max) + " :"))

    #Loop conditional to validate user input
    while guess < 0 or guess > max:
        guess = int(input("Please guess a number 0 - " + str(max) + ": "))
    #Loop to run guessing game with functions
    while number != guess:
        previousdifference = guessHighLow(number, guess, max)
        guess = int(input("Guess a number: "))
        while guess < 0 or guess > max:
            guess = int(input("Please guess a number 0 - " + str(max) + ": "))
        guessHotCold(previousdifference, number, guess, max)
    if guess == number:
        print("Correct!")


if __name__ == "__main__":
    main()