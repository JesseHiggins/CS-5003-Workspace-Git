import math

class Circle:

    def __init__(self, x ,y, r):

        self.x = x
        self.y = y
        self.r = r

    def get_area(self):

        area = 3.14 * (self.r ** 2)

        return area
    
    def get_distance(self, x, y):

        p = (self.x, self.y)
        q = (x, y)

        distance = math.dist(p, q)

        return distance
    
    def __str__(self):
        
        output = f"Circle: center at ({self.x}, {self.y}) with radius {self.r}"

        return output
    
def main():

    p = Circle(0, 0, 2)
    print(p.get_area())

main()
