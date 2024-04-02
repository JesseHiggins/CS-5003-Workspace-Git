
''' Jesse Higgins
    CS5001
    Test case for Stack Bracket Application
'''
import math
from StackProject import StackProject
import unittest

class testCarton(unittest.TestCase):

    def test_init(self):
        ''' Test Constructor
            Parameters:
                self'''
        Bracket = 
        self.assertAlmostEqual(carton.contains, 25.132741228718)

    def test_hasEnoughFor(self):
    
        carton = Carton(1,1)
        scoop = Scoop.Scoop(2)
        hasenough = carton.hasEnoughFor(scoop)

        self.assertEqual(carton.hasEnoughFor(scoop), False)

    def test_remove(self):

        carton = Carton(4,4)
        scoop = Scoop.Scoop(1)

        self.assertAlmostEqual(int(carton.remove(scoop)), 196)

    def test_str(self):
        
        carton = Carton(4, 4)
        expected_str = "Carton contains: 201"
        self.assertEqual(str(carton), expected_str)


def main():

    unittest.main()
if __name__ == "__main__":
    main()