# File which will hold the main function for the IceCreamShoppe project
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by (Jesse Higgins)
from IceCreamShoppe import IceCreamShoppe
from Scoop import Scoop

def main():
    
    radius1_text = -1
    while radius1_text < 0:
        radius1_text = int(input("What is the radius of your first scooper? "))
    scoop1 = Scoop(radius1_text)
    
    radius2_text = -1
    while radius2_text < 0:
        radius2_text = int(input("What is the radius of your second scooper? "))
    scoop2 = Scoop(radius2_text)

    radiuscarton_text = -1
    while radiuscarton_text < 0:
        radiuscarton_text = int(input("What is the radius of your carton? "))


    heightcarton_text = -1
    while heightcarton_text < 0:
        heightcarton_text = int(input("What is the height of your carton? "))

    myShop = IceCreamShoppe(radiuscarton_text, heightcarton_text)

    # defensive programming by asking for permission with repititon
    answer = int(input("Would you like more ice cream? (Enter 1 for yes and 0 for no) "))
    while answer < 0 or answer > 1:   
        answer = int(input("Please enter 1 or 0. Would you like more ice cream? (Enter 1 for yes and 0 for no) "))
    while answer > 0:
        numscoops1 = int(input(f"How many {scoop1.radius} scoops would you like? "))
        numscoops2 = int(input(f"How many {scoop2.radius} scoops would you like? "))
        myShop.serve(numscoops1, scoop1)
        myShop.serve(numscoops2, scoop2)

        answer = int(input("Would you like more ice cream? (Enter 1 for yes and 0 for no) "))
        print(f"You used {myShop.cartonsUsed()} cartons of ice cream.")


if __name__ == "__main__":
    main()