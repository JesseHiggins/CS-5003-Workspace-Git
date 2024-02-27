#
# Fall 2024, CS 5001
# Lab 2 code file
# Practicing good code style and more complex functions

def main():

    # User input three numbers x,y,z any type conversion to int
    x = int(input("Input a whole number"))
    y = int(input("Input another whole number"))
    z = int(input("Input another whole number")) 

    # Average 3 numbers
    average = (x + y + z) / 3

    # Are x,y,z the same? Print all the same
    if x == y == z:
        print ("All numbers same")

    # Boolean expressions to find biggest smallest and print 
    if x > y and y > z:
        print("biggest = " + str(x) + ", smallest = " + str(z) + ", average = " + str(average))
    if x > z and z > y:
        print("biggest = " + str(x) + ", smallest = " + str(y) + ", average = " + str(average))
    if y > x and x > z:
        print("biggest = " + str(y) + ", smallest = " + str(z) + ", average = " + str(average))
    if y > z and z > x:
        print("biggest = " + str(y) + ", smallest = " + str(x) + ", average = " + str(average))
    if z > x and x > y:
        print("biggest = " + str(z) + ", smallest = " + str(y) + ", average = " + str(average))
    if z > y and y > x:
        print("biggest = " + str(z) + ", smallest = " + str(x) + ", average = " + str(average))

if __name__=="__main__":
    main()