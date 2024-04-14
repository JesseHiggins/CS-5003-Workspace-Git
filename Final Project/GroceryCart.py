''' Final Project Grocery Cart Class
    Jesse Higgins
    Professor Jamieson
    CS5001
    4/10/24
    GroceryCart class that contains list of item ids for FoodItems'''

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

    def add_item(self, name, item_url):

        