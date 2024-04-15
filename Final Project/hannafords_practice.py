from FoodItem import FoodItem
from GroceryCart import GroceryCart
import requests
from bs4 import BeautifulSoup


# URL = "https://www.hannaford.com/product/hass-avocados/884468?hdrKeyword=AVACADO"
# page = requests.get(URL)


# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="quantity_")

# print(results.prettify())

# data_name = results.get("data-name")

# print(data_name)

########        
# URL = "https://www.hannaford.com/product/hass-avocados/884468?hdrKeyword=AVACADO"
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="quantity_")
# if results:
#     product_info = {
#         "id": results.get("data-id"),
#         "name": results.get("data-name"),
#         "price": results.get("data-price"),
#     }

# print(product_info)
#######

def main():

    cart = GroceryCart("Jesse")

    cart.add_item("avocado", "https://www.hannaford.com/product/hass-avocados/884468?hdrKeyword=AVACADO")

if __name__ == "__main__":
    main()