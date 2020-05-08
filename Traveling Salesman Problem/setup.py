#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 20:53:51 2020

@author: Brahim DEBBAGH
"""

from GeneticAlgorithm import GA
from Circuit import Carte
from Ville import Ville
from Population import Population


if __name__ == '__main__':
    
   carte = Carte()   

   ville1 = Ville(3.002556, 45.846117, 'Clermont-Ferrand')
   carte.ajouterVille(ville1)
   ville2 = Ville(-0.644905, 44.896839, 'Bordeaux')
   carte.ajouterVille(ville2)
   ville3 = Ville(-1.380989, 43.470961, 'Bayonne')
   carte.ajouterVille(ville3)
   ville4 = Ville(1.376579, 43.662010, 'Toulouse')
   carte.ajouterVille(ville4)
   ville5 = Ville(5.337151, 43.327276, 'Marseille')
   carte.ajouterVille(ville5)
   ville6 = Ville(7.265252, 43.745404, 'Nice')
   carte.ajouterVille(ville6)
   ville7 = Ville(-1.650154, 47.385427, 'Nantes')
   carte.ajouterVille(ville7)
   ville8 = Ville(-1.430427, 48.197310, 'Rennes')
   carte.ajouterVille(ville8)
   ville9 = Ville(2.414787, 48.953260, 'Paris')
   carte.ajouterVille(ville9)
   ville10 = Ville(3.090447, 50.612962, 'Lille')
   carte.ajouterVille(ville10)
   ville11 = Ville(5.013054, 47.370547, 'Dijon')
   carte.ajouterVille(ville11)
   ville12 = Ville(4.793327, 44.990153, 'Valence')
   carte.ajouterVille(ville12)
   ville13 = Ville(2.447746, 44.966838, 'Aurillac')
   carte.ajouterVille(ville13)
   ville14 = Ville(1.750115, 47.980822, 'Orleans')
   carte.ajouterVille(ville14)
   ville15 = Ville(4.134148, 49.323421, 'Reims')
   carte.ajouterVille(ville15)
   ville16 = Ville(7.506950, 48.580332, 'Strasbourg')
   carte.ajouterVille(ville16)
   ville17 = Ville(1.233757, 45.865246, 'Limoges')
   carte.ajouterVille(ville17)
   ville18 = Ville(4.047255,48.370925, 'Troyes')
   carte.ajouterVille(ville18)
   ville19 = Ville(0.103163,49.532415, 'Le Havre')
   carte.ajouterVille(ville19)
   ville20 = Ville(-1.495348, 49.667704, 'Cherbourg')
   carte.ajouterVille(ville20)
   ville21 = Ville(-4.494615, 48.447500, 'Brest')
   carte.ajouterVille(ville21)
   ville22 = Ville(-0.457140, 46.373545, 'Niort')
   carte.ajouterVille(ville22)   

   pop = Population(carte, 50, True)
   print("Distance initiale : " + str(pop.getFittest().getDistance()))
   
   ga = GA(carte)
   pop = ga.evoluerPopulation(pop)
   for i in range(0, 200):
      pop = ga.evoluerPopulation(pop)
   
   print("Distance finale : " + str(pop.getFittest().getDistance()))
   meilleurePopulation = pop.getFittest()

   lons = []
   lats = []
   noms = []
   for ville in meilleurePopulation.circuit:
      lons.append(ville.lon)
      lats.append(ville.lat)
      noms.append(ville.nom)

   lons.append(lons[0])
   lats.append(lats[0])
   noms.append(noms[0])



