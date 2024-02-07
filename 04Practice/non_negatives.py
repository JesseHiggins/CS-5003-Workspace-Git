

def non_negatives():

    integer = int(input("Enter an integer:"))

    while integer >= 0:

        print(integer)
        integer = int(input("Enter an integer:"))


def main():

    non_negatives()


if __name__ == "__main__":
    main()
