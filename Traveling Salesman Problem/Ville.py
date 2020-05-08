#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:11:03 2020

@author: Brahim DEBBAGH
"""

import math

class Ville:
   def __init__(self, lon, lat, nom):
      self.lon = lon
      self.lat = lat
      self.nom = nom
   

   def distance(self, ville):
      disX = (ville.lon-self.lon)*40000*math.cos((self.lat+ville.lat)*math.pi/360)/360
      disY = (self.lat-ville.lat)*40000/360
      distance = math.sqrt( (disX*disX) + (disY*disY) )
      return distance
  
    