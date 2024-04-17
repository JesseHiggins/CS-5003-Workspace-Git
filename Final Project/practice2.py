from GroceryCart import GroceryCart

def main():

    cart = GroceryCart("Jesse")

    cart.add_item("https://www.hannaford.com/product/hass-avocados/884468?hdrKeyword=AVACADO")

    # cart.add_item("avocado2", "https://www.hannaford.com/product/hass-avocados/884468?hdrKeyword=AVACADO")

    cart.print_cart()

    cart.remove_item("Hass Avocados")

    cart.print_cart()

if __name__ == "__main__":
    main()