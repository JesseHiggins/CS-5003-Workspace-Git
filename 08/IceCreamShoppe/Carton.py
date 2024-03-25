# File which will hold the implementation of Carton
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by (your name here)
import math #this gives you pi
from Scoop import Scoop

class Carton:
    ''' Class: Carton
        Attributes: contains
        Methods: hasEnoughFor, remove'''
    
    def __init__(self, radius, height):
        ''' Constructor
            Parameters:
                self
                radius - radius of a carton
                height - height of a carton'''
        if not isinstance(radius, int):
            raise TypeError("radius must be an integer value")
        if radius < 0:
            raise ValueError("radius must be non-negative integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer value")
        if height < 0:
            raise ValueError("height must be non-negative integer")
        self.contains = math.pi * height * (radius ** 2)

    def hasEnoughFor(self, scoop):
        ''' hasEnoughFor
            Parameters:
                scoop - the Scoop to be used on the Carton
            Return:
                whether or not the Carton contains enough to make a Scoop'''
        scoop_volume = scoop.volume()
        # validate that scoop is smaller than carton to avoid infinite loop on main application
        if scoop_volume > self.contains:
            raise ValueError("scoop must be smaller than carton")
        if self.contains >= scoop_volume:
            return True
        else:
            return False

    def remove(self, scoop):
        ''' remove
            Parameters:
                scoop - the Scoop to be used on the Carton
        '''
        scoop_volume = scoop.volume()
        # validate that scoop is smaller than carton to avoid infinite loop on main application
        if scoop_volume > self.contains:
            raise ValueError("scoop must be smaller than carton")
        self.contains -= scoop_volume


        return self.contains
    
    def __str__(self):
        output = f"Carton contains: {int(self.contains)}"
        return output