

import sympy as sm
import numpy as np
import matplotlib.pyplot as plt

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
            #NUI.append(float(donnees[0]))
            NOM.append(donnees[1])
            Al.append(float(donnees[2]))
            #CP.append(float(donnees[3]))
            LG.append(float(donnees[4]))
            LT.append(float(donnees[5]))
            POP.append(float(donnees[6]))
            SUF.append(float(donnees[7]))


max = LT[0]
indice = 0
for i in range(len(LT)):
    if (LT[i] > max):
        max = LT[i]
        indice = i

print(max, '\n', indice)




#Question 2
LtSorted = sorted(LT)
MedIndex = len(LT) // 2
Lat_med = LtSorted[MedIndex]
print("Lat_med =",Lat_med)

comN = 0
comS = 0
for i in range(len(LT)):
    if (LT[i] > Lat_med):
        comN += 1
    elif (LT[i] < Lat_med):
        comS += 1
print("Commune audessus de la moyenne:", comN)
print("Commune endessus de la moyenne:", comS)


#Question 2 partie 2
LtSorted = sorted(LG)
MedIndex = len(LG) // 2
Long_med = LtSorted[MedIndex]

print("Long_med =",Long_med)

#Question 3

def Dist():
    Dist = []
    indice = 0
    for i in range(len(LT)):
        Dist.append(np.sqrt(np.power((LT[i] - Lat_med), 2) + np.power((LG[i] - Long_med), 2)))
        if (i == 0):
            min = Dist[i]
            indice = i
        elif (Dist[i] < min):
            min = Dist[i]
            indice = i
    return indice

print("nom commune", NOM[Dist()])


#Qestion 4
listPop = []
def Visualise():
    for i in range(len(POP)):
        if (POP[i] >= 1000 and POP[i] <= 20000):
            listPop.append(POP[i])

Visualise()
plt.hist(listPop, bins =np.arange(999, 20001))
plt.show()
plt.figure()
#Question 5

com1 = []
com2_indice = []
def Visualise2():
    for i in range(len(POP)):
        if (POP[i] >= 100000):
           com1.append(POP[i])
           com2_indice.append(i)
           print(NOM[i])
    #plt.scatter(com2_indice, com1, color='r')
Visualise2()

x = np.arange(len(POP))
#plt.scatter(x, POP, color='b')
#Visualise2()
#plt.show()



#Question 6



def ReturnName(name):
    for i in range(len(NOM)):
        if (NOM[i] == name):
            return i


def agglomeration(name):
    indice = ReturnName(name)
    lat_vil = LT[indice]
    lg_vil = LG[indice]
    rayon = 20 * 1.56961 * pow(10, -4)
    com3 = 0
    Dist = []
    for i in range(len(LT)):
        Dist.append(np.sqrt(np.power((LT[i] - lat_vil), 2) + np.power((LG[i] - lg_vil), 2)))
        if (Dist[i] < rayon and NOM[i] != "Clermont-Ferrand"):
            com3 += 1
    return com3



print(agglomeration("Clermont-Ferrand"))

























