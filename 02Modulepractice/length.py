# 
# Fall 2020, CS 5001
# 02Practice code file
# Practicing good code style and more complex functions

def main():

    # Input length
    length = float(input("Enter length:"))

    # Calculate length in inches, feet, miles
    inches = length * 39.3701
    feet = inches / 12
    miles = length / 1609.34

    # Print
    print("The length in inches is ", inches)
    print("The length in feet is ", feet)
    print("The length in miles is", miles)


if __name__ == "__main__":
    main()
