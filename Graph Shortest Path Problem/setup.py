#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:55:52 2020

@author: Brahim DEBBAGH
"""

from graph import Graph
from population import Population
from geneticAlgorithm import GA

if __name__ == '__main__':
    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b','src')
    g.add_vertex('c')
    g.add_vertex('d','dest')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('e', 'a', 7)  
    g.add_edge('a', 'c', 1)
    g.add_edge('c', 'b', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('d', 'c', 2)
    g.add_edge('c', 'f', 2)
    g.add_edge('e', 'd', 6)
    g.add_edge('e', 'b', 4)
    g.add_edge('b', 'f', 6)
    
    pop = Population(g,50, True)
    print("Première génération : ")
    pop.displayPop()
    print("Chemin initiale : " + str(pop.getFittest()))
    
    ga = GA(g)
    
    for i in range(0, 200):
        pop = ga.evoluerPopulation(pop)
        print("G-"+str(i+2))
        pop.displayPop()
    print("Chemin finale : " + str(pop.getFittest()))
    meilleurePopulation = pop.getFittest()
 
    
 