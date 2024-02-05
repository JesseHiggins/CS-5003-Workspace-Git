

def non_negatives():

    word = input("Enter a word:")
    words = word

    while word != "stop":

        word = input("Enter a word:")
        words = words + " " + word
        
    print(words)

def main():

    non_negatives()


if __name__ == "__main__":
    main()
