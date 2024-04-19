''' Final Project Grocery Cart Class
    Jesse Higgins
    Professor Jamieson
    CS5001
    4/10/24
    driver application for Cart'''

from GroceryCart import GroceryCart
from FoodItem import FoodItem

def main():

    UserId = input("Enter a name for the user ID of this cart: ")
    Cart = GroceryCart(UserId)

    URL_List = []
    URL = input("Enter a URL for a food item from the Hannafords website or press 0 to end: ")

    while URL != "0":

        URL_List += URL
        URL = input("Enter a URL for a food item from the Hannafords website or press 0 to end: ")

    Cart.scrape_data(URL_List)
    Cart.add_items()

    print(Cart)

if __name__ == "__main__":
    main()

        
        