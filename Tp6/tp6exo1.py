
import sympy as sm
import numpy as np
import matplotlib.pyplot as plt


co = []
cmi = []
cc = []
dt = []

with open("C:/eyosias/PythonExo/Tp6/cac40.csv" , encoding = "utf - 8") as f:
    for ligne in f:
        l = ligne.replace(",", ".")
        donnees = l.split(";")
        co.append(float(donnees[2]))
        cc.append(float(donnees[5]))
        cmi.append(float(donnees[4]))
        dt.append(donnees[1])



min = co[0]
index = 0
for i in range(1, len(co)):
    if (co[i] < min):
        min = co[i]
        index = i

print(len(co))


print(co[index])
print(dt[index])

#question 3
Acc = []

for i in range(len(cc)):
    Acc.append(co[i] - cc[i])

plt.plot(Acc)
#plt.show()

#on ne peut pas savoir si le graphe permet de dire si il y a plus un accroissement negatif que positif.

plt.figure()

neg = 0
pos = 0
somme = 0
for i in range(len(Acc)):
    if (Acc[i] > 0):
        pos += 1
    if (Acc[i] < 0):
        neg += 1
    somme += Acc[i]
print("Accroisement negatif, ", neg)
print("Accroissement positif, ", pos)


plt.hist(neg, color='b', label='Acc Negatif')
plt.hist(pos, color='r', label='Acc Pos')
plt.legend()
plt.show()

# il y a plus de jour avec un accroissement negatif


#Qestion 4

print("il a un gain de 3560.899999999993 durant cette periode")


# Meme si on un gain et que on avait un jours d'accroissement negatif superieur a celle de l'accroissement positf le resultat montre que le taux n'influence pas vraiment le gain ou la perte.