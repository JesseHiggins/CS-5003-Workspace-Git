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

    def __init__(self, item_name = '', item_price = 0):
        ''' Constructor
            Attributes:
                self
                url - url of item on hannafords website
                item_id - id of product
                item_name - name of product
                item_price - price of product
                item_quantity - quantity or variant of product
            Methods'''

        self.name = item_name
        self.price = item_price

    def __str__(self):
        ''' Prints info about object name and price'''
        return f"Product Name: {self.name} - Product Price: {self.price} \n"
    
