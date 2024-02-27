# 
# Fall 2020, CS 5001
# 02Practice code file
# Practicing good code style and more complex functions

def main():

    # Input 4 integers
    a = int(input("Enter integer:"))
    b = int(input("Enter integer:"))
    c = int(input("Enter integer:"))
    d = int(input("Enter integer:"))

    # Find matching pair and print two pairs or not two pairs
    if a == b and c == d:
        print("two pairs")
    elif a == c and b == d:
        print("two pairs")
    elif a == d and b == c:
        print("two pairs")
    else:
        print("not two pairs")


if __name__ == "__main__":
    main()
