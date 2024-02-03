''' guess my number game
    Jesse Higgins
    1/29/2024
'''
guess = int(input("Guess a number: "))
def guessHighLow(number = 100):
    ''' compares guess to number and prints if it is high or low and returns difference
        params: none
        return: previousdifference
    '''
    while guess != number:
        if guess < number:
            print("Too low")
        if guess > number:
            print("Too high")
        previousdifference = number - guess
    return previousdifference

def guessHotCold(previousdifference):
    ''' compares difference in guess to previous difference and prints hot or cold
        params: previousdifference
        return: none
    '''
    difference = number - guess

def main():

    guessHighLow()

if __name__ == "__main__":
    main()