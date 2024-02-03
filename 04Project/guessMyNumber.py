''' guess my number game
    Jesse Higgins
    1/29/2024
'''
import random
import math

number = random.randint(0,100)
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

def main():

    guess = int(input("Guess a number: "))
    #print(number)
    while number != guess:
        previousdifference = guessHighLow(number, guess)
        guess = int(input("Guess a number: "))
        guessHotCold(previousdifference, number, guess)
    if guess == number:
        print("Correct!")


if __name__ == "__main__":
    main()