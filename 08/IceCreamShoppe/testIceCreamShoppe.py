''' Jesse Higgins
    CS5001
    Test case for IceCreamShoppe.py class
'''

import math
from Carton import Carton
from Scoop import Scoop
from IceCreamShoppe import IceCreamShoppe
import unittest

class testIceCreamShoppe(unittest.TestCase):

    def test_init(self):

        myShop = IceCreamShoppe(2, 2)
        self.assertEqual(myShop.carton_radius, 2)
        self.assertEqual(myShop.carton_height, 2)
        self.assertIsInstance(myShop.carton, Carton)
        self.assertEqual(myShop.number_cartons, 0)


    def test_server(self):

        myShop = IceCreamShoppe(4, 4)
        scoop = Scoop(2)
        expectedNCart = 100
        self.assertEqual(myShop.serve(601, scoop), expectedNCart)
    
    def test_cartons_used(self):

        myShop = IceCreamShoppe(4, 4)
        self.assertEqual(myShop.cartonsUsed(), 0)

def main():
    
    print("hello")
    unittest.main()
if __name__ == "__main__":
    main()