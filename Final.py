from copy import deepcopy
import numpy as np
import random
from collections import deque

random.seed(5)

def generer_matrice_adjacence(taille,typeDeGraphe):
    matrice = np.empty((taille, taille))              
    if(typeDeGraphe == 'Complete'):               
        for i in range(taille):
            for j in range(i,taille):
                valeur = 1 if i!=j else 0 
                matrice[i][j] = valeur
                matrice[j][i] = valeur
    else:
         for i in range(taille):
            for j in range(i,taille):
                valeur = random.randint(0, 1)  if i!=j else 0
                matrice[i][j] = valeur
                matrice[i][j] = valeur
    return matrice
    

matriceAdjacence = generer_matrice_adjacence(10, "Complete")
print(matriceAdjacence)

def generer_matrice_pondere(matrice):
    for i in range(len(matrice)):
        for j in range(i,len(matrice)):
            if(matrice[i][j] != 0):
                valeur = random.randint(0, 999)
                matrice[i][j] = valeur
                matrice[j][i] = valeur
    return matrice

matricePondere = generer_matrice_pondere(matriceAdjacence)
print(matricePondere)
def generate_time_window(matrice):
    timeWindow = {}
    for i in range(len(matrice)):
        timeOne = random.randint(1,4*len(matrice))
        timeTwo = random.randint(timeOne+1,4*len(matrice)+1)
        timeWindow[i] = tuple([timeOne,timeTwo])
    timeWindow[0] = tuple([0,max(max(timeWindow.values())) + random.randint(0,len(matrice))])
    timeWindow[len(matrice)] = timeWindow[0]
    return timeWindow

tw = generate_time_window(matricePondere)
print(tw)

def generate_solution(matrice):
    sol = {}
    matriceSearch = [i for i in range(len(matrice))]
    matriceSearch.remove(0)
    i = 0
    while (len(matriceSearch) > 0):
        way = []
        way.append(0)
        for j in range(0,random.randint(1,len(matrice)-4)) :
            if len(matriceSearch) > 0 :
                value = random.choice(matriceSearch)
                way.append(value)
                matriceSearch.remove(value)
            else: 
                break
        way.append(0)
        sol[i] = way
        i += 1
    return sol

sol = generate_solution(matricePondere)


# def generate_solution(matrice,tw):
#     sol = []
#     matriceSearch = [i for i in range(len(matrice))]
#     matriceSearch.remove(0)
#     sol.append(0)
#     for i in range(len(matrice)-1):
#         value = random.choice(matriceSearch)
#         value = random.choice(matriceSearch)
#         sol.append(value)
#         matriceSearch.remove(value)
#     sol.append(0)
#     return sol

# sol = generate_solution(matricePondere,tw)
# print(sol, "sol init")

def voisinage(sol:dict):
    voisinage = []
    for j in range(len(sol)):
        for i in range (1,len(sol[j])-2):
            voisin = deepcopy(sol)
            voisin[j] = sol[j][:i]+[sol[j][i+1],sol[j][i]]+sol[j][i+2:]
            voisinage.append(voisin)
    return voisinage



def weightSol(sol):
    return sum(matricePondere[sol[i][j]][sol[i][j+1]] for i in sol for j in range(len(sol[i])-1))

def recherche_tabou(solution_initiale, taille_tabou, iter_max):
    """
    1. On part d'un élément de notre ensemble de recherche qu'on déclare élément courant
    2. On considère le voisinage de l'element courant et on choisit le  meilleur d'entre
       eux comme nouvel element courant, parmi ceux absents de la liste tabou, et on l'ajoute
       a la liste tabou
    3. On boucle jusqu'a condition de sortie.
    """
    nb_iter = 0                                                                
    liste_tabou = deque((), maxlen = taille_tabou)                             
                                                                               
    # variables solutions pour la recherche du voisin optimal non tabou        
    solution_courante = solution_initiale                                      
    meilleure = solution_initiale                                              
    meilleure_globale = solution_initiale                                      
                                                                               
    # variables valeurs pour la recherche du voisin optimal non tabou          
    valeur_meilleure = weightSol(solution_initiale)                       
    valeur_meilleure_globale = valeur_meilleure                                
                                                                               
    while (nb_iter < iter_max):                                                
                                               
                                                                               
        # on parcourt tous les voisins de la solution courante                 
        for voisin in voisinage(solution_courante):                            
            valeur_voisin=weightSol(voisin)                         
                                                                               
            # MaJ meilleure solution non taboue trouvée                        
            if valeur_voisin < valeur_meilleure and voisin not in liste_tabou: 
                valeur_meilleure = valeur_voisin                               
                meilleure = voisin                                             
                                                                               
        # on met à jour la meilleure solution rencontrée depuis le début       
        if valeur_meilleure < valeur_meilleure_globale:                        
            meilleure_globale = meilleure                                      
            valeur_meilleure_globale = valeur_meilleure                        
            nb_iter = 0                                                        
        else:                                                                  
            nb_iter += 1                                                       
                                                                               
        # on passe au meilleur voisin non tabou trouvé                         
        solution_courante = meilleure                                          
                                                                               
        # on met à jour la liste tabou                                         
        liste_tabou.append(solution_courante)                                  
                                                                               
    return meilleure_globale   
print(sol)   
solfin = recherche_tabou(sol,5,50)
print(weightSol(solfin ),solfin )
