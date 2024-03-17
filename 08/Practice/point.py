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
        
        p = (self.x, self.y, self.z)
        q = (origin.x, origin.y, origin. z)

        distance = math.dist(p, q)

        return distance

    def __str__(self):
        
        output = f"Point: ({self.x}, {self.y}, {self.z})"

        return output

def main():

    point = Point(1, 2, 3)

    print(point.get_distance())
    print(point)

if __name__ == "__main__":
    main()