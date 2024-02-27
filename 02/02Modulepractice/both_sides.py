# 
# Fall 2020, CS 5001
# 02Practice code file
# Practicing good code style and more complex functions

def main():
    # Input number 
    number = int(input("Enter value:"))

    # If number is odd/even/positive/negative
    if (number % 2) == 0 and number >= 0:
        print("even positive number")
    elif (number % 2) == 0 and number < 0:
        print("even negative number")
    elif (number % 2) != 0 and number >= 0:
        print("odd positive number")
    else:
        print("odd negative number")


if __name__ == "__main__":
    main()
