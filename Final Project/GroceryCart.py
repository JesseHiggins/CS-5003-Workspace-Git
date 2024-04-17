''' Final Project Grocery Cart Class
    Jesse Higgins
    Professor Jamieson
    CS5001
    4/10/24
    GroceryCart class that contains list of item ids for FoodItems'''

from FoodItem import FoodItem
from bs4 import BeautifulSoup
import requests

class GroceryCart:
    ''' GroceryCart - holds FoodItem ids and user id
        Attributes: 
            cart_list - FoodItem ids from hannafords data
            user_id - UserId for specific grocerycart
        Methods:
            add_item - add item from url to cart_list
            remove_item - removes item from cart
            print_cart - prints the cart with price '''
    
    def __init__(self, user_id):
        ''' Constructor
            Parameters:
                cart_list
                user_id'''
        
        self.cart_list = []
        self.user_id = user_id

    def scrape_data(self, URL_List):
        
        URL = self.url
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="quantity_")
        if results:
            product_info = {
                "id": results.get("data-id"),
                "name": results.get("data-name"),
                "price": results.get("data-price"),
            }

        else:
            print("Product information not found.")

    def add_item(self, item_url):

        name = FoodItem(item_url)

        name.scrape_data()

        self.cart_list.append(name)

    def remove_item(self, string_food_name):

        for food in self.cart_list:

            if food.name == string_food_name:

                self.cart_list.remove(food)


    def print_cart(self):

        if len(self.cart_list) > 0:

            for item in self.cart_list:

                print(f"Product Name: {item.name}\nProduct Price: {item.price} \n")
        
        else:
            print("The cart is empty.")
