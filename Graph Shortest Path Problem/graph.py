#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:18:28 2020

@author: Brahim DEBBAGH
"""

import random
import matplotlib.pyplot as plt
import networkx as nx
import copy
 
class DictAttr(dict):
    def __getattr__(self, key):
        if key not in self:
            raise AttributeError(key)
        return self[key]
 
    def __setattr__(self, key, value):
        self[key] = value
 
    def __delattr__(self, key):
        del self[key]


def GA():
   return DictAttr({'tauxMutation':0.015,'tailleTournoi':5,'elitisme':True})
   
def evoluerPopulation(ga,graph,pop):
   nouvellePopulation = creerPopulation(graph, taillePopulation(pop), False)
   elitismeOffset = 0
   if ga.elitisme:
      meilleurChemin = getFittest(graph, pop)
      nouvellePopulation[0] =  meilleurChemin
      elitismeOffset = 1
   for i in range(elitismeOffset, taillePopulation(nouvellePopulation)):
      parent1 = selectionTournoi(ga, graph, pop)
      parent2 = selectionTournoi(ga, graph, pop)
      enfant = crossover(graph, parent1, parent2)
      nouvellePopulation[i] = enfant
      
   for i in range(elitismeOffset, taillePopulation(nouvellePopulation)):
      nouvellePopulation[i] = muter(ga, nouvellePopulation,i)
      
   return nouvellePopulation


def crossover(graph, parent1, parent2):
   randomIndex = random.choice(range(1,tailleChemin(parent1)))
   if parent1.data[randomIndex] in parent2.data :
       firstChild = parent1.data[:randomIndex]+parent2.data[randomIndex:]
       secondChild = parent2.data[:randomIndex]+parent1.data[randomIndex:]
       randomChild = random.choice([firstChild,secondChild])
       enfant = creerChemin(graph,randomChild)
       return enfant
   return parent1

              
def muter(ga, pop, cheminIndex) :
   chemin = getChemin(pop, cheminIndex)
   for cheminPos1 in range(1, tailleChemin(chemin)-1):
      cheminPos2 = random.choice(range(1,tailleChemin(chemin)-1))
      if random.random() < ga.tauxMutation :
         return swap(chemin, cheminPos1, cheminPos2) if(random.choice([True,False])) else removeNoeud(chemin, cheminPos2) 
   return chemin

def selectionTournoi(ga, graph, pop):
   tournoi = creerPopulation(graph, ga.tailleTournoi, False)
   for i in range(0, ga.tailleTournoi):
      randomId = int(random.random()*taillePopulation(pop))
      tournoi[i] = getChemin(pop, randomId)
   fittest = getFittest(graph, tournoi)
   return fittest
       
def creerPopulation(graph, taillePopulation, init):  
    if init : 
        return [genererIndividu(graph) for i in range(0, taillePopulation)]
    return [None]*taillePopulation

def cheminToString(chemin) : 
    return list([vertex.id for vertex in chemin.data])
  
def displayPop(pop):
    for chemin in pop:
        print(cheminToString(removeNones(chemin)))
   
def getChemin(pop, index):
    return pop[index]
   
def getFittest(graph, pop):
      fittest = pop[0]
      for i in range(0, taillePopulation(pop)):
         if getFitness(graph, fittest) <= getFitness(graph, getChemin(pop,i)) :
            fittest = getChemin(pop,i)
      return fittest
  
    
def getSmallChemin(pop):
      small = pop[0]
      for i in range(0, taillePopulation(pop)):
         if tailleChemin(small) >= tailleChemin(getChemin(pop,i)) :
            small = getChemin(pop,i)
      return small
   
def taillePopulation(pop):
      return len(pop)

def creerChemin(graph,data=None):
    return DictAttr({
        'data':data if data!=None else nombreNoeuds(graph)*[None],
         'fitness':0,
         'cout':0,
         'valide':True
         })
      
def getIndex(chemin, value) :
       return chemin.data.index(value)
     
def hasValideConnections(chemin):
       newChemin = copy.deepcopy(chemin)
       for i in range(0,len(newChemin.data)):
           if i+1<len(newChemin.data) and (newChemin.data[i] not in get_connections(newChemin.data[i+1].id)):
               newChemin.valide = False
       return newChemin.valide

def getNoeud(chemin, cheminPosition):
     return chemin.data[cheminPosition]

def setNoeud(chemin, cheminPosition, noeud):
     newChemin = copy.deepcopy(chemin)
     newChemin.data[cheminPosition] = noeud
     newChemin.fitness = 0.0
     newChemin.cout = 0
     return newChemin
     
def removeNoeud(chemin, cheminPosition):
     newChemin = copy.deepcopy(chemin)
     newChemin.data[cheminPosition] = None
     return newChemin
         
def swap(chemin,cheminPos1, cheminPos2):
    newChemin = copy.deepcopy(chemin)     
    newChemin = setNoeud(newChemin,cheminPos2, getNoeud(chemin,cheminPos1))
    newChemin = setNoeud(newChemin,cheminPos1, getNoeud(chemin,cheminPos2))
    return newChemin

def getFitness(graph, chemin):
    if chemin.fitness == 0:
        chemin.fitness = 1/float(getCout(graph,chemin)+1)
    return chemin.fitness
 
def genererIndividu(graph):
    chemin = creerChemin(graph)
    chemin = setNoeud(chemin, 0, get_vertex(graph, graph.sourceId))
    i=1     
    vertices = list(get_vertices(graph))
    random.shuffle(vertices)
    for v in vertices:
        if v != graph.sourceId and v != graph.destId:
            chemin = setNoeud(chemin, i, get_vertex(graph,v))
            i=i+1
    chemin = setNoeud(chemin, i, get_vertex(graph, graph.destId))
    return chemin
 
def removeNones(chemin):
     newChemin = copy.deepcopy(chemin)
     newData = list(filter(lambda x: x is not None, newChemin.data))
     newChemin.data = newData
     return newChemin

def getCout(graph, chemin):
    cheminWithoutNones = removeNones(chemin)
    if chemin.cout == 0 :
        cheminCout = 0
        for indiceNoeud in range(0, tailleChemin(cheminWithoutNones)):
              noeudOrigine = getNoeud(cheminWithoutNones,indiceNoeud).id
              noeudArrivee = None
              if indiceNoeud+1 < tailleChemin(cheminWithoutNones):
                 noeudArrivee = getNoeud(cheminWithoutNones,indiceNoeud+1).id 
              cheminCout += get_weight(graph, noeudOrigine,noeudArrivee)
        chemin.cout = cheminCout
    return chemin.cout

def tailleChemin(chemin):
   return len(chemin.data)

def contientNoeud(chemin, noeud):
   return noeud in chemin.data
 
def convert_to_tuples(graph, chemin) :
   newChemin = []
   for vertex in chemin.data:
      if vertex is not None: newChemin.append(vertex)
   cheminWithoutNones = creerChemin(graph, newChemin)
   tuples = []
   for i in range(0,tailleChemin(cheminWithoutNones)) : 
      if(i+1<=tailleChemin(cheminWithoutNones)-1):
          t = (cheminWithoutNones.data[i].id,cheminWithoutNones.data[i+1].id)
          tuples.append(t)
   return tuples


def add_neighbor(graph,origin, neighbor, weight=0):
    graph.vert_dict[origin].adjacent[neighbor] = weight 

def creerGraph() :
    return DictAttr({'num_vertices':0, 'vert_dict':{},'sourceId':None, 'destId':None})

def add_vertices(graph, vertices, src, dest):
    newGraph = DictAttr(copy.deepcopy(graph))
    newGraph.sourceId = src
    newGraph.destId = dest
    for pos in vertices :
        node = str(pos[0])+str(pos[1])
        new_vertex = creerVertex(node,pos)
        newGraph.vert_dict[node] = new_vertex
        newGraph.num_vertices = newGraph.num_vertices+1
    return newGraph
   
def creerVertex(node, pos):
   return DictAttr({'id':node,'pos':pos,'adjacent':{}})
   
def get_vertex(graph, n):
    if n in graph.vert_dict:
        return graph.vert_dict[n]
    else:
        return None

def get_id(vertex):
    return vertex.id

def get_weight(graph, origin, neighbor):
    if neighbor is not None :
        if neighbor in get_connections(graph,origin) :
            return get_adjacent(graph, origin, neighbor)
        return 1000
    return 0

def get_connections(graph,vertex):
    return graph.vert_dict[vertex].adjacent.keys()

def get_adjacent(graph,origin, neighbor):
    return graph.vert_dict[origin].adjacent[neighbor]

def get_pos(vertex):
    return vertex.pos

def add_edges(graph,edges):
    newGraph = DictAttr(copy.deepcopy(graph))
    for frm,toList in edges.items() :
        for to in toList :
            newGraph.vert_dict[frm].adjacent[newGraph.vert_dict[to[0]].id] = to[1]
            newGraph.vert_dict[to[0]].adjacent[newGraph.vert_dict[frm].id] = to[1]
    return newGraph

def setSource(graph,source) : 
    newGraph = DictAttr(graph)
    newGraph.sourceId = source
    return newGraph

def setDestination(graph,dest) : 
    newGraph = DictAttr(graph)
    newGraph.destId = dest
    return newGraph
       
    
def get_vertices(graph):
    return graph.vert_dict.keys()
    
def nombreNoeuds(graph):
    return graph.num_vertices
    
def changeNombreNoeuds(graph, nombre):
    newGraph = DictAttr(graph)
    newGraph.num_vertices = nombre
    return newGraph
        
def drawGraph(graph,shortestPath=None):
    G = nx.DiGraph()
    for n in get_vertices(graph) : 
        G.add_node(n, pos = get_pos(get_vertex(graph,n)))
            
    for v in graph.vert_dict :
        for w in get_connections(graph,v):
            G.add_edge(v, w, weight=get_weight(graph,v,w))
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