''' This file will be used in Project 3.
    NAME: Jesse Higgins
    DATE: January 24, 2024
    Description of Project 3: Project three introduces command line arguments and then builds functions
'''
# Imported libraries
import random
import sys

# Do not need a parameter because no input required, only a local variable for the radndint function and return
def getSuit():
    ''' getSuit - returns str with suit
            params: none
            returns: str of suit of card'''
    
    # Randomizing function to assign random int between 1 and 4 to variable suit
    suit = random.randint(1, 4)

    # Conditionals to assign str value based on int value
    if suit == 1:
        suit = "Diamonds"
    elif suit == 2:
        suit = "Hearts"
    elif suit == 3:
        suit = "Clubs"
    else:
        suit = "Spades"
    
    return suit 

def getValue():
    ''' getValue - returns str with value
            params: none
            returns: str of value of card'''
    
    # Randomizing function to assign random int between 1 and 4 to variable suit
    value = random.randint(0, 12)

    # Conditionals to assign str value based on int value
    if value == 0:
        value = "Ace"
    elif value == 11:
        value = "Jack"
    elif value == 12:
        value = "Queen"
    elif value == 13:
        value = "King"
    else:
        value = str(value)
    
    # Returns variable back to main function to be used in print function etc...
    return value

# Parameters are the variables to initialize only in this function but inputed from getSuit and getValue functions and returned to main
def printCard(value, suit):
    ''' printCard - prints parameters value and suit
        parameters: value, suit
        return: none'''
    
    # Print card
    print(value, "of", suit)

def main():
    ''' main - Determines if user inputted color matches random card
        parameters:  color
        return: string if color matched'''
    # Assign function returns to variables
    value = getValue()
    suit = getSuit()

    # Print Card
    printCard(value, suit)

    # Command line color input
    color = sys.argv[1]
    print("User entered:",color)

    # Conditionals checking suit and color, tried to use or operator but didnt work
    if suit == "Diamonds" and color == "red":
        print("Card is of the same color")
    elif suit == "Hearts" and color == "red":
        print("Card is of the same color")
    elif suit == "Clubs" and color == "black":
        print("Card is of the same color")
    elif suit == "Spades" and color == "black":
        print("Card is of the same color")
    else:
        print("Card is not of the same color")


#remember to put in the lines to call main() that are described in part 6
if __name__ == "__main__":
    main()
