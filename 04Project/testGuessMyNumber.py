''' Guess my number game test
    Jesse Higgins
    1/29/2024
'''
#Import Libraries
import random
import math
import sys

turns = 0

def guessHighLow(number, guess, max):
    ''' compares guess to number and prints if it is high or low and returns difference
        params: none
        return: previousdifference
    '''

    while guess < 0 or guess > max:
        guess = int(input("Please guess a number 0 - " + str(max) + ": "))
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
    while guess < 0 or guess > max:
        guess = int(input("Please guess a number 0 - " + str(max) + ": "))

    difference = abs(number - guess)
    if difference < previousdifference:
         print("Hot")
    if difference > previousdifference:
         print("Cold")

def efficientGuess(number, guess, maxturn):
    ''' counts number of turns and evaluates if efficient when correct
        params: none
        returns: none'''
    while guess < 0 or guess > max:
        guess = int(input("Please guess a number 0 - " + str(max) + ": "))

    global turns 
    if number == guess and turns <= maxturn:
        print("Efficient")
    if number == guess and turns > maxturn:
         print("Not Efficient")

    turns = turns + 1
    print("Number of turns: ", turns)
    

def main():

    #Test 1 good data: should see result
    print("Expected result: \n'Too High'")
    print("Actual result: ", guessHighLow(56, 65, 100), "\nExpected result: '9'")

    # #Test 2 bad data: should be prompted to enter number 0 - 50
    print("Should prompt user to enter new number 0 - 50 ")
    guessHighLow(45, 110, 50)

    #Test 3 good data: should see Hot
    print("Actual result: ")
    guessHotCold(10, 50, 45, 100)
    print("Expected result: \nHot")

    #Test 4 bad data: should be prompted to enter new number 0 - 100
    print("Expected result: \nPlease guess a number 0 - 100:")
    print("Actual result: ")
    guessHotCold(20, 50, 101, 100)

if __name__ == "__main__":
    main()