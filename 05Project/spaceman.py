listwords = ["actor", "adult", "anger", "beach", "birth", "cross", "crowd", "dance", "chair", "bread", "brown", "guide", "happy", "heart", "drill", "metal", "judge", "rival", "paper", "sense", "texas"]
import random

def random_word(list):

    word = list[random.randint(1, 20)]

    return word

def hide_word(word):
    
    hidword = "*" * len(word)

    return hidword

def find_replace(word, hidword, guess):
    
    hidword = list(hidword)

    count = 0

    while count < len(word):
        if guess == word[count]:
            hidword[count] = guess
        count += 1

    return "".join(hidword)

def word_check(word, hidword, numguess):

    if word == hidword:
        print("Correct! The word is:", word, "\nNumber of guesses: ", numguess)

def main():
    
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
    