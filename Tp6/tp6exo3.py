import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

#Question 1

NUI = []
NOM = []
Al = []
CP = []
LG = []
LT = []
POP = []
SUF = []

with open("C:/eyosias/PythonExo/Tp6/villes.csv" , encoding = "utf - 8") as f:
    for ligne in f:
        if (ligne[0] != "I"):
            l = ligne.replace(",", ".")
            donnees = l.split(";")
            NUI.append(donnees[0])
            NOM.append(donnees[1])
            Al.append(float(donnees[2]))
            CP.append(donnees[3])
            LG.append(float(donnees[4]))
            LT.append(float(donnees[5]))
            POP.append(float(donnees[6]))
            SUF.append(float(donnees[7]))

def ReturnName(name):
    for i in range(len(NOM)):
        if (NOM[i] == name):
            return i

def Commune():
    indice = ReturnName("Clermont-Ferrand")
    lat_vil = LT[indice]
    lg_vil = LG[indice]
    list_comm = []
    for i in range(len(NUI)):
        if (NOM[i] != "Clermont-Ferrand"):
            if (NUI[i][0] == '6' and NUI[i][1] == '3'):
                list_comm.append(NOM[i])
    return list_comm


def Dist():
    Dist = []
    indice = ReturnName("Clermont-Ferrand")
    lat_vil = LT[indice]
    lg_vil = LG[indice]
    com4 = Commune()
    for i in range(len(com4)):
            Dist.append(np.sqrt(np.power((LT[i] - lat_vil), 2) + np.power((LG[i] - lg_vil), 2)))
    zipped_lists = zip(Dist, com4)
    sorted_zip =  sorted(zipped_lists)
    #print(sorted_zip)
    sorted_list1 = [element for _, element in sorted_zip]
    return sorted_list1



def afficheCom():
    commune_clermont = Dist()
    commune_proche = []
    for i in range(30):
        commune_proche.append(commune_clermont[i])
    return commune_proche
commune_proche = afficheCom()
#print(commune_proche)
#print(len(commune_proche))

#Question 2
list_toutCom = Dist()
#print(list_toutCom[len(list_toutCom) - 1])

#Question 3
indice = ReturnName("Saint-Amant-Roche-Savine")
indice1 = ReturnName("Clermont-Ferrand")
lat_vil1 = LT[indice1]
lg_vil1 = LG[indice1]
lat_vil = LT[indice]
lg_vil = LG[indice]


distance = np.sqrt(np.power((lat_vil1 - lat_vil), 2) + np.power((lg_vil1 - lg_vil), 2))
distance = distance /  (1.56961 * pow(10, -4))
#print(distance)

#Question 4


def agglomeration(name):
    indice = ReturnName(name)
    lat_vil = LT[indice]
    lg_vil = LG[indice]
    rayon = (distance / 2) * 1.56961 * pow(10, -4)
    com3 = 0
    Dist = []
    for i in range(len(LT)):
        Dist.append(np.sqrt(np.power((LT[i] - lat_vil), 2) + np.power((LG[i] - lg_vil), 2)))
        if (Dist[i] < rayon and NOM[i] != "Clermont-Ferrand"):
            com3 += 1
    return com3

#print(agglomeration("Clermont-Ferrand"))

#print((agglomeration("Clermont-Ferrand") / len(Commune())) * 100)

