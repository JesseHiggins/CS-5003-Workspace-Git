''' Final Project FoodItem Class
    Jesse Higgins
    Professor Jamieson
    CS5001
    4/10/24
    food item class for application that takes a basket of goods and scrapes their pricing information from hannafords website.
'''
import requests
from bs4 import BeautifulSoup

class FoodItem:
    ''' FoodItem class - stores information scraped from website
        Attributes: product id, name, price, quantity
        Methods: scrape_data'''

    def __init__(self, item_url):
        ''' Constructor
            Parameters:
                self
                url - url of item on hannafords website
                item_id - id of product
                item_name - name of product
                item_price - price of product
                item_quantity - quantity or variant of product'''

        self.url = item_url
        self.product_info = []

        URL = self.url
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="quantity_")
        if results:
            self.product_info = {
                "id": results.get("data-id"),
                "name": results.get("data-name"),
                "price": results.get("data-price"),
            }
            self.id = results.get("data-id")
            self.name = results.get("data-name")
            self.price = results.get("data-price")
            
            print(self.product_info)
        else:
            print("Product information not found.")

    def __str__(self):

        print(f"Product Name: {self.name} - Product Price: {self.price} \n")

        

    
