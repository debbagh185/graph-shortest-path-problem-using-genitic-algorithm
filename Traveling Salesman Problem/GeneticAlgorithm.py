#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:02:20 2020

@author: Brahim DEBBAGH
"""

import random
from Circuit import Circuit
from Population import Population
 

class GA :
   def __init__(self, carte):
      self.carte = carte
      self.tauxMutation = 0.015
      self.tailleTournoi = 5
      self.elitisme = True
   
   def evoluerPopulation(self, pop):
      nouvellePopulation = Population(self.carte, pop.taillePopulation(), False)
      elitismeOffset = 0
      if self.elitisme:
         nouvellePopulation.sauvegarderCircuit(0, pop.getFittest())
         elitismeOffset = 1
      
      for i in range(elitismeOffset, nouvellePopulation.taillePopulation()):
         parent1 = self.selectionTournoi(pop)
         parent2 = self.selectionTournoi(pop)
         enfant = self.crossover(parent1, parent2)
         nouvellePopulation.sauvegarderCircuit(i, enfant)
      
      for i in range(elitismeOffset, nouvellePopulation.taillePopulation()):
         self.muter(nouvellePopulation.getCircuit(i))
      
      return nouvellePopulation


   def crossover(self, parent1, parent2):
      enfant = Circuit(self.carte)
      
      startPos = int(random.random() * parent1.tailleCircuit())
      endPos = int(random.random() * parent1.tailleCircuit())
      
      for i in range(0, enfant.tailleCircuit()):
         if startPos < endPos and i > startPos and i < endPos:
            enfant.setVille(i, parent1.getVille(i))
         elif startPos > endPos:
            if not (i < startPos and i > endPos):
               enfant.setVille(i, parent1.getVille(i))
      
      for i in range(0, parent2.tailleCircuit()):
         if not enfant.contientVille(parent2.getVille(i)):
            for ii in range(0, enfant.tailleCircuit()):
               if enfant.getVille(ii) == None:
                  enfant.setVille(ii, parent2.getVille(i))
                  break
      
      return enfant
   
   def muter(self, circuit):
     for circuitPos1 in range(0, circuit.tailleCircuit()):
        if random.random() < self.tauxMutation:
           circuitPos2 = int(circuit.tailleCircuit() * random.random())
           
           ville1 = circuit.getVille(circuitPos1)
           ville2 = circuit.getVille(circuitPos2)
           
           circuit.setVille(circuitPos2, ville1)
           circuit.setVille(circuitPos1, ville2)

   def selectionTournoi(self, pop):
     tournoi = Population(self.carte, self.tailleTournoi, False)
     for i in range(0, self.tailleTournoi):
        randomId = int(random.random() * pop.taillePopulation())
        tournoi.sauvegarderCircuit(i, pop.getCircuit(randomId))
     fittest = tournoi.getFittest()
     return fittest


