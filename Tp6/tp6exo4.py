import sympy as sm
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

Lin  = []
nbc =  [["A", 0], ["B", 0], ["C", 0],  ["D", 0],  ["E", 0],  ["F", 0],  ["G", 0], ["H", 0],  ["I", 0], ["J", 0], ["K", 0],  ["L", 0],  ["M", 0],  ["N", 0],  ["O", 0],  ["P", 0],  ["Q", 0],  ["R", 0],  ["S", 0],  ["T", 0],  ["U", 0],  ["V", 0],  ["W", 0],  ["X", 0],  ["Y", 0],  ["Z", 0]]


with open("C:/eyosias/PythonExo/Tp6/sherlock.txt" , encoding = "utf - 8") as f:
    for ligne in f:
        Lin.append(ligne.upper())

def ReturnIndice(lettre):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(alph)):
        if (lettre == alph[i]):
            return i


def Ajoute():
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(Lin)):
        for j in range(len(Lin[i])):
            if (Lin[i][j] in alph):
                nbc[ReturnIndice(Lin[i][j])][1] += 1
Ajoute()
print(nbc, '\n')
nbc = sorted(nbc, key=itemgetter(1))
print(nbc)


def Frequ(nbcL, nbcT):
    return (nbcL / nbcT) * 100

def S(nbc):
    somme = 0
    for i in range(len(nbc)):
            somme += nbc[i][1]
    return somme

def calcFr():
    sommeT = S(nbc)
    GPL = 26
    index = np.arange(GPL)
    largeur = 0.35
    freqLi = []
    liAl = []
    for i in range(len(nbc)):
        freqLi.append(Frequ(nbc[i][1], sommeT))
        liAl.append(nbc[i][0])
    return freqLi



freqli = calcFr()
liAl = []
GPL = 10
index = np.arange(GPL)
largeur = 0.5
freqLi2 = []
for i in range(len(nbc) - 10, len(nbc)):
    liAl.append(nbc[i][0]) # contient les caratere de l'alphabet des 10 dernier plus grand
    freqLi2.append(freqli[i])   #contient frequence des 10 dernier plus grand
plt.bar(index, freqLi2, largeur, color='b', label='Frequence en %')
plt.xticks(index, liAl)
plt.legend()
plt.show()