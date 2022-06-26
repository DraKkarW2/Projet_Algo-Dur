from copy import deepcopy
import numpy as np
import random

random.seed(11)

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
        timeTwo = random.randint(timeOne,4*len(matrice))
        timeWindow[i] = tuple([timeOne,timeTwo])
    timeWindow[0] = tuple([max(max(timeWindow.values()))+ random.randint(0,len(matrice))])
    timeWindow[len(matrice)] = timeWindow[0]
    return timeWindow

tw = generate_time_window(matricePondere)
print(tw)

capacity = 20
def generate_capacity(matrice,capacityTruck):
    capacity = []
    for i in range(len(matrice)):
        valueCustomers = random.randint(1,capacityTruck-10)
        capacity.append(valueCustomers)
    return capacity
cp = generate_capacity(matricePondere,capacity)
print(cp)


def generate_solution(matrice):
    sol = {}
    matriceSearch = [i for i in range(len(matrice))]
    matriceSearch.remove(0)
    i = 1
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

print(generate_solution(matricePondere))


