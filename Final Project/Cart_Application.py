''' Final Project Grocery Cart Class
    Jesse Higgins
    Professor Jamieson
    CS5001
    4/10/24
    driver application for Cart'''

from GroceryCart import GroceryCart
from FoodItem import FoodItem
import requests

def main():

    UserId = input("Enter a name for the user ID of this cart: ")
    Cart = GroceryCart(UserId)

    URL_List = []
    URL = input("Enter a URL for a food item from the Hannafords website or press 0 to end: ")

    while URL != "0":

        URL_List.append(URL)
        URL = input("Enter a URL for a food item from the Hannafords website or press 0 to end: ")

    Cart.scrape_data(URL_List)
    Cart.add_items()

    print(Cart)

    while True:
        option = input("Do you want to:\n1. Add an item to the cart\n2. Remove an item from the cart\n3. Print the cart\n4. Exit\n")
        if option == "1":
            URL = input("Enter a URL for a food item from the Hannafords website: ")
            URL_List.append(URL)
            Cart.scrape_data(URL_List)
            Cart.add_items()
            print(Cart)
        elif option == "2":
            string_name = input("Enter the name of the item you want to remove: ")
            Cart.remove_item(string_name)
            print(Cart)
        elif option == "3":
            Cart.print_cart()
            print(Cart)
        elif option == "4":
            break

if __name__ == "__main__":
    main()

        
        