#
# Fall 2024, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions

def main():
    
    #input four words
    a = input("Enter the first word")
    b = input("Enter the second word")
    c = input("Enter the third another word")
    d = input("Enter the fourth another word")
        
    #alphabetize words with boolean expressions and print in alphabetical order
    if a > b:
        a, b = b, a
    elif b > c:
        b, c = c, b
    elif c > d:
        c, d = d, c
    elif a > b:
        a, b = b, a
    elif b > c:
        b, c = c, b
    elif a > b:
        a, b = b, a

    #words are sorted in alphabetical order and print to user
    sorted_words = [a, b, c, d]
    print("Sorted Words:", sorted_words)
    
if __name__=="__main__":
    main()