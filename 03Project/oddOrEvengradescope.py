''' This file will be used in Project 3.
    NAME: Jesse Higgins
    DATE: January 24, 2024
    Description of Project 3: Project three introduces command line arguments and then builds functions
'''

#Import libraries
import sys

#determine if a number is odd or even with command line arguments
def main():

    # calculate whether a number is odd or even
    def oddOrEven( number ):
        print('determining if ' + str(number) + ' is odd or even:')

        # if statement
        if number%2==0:
            print(str(number) + " is even.") 
        else:
            print(str(number) + " is odd.")



    # assign a default value
    my_number = 10

    # check for user input
    if len( sys.argv ) > 1:
        # re-assign the value if the user provided one
        my_number = int( sys.argv[1] )

    # call the function
    oddOrEven(my_number)


if __name__ == "__main__":
    main()
