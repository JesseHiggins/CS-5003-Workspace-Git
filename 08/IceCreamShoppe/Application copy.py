# File which will hold the main function for the IceCreamShoppe project
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by (Jesse Higgins)
from IceCreamShoppe import IceCreamShoppe
from Scoop import Scoop

def main():
    

    scoop1 = Scoop(2)

    radiuscarton_text = -1
    while radiuscarton_text < 0:
        radiuscarton_text = int(input("What is the radius of your carton? "))


    heightcarton_text = -1
    while heightcarton_text < 0:
        heightcarton_text = int(input("What is the height of your carton? "))

    myShop = IceCreamShoppe(radiuscarton_text, heightcarton_text)

        numscoops1 = int(input(f"How many {scoop1.radius} scoops would you like? "))
        myShop.serve(numscoops1, scoop1)
        myShop.serve(numscoops2, scoop2)



if __name__ == "__main__":
    main()