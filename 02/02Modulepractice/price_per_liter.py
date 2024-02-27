# 
# Fall 2020, CS 5001
# 02Practice code file
# Practicing good code style and more complex functions

def main():

    # Input price per liter
    sixpack = float(input("Price per six-pack:"))
    twoliter = float(input("Price per two-liter:"))

    # Calculate price per liter
    pricesixpack = sixpack / 2.13
    pricetwoliter = twoliter / 2

    # Print
    print("Six-pack price per liter:", pricesixpack)
    print("Two-liter price per liter:", pricetwoliter)


if __name__ == "__main__":
    main()
