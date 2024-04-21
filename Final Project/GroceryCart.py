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
                product_info_list - list of dictionaries of product information from url scraping
                cart_list - list of fooditem objects intiated with data from the product_info_list
                user_id'''
        
        self.product_info_list = []
        self.cart_list = []
        self.user_id = user_id

    def scrape_data(self, URL_List):
        ''' scrapes data for a list of URLs of food items from the hannafords website
            parameters:
                self
                URL_List - list of urls intiated from user input in the main driver
                '''
        for Item_URL in URL_List:

            URL = Item_URL
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, "html.parser")

            results = soup.find(id="quantity_")
            if results:
                product_info = {
                    "name": results.get("data-name"),
                    "price": results.get("data-price"),
                }
                self.product_info_list.append(product_info)

            else:
                print("Product information not found.")

    def add_items(self):
        ''' Adds items from product_info dictionaries in product_info_list
            Parameters: Self'''
        
        for product_info in self.product_info_list:

            name = product_info['name']
            price = product_info['price']

            food_item = FoodItem(name, price)

            self.cart_list.append(food_item)

            print(f"Item added:\n{food_item}")

            # Resets product_info_list to use again so there are not duplicate items from it
        self.product_info_list.clear()

    def remove_item(self, string_food_name):

        cart_length_intial = len(self.cart_list)

        for food_object in self.cart_list:

            if food_object.name == string_food_name:

                self.cart_list.remove(food_object)
                print(f"{food_object} was removed from the cart.")

        if cart_length_intial == len(self.cart_list):
                
            print("Item not found.")

    def print_cart(self):

        if len(self.cart_list) > 0:

            for item in self.cart_list:

                print(f"Product Name: {item.name}\nProduct Price: {item.price} \n")
        
        else:
            print("The cart is empty.")

    def __str__(self):

        return f"{self.user_id}'s Grocery Cart\nUser Id: {self.user_id}\nNumber of Items: {len(self.cart_list)}"
