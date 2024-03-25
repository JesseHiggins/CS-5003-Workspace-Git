''' Jesse Higgins
    CS5001
    Test case for Scoop.py class
'''
import unittest
from Scoop import Scoop

class testScoop(unittest.TestCase):

    def test_init(self):

        scoop = Scoop(2)
        self.assertEqual(scoop.radius, 2)
    
    def test_get_radius(self):

        scoop = Scoop(2)
        r = scoop.get_radius()
        self.assertAlmostEqual(r, scoop.radius)
        
    def test_volume(self):

        scoop = Scoop(2)
        volume = scoop.volume()
        self.assertAlmostEqual(volume, 33.51032163829)
    
    def test_str(self):
        scoop = Scoop(2)
        self.assertEqual(print(scoop), print("Volume of scoop is 33.51"))

def main():

    scoop = Scoop(2)
    print(scoop)
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()