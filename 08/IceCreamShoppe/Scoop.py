# File which will hold the implementation of Scoop
# Created by Lindsay Jamieson
# 3/29/2022
# Implemented by (Jesse Higgins)
import math

class Scoop:
   '''Class Scoop
      Attributes: radius
      Methods: volume'''
    
   def __init__(self, radius):
      '''
      Constructor - creates a new instance of Scoop
      Parameters -
         self - the current object
         radius - the radius of the scoop'''
      # asked permission by raising a type or value error
      if not isinstance(radius, int):
        raise TypeError("radius must be an integer value")
      if radius < 0:
        raise ValueError("radius must be non-negative integer")
      self.radius = radius

   def get_radius(self):
      '''method - return attribute radius
      params: none
      returns: radius'''
      radius = self.radius

      return radius

   def volume(self):
      ''' Method - calculate the volume of the scoop
      Parameters:
      self - the current object'''
         
      volume = (4/3) * math.pi * (self.radius ** 3)

      return volume
   
   def __str__(self):
      output = f"Volume of scoop is {self.volume()}"
      return output
      