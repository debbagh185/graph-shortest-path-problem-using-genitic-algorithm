#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:18:28 2020

@author: Brahim DEBBAGH
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

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
     
   def getIndex(self, value) :
       return self.chemin.index(value)
     
    
   def hasValideConnections(self):
       for i in range(0,len(self.chemin)):
           if i+1<len(self.chemin) and (self.chemin[i] not in self.chemin[i+1].get_connections()):
               self.valide = False
       return self.valide

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
 
   def removeNones(self):
        newChemin = []
        for chemin in self.chemin:
            if chemin is not None: newChemin.append(chemin)
        return Chemin(self.graph, newChemin)

   def getCout(self):
     cheminWithoutNones = self.removeNones()
     if self.cout == 0 :
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
 
   def convert_to_tuples(self) :
       newChemin = []
       for chemin in self.chemin:
         if chemin is not None: newChemin.append(chemin)
       cheminWithoutNones = Chemin(self.graph, newChemin)
       tuples = []
       for i in range(0,cheminWithoutNones.tailleChemin()) : 
           if(i+1<=cheminWithoutNones.tailleChemin()-1):
               t = (cheminWithoutNones.chemin[i].get_id(),cheminWithoutNones.chemin[i+1].get_id())
               tuples.append(t)
       return tuples

class Vertex:
    def __init__(self, node, pos):
        self.id = node
        self.pos = pos
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id
    
    def get_pos(self):
        return self.pos

    def get_weight(self, neighbor):
         if neighbor is not None :
            if neighbor in self.get_connections() :
                return self.adjacent[neighbor]
            return 1000
         else : return 0


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def __getitem__(self):
        return self.vert_dict

    def add_vertex(self,pos=(0,0),etat=None):
        node = str(pos[0])+str(pos[1])
        if etat is not None : 
            if etat == 'src': 
                self.sourceId = node
            elif etat == 'dest': 
                self.destId = node
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node,pos)
        self.vert_dict[node] = new_vertex
        return new_vertex
   
   
    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, toList):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        for to in toList :
            if to[0] not in self.vert_dict:
                self.add_vertex(to[0])
            self.vert_dict[frm].add_neighbor(self.vert_dict[to[0]], to[1])
            self.vert_dict[to[0]].add_neighbor(self.vert_dict[frm], to[1])

    def get_vertices(self):
        return self.vert_dict.keys()
    
    def nombreNoeuds(self):
        return self.num_vertices
    def setNombreNoeuds(self, nombre):
        self.num_vertices = nombre
        
    def drawGraph(self,shortestPath=None):
        G = nx.DiGraph()
        for n in self.get_vertices() : 
            G.add_node(n, pos = self.get_vertex(n).get_pos())
            
        for v in self :
            for w in v.get_connections():
                G.add_edge(v.get_id(), w.get_id(), weight=v.get_weight(w))
        plt.figure(figsize=(8,6))
        pos=nx.get_node_attributes(G,'pos')
        if(shortestPath is not None):
            elseEdges=[(u,v) for (u,v,d) in G.edges(data=True) if (u,v) not in shortestPath]
            nx.draw_networkx_nodes(G,pos)
            nx.draw_networkx_edges(G,pos,edgelist=shortestPath, width=6, edge_color='r')
            nx.draw_networkx_edges(G,pos,edgelist=elseEdges)
            nx.draw_networkx_labels(G,pos)
        else :
            nx.draw_networkx(G,pos,with_labels=True)
        
        edge_labels =dict([((u, v), d['weight']) for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        
        plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
        plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
        for pos in ['right','top','bottom','left']:
            plt.gca().spines[pos].set_visible(False)
        
        plt.show()