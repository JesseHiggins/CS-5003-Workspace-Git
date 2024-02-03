'''Right triangle with functions
    Jesse Higgins
    1/22/2024
'''

def isRightTriangle(side1, side2, side3):
    '''isRightTriangle - finds out if the three sides are a right triangle
        params: 3 three sides
        returns: true/false is it a right triangle
    '''
    square_side1 = side1*side1
    square_side2 = side2*side2
    square_side3 = side3*side3
    if(square_side1+square_side2) == square_side3:
        return True
    else:
        return False

def isRightTriangle(side1, side2, side3):
    '''isRightTriangle - finds out if the three sides are a right triangle
        params: 3 three sides
        returns: true/false is it a right triangle
    '''
    return (side1**2 + side2**2) == side3**2

