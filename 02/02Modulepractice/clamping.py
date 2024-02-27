# 
# Fall 2020, CS 5001
# 02Practice code file
# Practicing good code style and more complex functions

def main():
    # Input number 1 - 100
    number = int(input("Enter value:"))

    # Clamp numbers

    if number > 100:
        number = 100
        print("Too big, clamping required")
        print("Value is 100")
    elif number < 1:
        number = 1
        print("Too small, clamping required")
        print("Value is 1")
    else:
        print("Value is", number)


if __name__ == "__main__":
    main()
