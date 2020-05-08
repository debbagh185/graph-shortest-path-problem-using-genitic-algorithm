#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:02:20 2020

@author: Brahim DEBBAGH
"""

import random
from graph import Chemin
from population import Population
 

class GA :
   def __init__(self, graph):
      self.graph = graph
      self.tauxMutation = 0.015
      self.tailleTournoi = 5
      self.elitisme = True
   
   def evoluerPopulation(self, pop):
      nouvellePopulation = Population(self.graph, pop.taillePopulation(), False)
      elitismeOffset = 0
      if self.elitisme:
         nouvellePopulation.sauvegarderChemin(0, pop.getFittest())
         elitismeOffset = 1
      for i in range(elitismeOffset, nouvellePopulation.taillePopulation()):
         parent1 = self.selectionTournoi(pop)
         parent2 = self.selectionTournoi(pop)
         enfant = self.crossover(parent1, parent2)

         nouvellePopulation.sauvegarderChemin(i, enfant)
      
      for i in range(elitismeOffset, nouvellePopulation.taillePopulation()):
         self.muter(nouvellePopulation.getChemin(i))
      
      return nouvellePopulation


   def crossover(self, parent1, parent2):
      nombre = parent1.tailleChemin() if parent1.tailleChemin() > parent2.tailleChemin() else parent2.tailleChemin()
      self.graph.setNombreNoeuds(nombre)
      enfant = Chemin(self.graph)
      enfant.setNoeud(0, parent1.getNoeud(0))
      enfant.setNoeud(enfant.tailleChemin()-1, parent1.getNoeud(enfant.tailleChemin()-1))
      
      startPos = random.choice(range(0,parent1.tailleChemin()))
      endPos = random.choice(range(0,parent1.tailleChemin()))
      
      for i in range(1, enfant.tailleChemin()-1):
         if startPos < endPos and i > startPos and i < endPos:
            enfant.setNoeud(i, parent1.getNoeud(i))
         elif startPos > endPos:
            if not (i < startPos and i > endPos):
               enfant.setNoeud(i, parent1.getNoeud(i))
      
      for i in range(0, parent2.tailleChemin()):
         if not enfant.contientNoeud(parent2.getNoeud(i)):
            for ii in range(0, enfant.tailleChemin()):
               if enfant.getNoeud(ii) == None:
                  enfant.setNoeud(ii, parent2.getNoeud(i))
                  break
              
      return enfant
   
   def muter(self, chemin):
     for cheminPos1 in range(1, chemin.tailleChemin()-1):
        cheminPos2 = random.choice(range(1,chemin.tailleChemin()-1))
        if random.random() < self.tauxMutation:
           chemin.swap(cheminPos1, cheminPos2)           
        elif random.random() >= self.tauxMutation and random.random() < self.tauxMutation*2:
           chemin.removeNoeud(cheminPos2)

   def selectionTournoi(self, pop):
     tournoi = Population(self.graph, self.tailleTournoi, False)
     for i in range(0, self.tailleTournoi):
        randomId = random.choice(range(0,pop.taillePopulation()))
        tournoi.sauvegarderChemin(i, pop.getChemin(randomId))
     fittest = tournoi.getFittest()
     return fittest


