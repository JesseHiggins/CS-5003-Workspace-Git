

def read_values():
    index = 0
    list = []
    integer = int(input("Enter a number: "))
    while integer > 0:
        list += [integer]
        index += 1
        integer = int(input("Enter a number: "))
    print(list)
    return list


def main():

    read_values()


if __name__ == "__main__":
    main()
