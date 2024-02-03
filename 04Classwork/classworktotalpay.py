''' In class exercises
    Jesse Higgins
    1/29/2024
'''

def totalPay(base_pay, percent = .2):
    ''' computes the averages of the grades read in
        params: none
        return: none
    '''
    # debug put breakpoint on first line inside function
    total_pay = base_pay
    sale = int(input("Enter a sale or -1 to quit: "))
    while(sale != -1):
        total_pay += sale * percent
        sale = int(input("Enter a sale or -1 to quit: "))
    return total_pay


def printBig():
    '''Computes biggest number from entered numbers
        params: none
        returns: none'''
    big = 0
    number = int(input("Enter a number: "))

    while(number >= 0):
        if number > big:
            big = number
            print("Biggest number: ", big)
        number = int(input("Enter a number: "))

def lindsayBigSmall():
    '''Computes biggest and smallest number from entered numbers
        params: none
        returns: big, small
    '''
    big = small = num = int(input("Enter a number: "))
    while(num >= 0):
        if num < small:
            small = num
        if big < num:
            big = num
        num = int(input("Enter a number: "))
    return big, small

def example1():
    '''example1: Function that will print the numbers from 10 down to 5
    parameters: none
    return: none'''
    var = 10
    while(var >= 5):
        print("current variable value: ", var)
        var = var -1
    print("Good bye!")

def example2():
    var = 10
    while (var >= 0):
        print(var)
        var = var - 1
    print("-1 my number is negative")

def example3():
    num_inputs = 0
    total = 0
    grade = int(input("Enter your grade or -1 to quit"))
    while(grade >= 0):
        total += grade
        num_inputs += 1
        grade = int(input("Enter your grade or -1 to quit"))
    average = total/num_inputs
    print("There were " + str(num_inputs) + " grades with an average of " + str(average))

def main():

    example3()
    #example2()
    #example1()
    #print(lindsayBigSmall())
    #printBig()
    #total_pay = totalPay(200)
    #print("The total pay was: " + str(total_pay))

if __name__ == "__main__":
      main()