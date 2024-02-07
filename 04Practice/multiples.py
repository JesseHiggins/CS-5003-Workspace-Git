

def multiples():

    integer = int(input("Enter a non-zero integer: "))
    multiple = int(input("Enter multiple: "))

    while multiple % integer != 0:

        multiple = int(input("Try again: "))


def main():

    multiples()


if __name__ == "__main__":
    main()
