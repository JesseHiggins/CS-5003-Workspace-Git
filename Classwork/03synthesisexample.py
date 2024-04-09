
from Car import Car

def factorial(n):

    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")
    fac = 1

    for i in range(1, num+1):
        fac *= i
    
    return fac

def main():

    try:
        number = int(input("Enter number to be factorialized: "))
        factorialized_number = factorial(number)
        print(number, "factorialized is: ", factorialized_number)

    except TypeError as ex:
        print("Invalid type:", type(ex), ex)
    except ValueError as ex:
        print("Invalid value:", type(ex), ex)

def main():

    filename = input("enter filename:")
    file = open(filename, "w")

    first_line = file.readline()

    print("First line:", first_line)

    file.close()
             
if __name__ == "__main__":
    main()
