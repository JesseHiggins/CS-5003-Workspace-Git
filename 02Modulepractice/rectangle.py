# 
# Fall 2020, CS 5001
# 02Practice code file
# Practicing good code style and more complex functions

# input rectangle sides and convert

def main():

    width = float(input("Enter width:"))
    height = float(input("Enter height:"))

    # compute area, perimeter, diagonal
    import math
    area = height * width
    diagonal = math.sqrt(height ** 2 + width ** 2)
    perimeter = (height + width) * 2

    # print
    print("The area of the rectangle is " + str(area))
    print("The perimeter of the rectangle is " + str(perimeter))
    print("The diagonal of the rectangle is " + str(diagonal))


if __name__ == "__main__":
    main()
