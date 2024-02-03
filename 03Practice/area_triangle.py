
import math


def area_triangle(side1, side2, side3):

    s = (side1 + side2 + side3) / 2

    area = math.sqrt(s * ((s - side1) * (s - side2) * (s - side3)))

    return area


def main():

    result = area_triangle(10, 10, 10)

    print(result)


if __name__ == "__main__":
    main()
