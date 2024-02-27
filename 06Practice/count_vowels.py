def count_vowels(word):
    num = 0
    word = word.lower()
    for i in range(0, len(word)):
        if word[i] == "a":
            num += 1
        elif word[i] == "e":
            num += 1
        elif word[i] == "i":
            num += 1
        elif word[i] == "o":
            num += 1
        elif word[i] == "u":
            num += 1
    return num

def main():

    print(count_vowels("HELLO"))

if __name__ == "__main__":
    main()