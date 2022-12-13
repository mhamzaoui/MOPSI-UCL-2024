import numpy as np
import networkx as nx
from networkx.algorithms import bipartite
Winners = [['NAP','A','ITA' ],['POR','B','POR'],['BAY','C','GER'], ['TOT','D','ENG'],['CHE','E','ENG'],['Real','F',"SPA"],['ManC','G',"ENG"],['BEN','H','POR']]
Runners_up = [['LIV','A','ENG'],['BRU','B','BEL'],['INT','C','ITA'],['FRA','D','GER'],['MIL','E','ITA'],['LEI','F','GER'],['DOR','G','GER'],['PSG','H','FRA']]
edges=[]
def initialize(winners,runners_up):
    edges=[]
    for i in range(len(winners)):
        for j in range(len(runners_up)):
            if winners[i][1] != runners_up[j][1] and winners[i][2] != runners_up[j][2]:
                edges.append((winners[i][0],runners_up[j][0]))

    return edges
G=nx.Graph()
G.add_nodes_from([W[0] for W in Winners], bipartite=1)
G.add_nodes_from([R[0] for R in Runners_up],bipartite=0)
G.add_edges_from(initialize(Winners,Runners_up))
bipartite.is_bipartite(G)
nx.draw_networkx(G, pos = nx.drawing.layout.bipartite_layout(G, [R[0] for R in Runners_up]), width = 2)


def chaine_aug(G,C):
    P=G-C
    pred=np.array([0]*len(G))
    while len(P)!=0:
        F=[P[-1]]
        P.pop()
        M=F
        while len(F)!=0:
            x=F[0]
            F=F[1:]
