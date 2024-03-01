def count_words():
    word = input("Enter a sentence: ")
    list1 = word.split()
    for i in range(len(list1)):
        print(i,". ",list1[i], sep='')

def main():

    count_words()

if __name__ == "__main__":
    main()