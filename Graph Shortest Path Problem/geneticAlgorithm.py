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
         meilleurChemin = pop.getFittest()
         nouvellePopulation.sauvegarderChemin(0, meilleurChemin)
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
      randomIndex = random.choice(range(1,parent1.tailleChemin()))
      if parent1.chemin[randomIndex] in parent2.chemin :
          firstChild = parent1.chemin[:randomIndex]+parent2.chemin[randomIndex:]
          secondChild = parent2.chemin[:randomIndex]+parent1.chemin[randomIndex:]
          randomChild = random.choice([firstChild,secondChild])
          self.graph.setNombreNoeuds(len(randomChild))
          enfant = Chemin(self.graph)
          for i in range(0,len(randomChild)) :
              enfant.setNoeud(i,randomChild[i])
          return enfant
      else :
          return parent1

              
   def muter(self, chemin) :
     for cheminPos1 in range(1, chemin.tailleChemin()-1):
        cheminPos2 = random.choice(range(1,chemin.tailleChemin()-1))
        if random.random() < self.tauxMutation:
           if(random.choice([True,False])) : chemin.swap(cheminPos1, cheminPos2)    
           else : chemin.removeNoeud(cheminPos2)

   def selectionTournoi(self, pop):
     tournoi = Population(self.graph, self.tailleTournoi, False)
     for i in range(0, self.tailleTournoi):
        randomId = random.choice(range(0,pop.taillePopulation()))
        tournoi.sauvegarderChemin(i, pop.getChemin(randomId))
     fittest = tournoi.getFittest()
     return fittest


