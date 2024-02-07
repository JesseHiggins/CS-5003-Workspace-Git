

def multiples():

    integer = int(input("Enter the number of values to read: "))
    value = int(input("Enter an integer:"))
    total = value
    count = 1

    while count < integer:
        if integer < 0:
            print("The sum is 0")
        value = int(input("Enter an integer:"))
        total = total + value
        count += 1

    average = total / integer
    print("The sum is", total)
    print("The average is", average)


def main():

    multiples()


if __name__ == "__main__":
    main()
