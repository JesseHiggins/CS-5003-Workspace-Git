# File which will implement the IceCreamShoppe class
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by (your name here)
from Carton import Carton
from Scoop import Scoop

class IceCreamShoppe:
    '''Class IceCreamShoppe
        Attributes: carton_radius, carton_height, cartons_used
        Methods: serve, cartonsUsed'''

    def __init__(self, carton_radius, carton_height):
        ''' Constructor
        Parameters: carton_radius, carton_height - dimensions for a carton
        Return: nothing'''
      # asked permission by raising a type or value error
        if not isinstance(carton_radius, int):
            raise TypeError("radius must be an integer value")
        if carton_radius < 0:
            raise ValueError("radius must be non-negative integer")
        if not isinstance(carton_height, int):
            raise TypeError("height must be an integer value")
        if carton_height < 0:
            raise ValueError("height must be non-negative integer")
        self.carton_radius = carton_radius
        self.carton_height = carton_height
        self.carton = Carton(self.carton_radius, self.carton_height)
        self.number_cartons = 0

    def serve(self, numScoops, scooper):
        ''' serve method
        Parameters: numScoops - number of scoops wanted; 
            scooper - the specific Scoop to use
        Return: nothing'''
        # ask permission with value and type error to validate positive integer input
        if not isinstance(numScoops, int):
            raise TypeError("numScoops must be an integer value")
        if numScoops < 0:
            raise ValueError("height must be non-negative integer")
        while numScoops > 0:
            if self.carton.contains > scooper.volume():
                self.carton.contains -= scooper.volume()
                numScoops -= 1
            elif self.carton.contains <= scooper.volume():
                self.carton = Carton(self.carton_radius, self.carton_height)
                self.number_cartons += 1
        return self.number_cartons
                

    def cartonsUsed(self):
        ''' cartonsUsed method
        Parameters: none
        Return: the number of cartons used so far in the Shoppe'''
        return self.number_cartons