''' Guess my number game
    Jesse Higgins
    1/29/2024
'''
#Import Libraries
import random
import math
import sys

turns = 0

def guessHighLow(number, guess):
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

def guessHotCold(previousdifference, number, guess):
    ''' compares difference in guess to previous difference and prints hot or cold
        params: previousdifference
        return: none
    '''
    difference = abs(number - guess)
    if difference < previousdifference:
         print("Hot")
    if difference > previousdifference:
         print("Cold")

def efficientGuess(number, guess, maxturn):
    ''' counts number of turns and evaluates if efficient when correct
        params: none
        returns: none'''
    global turns 
    if number == guess and turns <= maxturn:
        print("Efficient")
    if number == guess and turns > maxturn:
         print("Not Efficient")

    turns = turns + 1
    print("Number of turns: ", turns)
    

def main():

    #Command line argument for max and find maxturns for efficientGuess
    max = int(sys.argv[2])
    maxturn = math.log2(max)

    #Assigns random value 1-max to number
    number = random.randint(0, max)

    #Asks for user input for guess
    guess = int(input("Guess a number 0 - " + str(max) + " :"))

    #Loop conditional to validate user input
    while guess < 0 or guess > max:
        guess = int(input("Please guess a number 0 - " + str(max) + ": "))

    #Loop to run guessing game with functions
    while number != guess:
        efficientGuess(number, guess, maxturn)
        previousdifference = guessHighLow(number, guess)
        guess = int(input("Guess a number: "))
        while guess < 0 or guess > max:
            guess = int(input("Please guess a number 0 - " + str(max) + ": "))
        guessHotCold(previousdifference, number, guess)
    if guess == number:
        efficientGuess(number, guess, maxturn)
        print("Correct!")


if __name__ == "__main__":
    main()