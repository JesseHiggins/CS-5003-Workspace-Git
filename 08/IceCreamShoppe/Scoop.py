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
      