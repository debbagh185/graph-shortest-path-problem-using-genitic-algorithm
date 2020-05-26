#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:55:52 2020

@author: Brahim DEBBAGH
"""

import graph as utils

if __name__ == '__main__':
    
    # On define les sommets de notre graphe
    vertices = [
        (1,1),(1,2),(1,3),(1,4),(1,5),
        (2,1),(2,2),(2,3),(2,4),(2,5),
        (3,1),(3,2),(3,3),(3,4),(3,5),
        (4,1),(4,2),(4,3),(4,4),(4,5)
        ]
    
    #on define les arcs de notre graph
    edges = {
     '11':[('12',7),('22',11)],
     '12':[('13',7),('22',7)],
     '13':[('14',7),('23',7)],
     '14':[('15',7),('24',7),('25',7)],
     '15':[('25',7)],
     '21':[('22',7),('32',7)],
     '22':[('32',7),('23',1)],
     '23':[('14',2),('24',0.5),('33',7)],
     '24':[('15',7),('25',7),('35',0.7),('34',7)],
     '25':[('35',7)],
     '31':[('22',0.001),('32',700),('42',2),('45',100)],
     '32':[('33',7),('43',7),('42',7)],
     '33':[('24',7),('34',7),('44',7),('43',7)],
     '34':[('25',7),('35',7),('45',7),('44',7)],
     '35':[('45',100)],
     '41':[('42',7)],
     '42':[('43',1)],
     '43':[('34',7),('44',0.001)],
     '44':[('34',7),('45',0.001)],
     '45':[('45',0.3)]
     }
    
    emptyGraph = utils.creerGraph()
    
    graphWithoutConnections = utils.add_vertices(emptyGraph,vertices,src='31',dest='45')
    
    g = utils.add_edges(graphWithoutConnections,edges)
    
    utils.drawGraph(g)

    pop = utils.creerPopulation(g, 200, True)
    
    print("Première génération : ")
    utils.displayPop(pop)
    
    ga = utils.GA()
    
    
    for i in range(0, 100):
        pop = utils.evoluerPopulation(ga,g,pop)
        print("G-"+str(i+1))
        utils.displayPop(pop)
        
    print("Chemin finale : " + str(utils.getCout(g, utils.getFittest(g, pop))))
    
    meilleurChemin = utils.removeNones(utils.getFittest(g, pop))
    
    #if(meilleurChemin.hasValideConnections()) : 
    utils.drawGraph(g, utils.convert_to_tuples(g, meilleurChemin))

 
    
 