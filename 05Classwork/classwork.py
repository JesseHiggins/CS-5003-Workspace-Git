''' Strings and Lists
    February 5, 2024
    Lindsay Jamieson
'''

def printString(my_str):
    ''' printString - prints the string vertically
        param: the string
        returns: None'''
        # Python literally returns a string None
    location = 0
    while location < len(my_str):
        print(my_str[location])
        location += 1

def main():
    hello = "Hello World"
    hello = "Welcome!"
    printString(hello)
    printString(hello)

if __name__ == "__main__":
    main()