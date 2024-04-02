
def validating_input():

    firstint = int(input("Enter value: "))

    if firstint == 0:
        print("Value should be either negative or positive")
        firstint = int(input("Enter value: "))
        
    secondint = int(input("Enter value: "))
        
    if firstint > 0:
        if secondint >= 0:
            print("Value should be negative")
            secondint = int(input("Enter value: "))

    if firstint < 0 and secondint <= 0:
        print("Value should be positive")
        secondint = int(input("Enter value: "))

    if firstint < secondint:
        print(f"Pair: ({firstint}, {secondint})")

    if secondint < firstint:
        print(f"Pair: ({secondint}, {firstint})")


def main():

    validating_input()

if __name__ == "__main__":
    main()

    
        

    