''' Spaceman Game
    Jesse Higgins
    2/12/2024
'''
#Import libraries
import random

#Create list
listwords = ["actor", "adult", "anger", "beach", "birth", "cross", "crowd", "dance", "chair", "bread", "brown", "guide", "happy", "heart", "drill", "metal", "judge", "rival", "paper", "sense", "texas"]


def random_word(list):
    ''' Function chooses random word
        params: list
        return: word
    '''
    word = list[random.randint(1, 20)]

    return word

def hide_word(word):
    ''' Function hides word with * characters
        params: word
        return: hidword
    '''
    hidword = "*" * len(word)

    return hidword

def find_replace(word, hidword, guess):
    ''' Function finds characters that matches guess and replaces it with letter.
        params: word, hidword, guess
        return: str of hidword list
    '''
    hidword = list(hidword)

    count = 0

    while count < len(word):
        if guess == word[count]:
            hidword[count] = guess
        count += 1

    return "".join(hidword)

def word_check(word, hidword, numguess):
    ''' Function checks if word is the same as hidword and prints correct message
        params: word, hidword, numguess
        return: none
    '''
    if word == hidword:
        print("Correct! The word is:", word, "\nNumber of guesses: ", numguess)


def main():
    ''' implements the functions to create game of spaceman
        params: none
        returns: none
    '''
    numguess = 0
    word = random_word(listwords)
    hidword = hide_word(word)
    print(hidword)
    
    while word != hidword and numguess < 6:
        guess = input("Enter a letter: ")

        prevstate = hidword

        hidword = find_replace(word, hidword, guess)
        print(hidword)

        if prevstate == hidword:
            numguess += 1
            print("Wrong Guess \n Wrong Guesses =", numguess)

        word_check(word, hidword, numguess)
    
    if numguess == 6:
        print("Sorry too many wrong guesses, try again!")


if __name__ == "__main__":
    main()
    