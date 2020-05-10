#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 21:03:40 2020

@author: Brahim DEBBAGH
"""
from graph import Chemin

class Population:
   def __init__(self, graph,init,taillePopulation=0):
      self.chemins = []
      self.graph = graph
      
      if init:
         visited = dict.fromkeys(graph.vert_dict.keys(),False)
         path = []  
         self.saveAllPathsUtil(graph.sourceId, graph.destId, visited, path) 
      else:          
          for i in range(0, taillePopulation):
             self.chemins.append(None)
         
       
   def saveAllPathsUtil(self,u, d, visited, path): 
  
        visited[u]= True
        path.append(u) 
  
        if u == d: 
            self.graph.setNombreNoeuds(len(path))
            chemin = Chemin(self.graph)
            for i in range(0,chemin.tailleChemin()) :
                chemin.setNoeud(i, self.graph.get_vertex(path[i]))
            self.chemins.append(chemin) 
        elif self.taillePopulation() <= 30: 
            
            for i in self.graph.get_vertex(u).get_connections(): 
                if visited[i.get_id()]==False: 
                    self.saveAllPathsUtil(i.get_id(), d, visited, path) 

        path.pop() 
        visited[u]= False
      
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
         if fittest.getFitness() <= self.getChemin(i).getFitness() :
            fittest = self.getChemin(i)
      return fittest
   
   def taillePopulation(self):
      return len(self.chemins)




