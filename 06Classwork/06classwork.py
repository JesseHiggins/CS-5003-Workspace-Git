""" classwork for 06module
    Jesse Higgins
    February 12, 2024
"""
def countUp(min, max, jump = 1):
    ''' counts from 0 to max by jump
        params:
            min - the number to count from
            max - largest number to count to,
            jump - how many to skip
        returns: none'''
    for count in range(min, max, jump):
        print(count)

def sumNum():
    ''' takes a number and sums from 1 to that number
        params: number
        return: none
    '''
    num = int(input("Enter a number: "))
    sum = 0

    for i in range(1, (num + 1)):
        sum += i

    print(sum)

# takes a number and factorials that number
def factorial():
    
    num = int(input("Enter a number: "))
    fac = 1

    for i in range(1, num+1):
        fac *= i

    print(fac)

#creates a square list from a list
def squareList(mylist):

    for num in mylist:
        num *= num
        print

# iteratres through a list to determine if a character should be swapped to leetspeak and swaps
def leetSpeak(string):

    swap = ["a", "e", "h", "i", "l", "o", "p", "t"]
    swapped = ["4", "3", "#", "!", "1", "0", "9", "7"]
    lst = list(string)

    for char in lst:
        for i in range(0,len(swap)):
            if char == swap[i]:
                lst[lst.index(char)] = swapped[i]
    lst = str().join(lst)
    print(lst)

# different leetspeak using ifs
def lindsayleet():
    result = ""
    mystring = mystring.lower()
    for char in mystring:
        if char == "a":
            result += "4"
        elif char == "e":
            result += "3"
        elif char == "e":
            result += "3"
        elif char == "h":
            result += "#"
        elif char == "i":
            result += "!"
        elif char == "l":
            result += "1"
        elif char == "o":
            result += "0"
        elif char == "e":
            result += "3"

#psiuedo code from lyndsay for leetspeak
# def leetspeak(mystring):
#     normal = ["a", "e"]
#     leet = ["4", "4"]

#     for char in mystring:
#         if char in normal:
#             location = 
#             result += leet[location]

def rangOverList(list):
    for i in range(len(list)):
        if (list[i] % 2) == 0:
            print(list[i], " is even")
        else:
            print(list[i], "is not even")

def triangle():
    for i in range(1, 11):
        print("*" * i)

def lindsaytriangle2():
    for i in range(10, 0, -1):
        for j in range (i):
            print("*", end='')
            print()

def triangleUpside():
    for i in range(11, 1, -1):
        print("*" * i)

def triangleRight():
    for i in range(1, 11):
        for j in range():
            print("_" * i, end="")
            print("*" * j, end="")

def triangle3():
    for i in range(10, 0, -1):
        for j in range(i-1):
            print("_")
            10-i+1


def main():

    triangleRight()
    # leetSpeak("dont come at me bro")

    # mylist = [1, 2, 3, 4, 5]
    # print(mylist)
    # squareList(mylist)
    # print(mylist)

    #countUp(1, 11)
    #print()
    #countUp(1, 20, 2)

    #for i in range(0, 201, 2):
    #    print(i)

    #sumNum()

    # factorial()

if __name__ == "__main__":
    main()