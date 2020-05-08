#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:03:40 2020

@author: Brahim DEBBAGH
"""
from graph import Chemin

class Population:
   def __init__(self, graph, taillePopulation, init):
      self.chemins = []
      for i in range(0, taillePopulation):
         self.chemins.append(None)
      
      if init:
         for i in range(0, taillePopulation):
            nouveauChemin = Chemin(graph)
            nouveauChemin.genererIndividu()
            self.sauvegarderChemin(i, nouveauChemin)
      
   def __setitem__(self, key, value):
      self.chemins[key] = value
   
   def __getitem__(self, index):
      return self.chemins[index]
  
   def displayPop(self):
       for chemin in self.chemins:
           print(chemin)
   
   def sauvegarderChemin(self, index, chemin):
      self.chemins[index] = chemin
   
   def getChemin(self, index):
      return self.chemins[index]
   
   def getFittest(self):
      fittest = self.chemins[0]
      for i in range(0, self.taillePopulation()):
         if fittest.getFitness() <= self.getChemin(i).getFitness():
            fittest = self.getChemin(i)
      return fittest
   
   def taillePopulation(self):
      return len(self.chemins)




