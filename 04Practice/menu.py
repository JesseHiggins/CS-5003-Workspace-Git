

def menu():

    print("0 -- Quit")
    print('1 -- Add "O"')
    print('2 -- Add "oo"')
    print('3 -- Add "xXx"')
    option = int(input("Option: "))

    result = ""

    while option != 0:
        if option == 1:
            result += "O"
            print("0 -- Quit")
            print('1 -- Add "O"')
            print('2 -- Add "oo"')
            print('3 -- Add "xXx"')
        elif option == 2:
            result += "oo"
            print("0 -- Quit")
            print('1 -- Add "O"')
            print('2 -- Add "oo"')
            print('3 -- Add "xXx"')
        elif option == 3:
            result += "xXx"
            print("0 -- Quit")
            print('1 -- Add "O"')
            print('2 -- Add "oo"')
            print('3 -- Add "xXx"')
        else: 
            print("Invalid option")
            print("0 -- Quit")
            print('1 -- Add "O"')
            print('2 -- Add "oo"')
            print('3 -- Add "xXx"')
        option = int(input("Option: "))

    print("Result:", result)


def main():

    menu()


if __name__ == "__main__":
    main()
