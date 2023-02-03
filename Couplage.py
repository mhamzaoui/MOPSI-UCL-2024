import numpy as np
import py_bipartite_matching as pbm
import networkx as nx
import math

Winners = [['NAP', 'A', 'ITA'],['POR','B','POR'],['BAY','C','GER'], ['TOT','D','ENG'],['CHE','E','ENG'],['Real','F',"SPA"],['ManC','G',"ENG"],['BEN','H','POR']]
Runners_up = [['LIV','A','ENG'],['BRU','B','BEL'],['INT','C','ITA'],['FRA','D','GER'],['MIL','E','ITA'],['LEI','F','GER'],['DOR','G','GER'],['PSG','H','FRA']]
n = len(Winners)

def initialize(winners,runners_up):
    edges=[]
    for i in range(len(winners)):
        for j in range(len(runners_up)):
            if winners[i][1] != runners_up[j][1] and winners[i][2] != runners_up[j][2]:
                edges.append((winners[i][0],runners_up[j][0]))

    return edges

# Initialise graph
B = nx.Graph()# Add nodes with the node attribute "bipartite"
left_nodes = [W[0] for W in Winners]
right_nodes = [R[0] for R in Runners_up]
B.add_nodes_from(left_nodes, bipartite=0)
B.add_nodes_from(right_nodes, bipartite=1) # Add edges only between nodes of opposite node sets
B.add_edges_from(initialize(Winners,Runners_up))

nb_matchings = 0
matchings = []
for matching in pbm.enum_maximum_matchings(B):
    nb_matchings += 1
    matchings.append(list(matching.items()))


#définir une fonction
'''
def probability(X, matching):
  # Calcule la probabilité p(x) en utilisant la formule donnée
  res = 0
  for i in X:
      X.remove(i)
      res = probability(X, matching) / a(X, i)
  p = 1 / (n - len(X) + 1)*res

  return p

def voisins(G,X):
    neighbors = []
    for i in X:
        voisins = list(G.neighbors(i))
        for v in voisins:
            neighbors.append(v)
    return list(set(neighbors))

print(voisins(B,left_nodes))


def a(G,X, i):
  # Calcule le nombre d'arêtes incidentes à i contenues dans un couplage parfait de G privé de X et M(X)
  M_X = voisins(G,X)
  for m in matching:
      if m[0] == i and i not in X:
          break
  return sum(1 for (u, v) in matching if u == i and v not in X)

for matching in matchings:
  #prob = probability(right_nodes, matching)
  #print(f"Probabilité de tirer le couplage parfait {matching}: {prob}")
  print(a(matching,'PSG'))'''