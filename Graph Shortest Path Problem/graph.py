#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:18:28 2020

@author: Brahim DEBBAGH
"""

import random
import numpy as np

class Chemin:
   def __init__(self, graph, chemin=None):
      self.graph = graph
      self.chemin = []
      self.fitness = 0.0
      self.cout = 0
      self.valide = True
      if chemin is not None:
         self.chemin = chemin  
      else:
         for i in range(0, self.graph.nombreNoeuds()):
            self.chemin.append(None)

   def __len__(self):
      return len(self.chemin)
  
   def __str__(self):
      l = []
      for noeud in self.chemin:
         if noeud is not None:
             l.append(noeud.get_id())
      return str(l)+" Coût : "+str(self.getCout())
   
   def __getitem__(self, index):
     return self.chemin[index]

   def __setitem__(self, key, value):
     self.chemin[key] = value
     
    
   def hasValideConnections(self):
       newChemin = []
       for chemin in self.chemin:
            if chemin is not None: newChemin.append(chemin)
       cheminWithoutNones = Chemin(self.graph, newChemin)
       for i in range(0,len(newChemin)):
           if i+1<len(newChemin) and (cheminWithoutNones.chemin[i] not in cheminWithoutNones.chemin[i+1].get_connections()):
               self.valide = False
       return self.valide
   
   def genererIndividu(self):
         self.setNoeud(0, self.graph.get_vertex(self.graph.sourceId))
         i=1     
         vertices = list(self.graph.get_vertices())
         random.shuffle(vertices)
         for v in vertices:
             if v != self.graph.sourceId and v != self.graph.destId:
                 self.setNoeud(i, self.graph.get_vertex(v))
                 i=i+1
         self.setNoeud(i, self.graph.get_vertex(self.graph.destId))

   def getNoeud(self, cheminPosition):
     return self.chemin[cheminPosition]

   def setNoeud(self, cheminPosition, noeud):
     self.chemin[cheminPosition] = noeud
     self.fitness = 0.0
     self.cout = 0
     
   def removeNoeud(self, cheminPosition):
       self.chemin[cheminPosition] = None
         
   def swap(self,cheminPos1, cheminPos2):
       noeud1 = self.getNoeud(cheminPos1)
       noeud2 = self.getNoeud(cheminPos2)       
       self.setNoeud(cheminPos2, noeud1)
       self.setNoeud(cheminPos1, noeud2)

   def getFitness(self):
     if self.fitness == 0:
        self.fitness = 1/float(self.getCout())
     return self.fitness

   def getCout(self):
     if(not self.hasValideConnections()):
        return np.Infinity
     newChemin = []
     for chemin in self.chemin:
         if chemin is not None: newChemin.append(chemin)
     cheminWithoutNones = Chemin(self.graph, newChemin)
     if self.cout == 0:
        cheminCout = 0
        for indiceNoeud in range(0, cheminWithoutNones.tailleChemin()):
           noeudOrigine = cheminWithoutNones.getNoeud(indiceNoeud)
           noeudArrivee = None
           if indiceNoeud+1 < cheminWithoutNones.tailleChemin():
              noeudArrivee = cheminWithoutNones.getNoeud(indiceNoeud+1)
              
           cheminCout += noeudOrigine.get_weight(noeudArrivee)
        self.cout = cheminCout
     return self.cout

   def tailleChemin(self):
     return len(self.chemin)

   def contientNoeud(self, noeud):
     return noeud in self.chemin

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        if neighbor is None:
            return 0
        return self.adjacent[neighbor]


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def __getitem__(self):
        return self.vert_dict

    def add_vertex(self, node, position=None):
        if position is not None : 
            if position == 'src': 
                self.sourceId = node
            elif position == 'dest': 
                self.destId = node
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()
    
    def nombreNoeuds(self):
        return self.num_vertices
    def setNombreNoeuds(self, nombre):
        self.num_vertices = nombre
        