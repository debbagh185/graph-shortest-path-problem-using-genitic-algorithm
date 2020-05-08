#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:04:13 2020

@author: Brahim DEBBAGH
"""

import random

class Carte:
   villes = []
   
   def ajouterVille(self, ville):
      self.villes.append(ville)
   
   def getVille(self, index):
      return self.villes[index]
   
   def nombreVilles(self):
      return len(self.villes)

class Circuit:
   def __init__(self, carte, circuit=None):
      self.carte = carte
      self.circuit = []
      self.fitness = 0.0
      self.distance = 0
      if circuit is not None:
         self.circuit = circuit
      else:
         for i in range(0, self.carte.nombreVilles()):
            self.circuit.append(None)

   def __len__(self):
      return len(self.circuit)
   
   def __getitem__(self, index):
     return self.circuit[index]

   def __setitem__(self, key, value):
     self.circuit[key] = value

   def genererIndividu(self):
     for indiceVille in range(0, self.carte.nombreVilles()):
        self.setVille(indiceVille, self.carte.getVille(indiceVille))
     random.shuffle(self.circuit)

   def getVille(self, circuitPosition):
     return self.circuit[circuitPosition]

   def setVille(self, circuitPosition, ville):
     self.circuit[circuitPosition] = ville
     self.fitness = 0.0
     self.distance = 0

   def getFitness(self):
     if self.fitness == 0:
        self.fitness = 1/float(self.getDistance()+1)
     return self.fitness

   def getDistance(self):
     if self.distance == 0:
        circuitDistance = 0
        for indiceVille in range(0, self.tailleCircuit()):
           villeOrigine = self.getVille(indiceVille)
           villeArrivee = None
           if indiceVille+1 < self.tailleCircuit():
              villeArrivee = self.getVille(indiceVille+1)
           else:
              villeArrivee = self.getVille(0)
           circuitDistance += villeOrigine.distance(villeArrivee)
        self.distance = circuitDistance
     return self.distance

   def tailleCircuit(self):
     return len(self.circuit)

   def contientVille(self, ville):
     return ville in self.circuit