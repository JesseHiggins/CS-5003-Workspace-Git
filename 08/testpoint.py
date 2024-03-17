from point import Point
import unittest

class PointTest(unittest.TestCase):
    def test_init(self):
        point = Point(1, 2, 3)
        self.assertEqual(point.x, 1)
        self.assertEqual(point.y, 2)
        self.assertEqual(point.z, 3)

    def test_get_distance(self):
        point = Point(1, 2, 3)

def main():
    unittest.main()

main()