import numpy as np



#List of teams that reached the round of 16 for the 2023 Champions League

Winners = [['NAP','A','ITA' ],['POR','B','POR'],['BAY','C','GER'], ['TOT','D','ENG'],['CHE','E','ENG'],['Real','F',"SPA"],['ManC','G',"ENG"],['BEN','H','POR']]
Runners_up = [['LIV','A','ENG'],['BRU','B','BEL'],['INT','C','ITA'],['FRA','D','GER'],['MIL','E','ITA'],['LEI','F','GER'],['DOR','G','GER'],['PSG','H','FRA']]

#On crée un graph G où chaque noeud représente une équipe, deux noeuds sont
#connectés s'ils n'appartiennent pas au même pays (répondent à la contrainte).
#G est une matrice de taille nb_teams² où aij = 1 si les équipes peuvent jouer l'une contre l'autre 0 sinon.

def initialize(winners,runners_up):
    fullCompatibilityMatrix = np.zeros((len(winners),len(runners_up)))
    for i in range(len(winners)):
        for j in range(len(runners_up)):
            if winners[i][1] == runners_up[j][1] or winners[i][2] == runners_up[j][2]:
                fullCompatibilityMatrix[i,j] = 0
            else:
                fullCompatibilityMatrix[i,j] = 1

    return fullCompatibilityMatrix



def computeProbabilities(compatibilityMatrix,unmatchedRunnerUp):
    options = 0
    size = compatibilityMatrix.shape[0]
    probabilities = np.zeros((size,size))


    # 1er cas: On choisit le prochain runner-up
    if unmatchedRunnerUp == None:
        for i in range(size): # On itère avec sur tous les runners-up (les équipes pouvant être tirées)
            # puis on appelle récursivement la fonction de calcul avec les paramètres (G,runner-up)
            options += 1
            conditionalProbabilities = computeProbabilities(compatibilityMatrix,i)
            if conditionalProbabilities.shape[0] == 0:
                # On ignore les runners-up pour lesquels la fonction récursive renvoie NULL
                options -= 1
            else:
                # Retourne un graph complet contentant les noeuds de G où chaque
                # arc a un poids dans [0,1] qui indique la probabilité d'un match
                # entre les deux équipes connectées.
                for j in range(size):
                    for k in range(size):
                        probabilities[j][k] += conditionalProbabilities[j][k]

        if options == 0 and size > 0:# Retourne NULL si tous les appels récursifs renvoie NULL (ie impasse)
            probabilities = np.array([])

    else: #2ème cas : on doit choisir l'équipe pour le runner-up choisit
          # (ie le unmatched runner-up)
        for i in range(size): # i est le winner
            if compatibilityMatrix[i][unmatchedRunnerUp] == 1: # Si il existe un arc en i et unmatchedRunnerUp
                options += 1 # On ajoute un voisin
                #Création de la sous matrice  G' = G\{unmatched runner-up,winner}.
                subMatrix = np.delete(np.delete(compatibilityMatrix,i, axis = 0),unmatchedRunnerUp, axis = 1)
                if subMatrix.shape[0] != 0:
                    # appeller récursivement la fonction de calcul de probabilité avec G'
                    conditionalProbabilities = computeProbabilities(subMatrix, None)
                    if conditionalProbabilities.shape[0] == 0:
                        options -= 1 # On retire un le voisin qui mène a une impasse
                    else:
                    # retourner un graph complet contenant tous les noeuds de G où les arcs ont des poids
                    # dans [0,1] indicant la probabilité d'un match entre les deux équipes connectées.
                        for j in range(size):
                            for k in range(size):
                                if j < i:
                                    if k < unmatchedRunnerUp:
                                        probabilities[j][k] += conditionalProbabilities[j][k]
                                    if k > unmatchedRunnerUp:
                                        probabilities[j][k] += conditionalProbabilities[j][k-1]
                                elif j > i:
                                    if k < unmatchedRunnerUp:
                                        probabilities[j][k] += conditionalProbabilities[j-1][k]
                                    if k > unmatchedRunnerUp:

                                        probabilities[j][k] += conditionalProbabilities[j-1][k-1]

                else:
                    probabilities[i][unmatchedRunnerUp] += 1

        if options == 0:  #Retourne NULL si le tirage actuel est sans issues
            probabilities = np.array([])
    if options != 0:
        for i in range(size):
            for j in range(size):
                probabilities[i][j] /= options
    return probabilities





fullCompatibilityMatrix = initialize(Winners,Runners_up)
print(fullCompatibilityMatrix)

print(computeProbabilities(fullCompatibilityMatrix,None))
