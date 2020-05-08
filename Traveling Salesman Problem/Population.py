#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:03:40 2020

@author: Brahim DEBBAGH
"""
from Circuit import Circuit

class Population:
   def __init__(self, carte, taillePopulation, init):
      self.circuits = []
      for i in range(0, taillePopulation):
         self.circuits.append(None)
      
      if init:
         for i in range(0, taillePopulation):
            nouveauCircuit = Circuit(carte)
            nouveauCircuit.genererIndividu()
            self.sauvegarderCircuit(i, nouveauCircuit)
      
   def __setitem__(self, key, value):
      self.circuits[key] = value
   
   def __getitem__(self, index):
      return self.circuits[index]
   
   def sauvegarderCircuit(self, index, circuit):
      self.circuits[index] = circuit
   
   def getCircuit(self, index):
      return self.circuits[index]
   
   def getFittest(self):
      fittest = self.circuits[0]
      for i in range(0, self.taillePopulation()):
         if fittest.getFitness() <= self.getCircuit(i).getFitness():
            fittest = self.getCircuit(i)
      return fittest
   
   def taillePopulation(self):
      return len(self.circuits)




