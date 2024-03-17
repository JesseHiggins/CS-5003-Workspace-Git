''' Align Online
    CS5001
    Sample code -- defining a class, in this case, Coffee
'''
import math

class Point:


    def __init__(self, x, y, z):
        
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, origin = None):
        if origin is None:
            origin = Point(0, 0, 0)
        
        distance = math.dist(self, origin)

        return distance

def main():

    point = Point(1, 2, 3)

    print(point.get_distance())

if __name__ == "__main__":
    main()