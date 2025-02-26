import matplotlib.pyplot as plt
import numpy as np
""""Nombre Premier" Un nombre est dit premier s'il est seulement divisible par et par lui-même.

1 : Écrire une fonction est_premier(n:int)->bool qui prend en entrée un argument n:int, et qui renvoie en sortie :

    True si n est un nombre premier,
    False, sinon

2 : En déduire une deuxième fonction premiers(x:int)->list qui accepte en entrée un argument x:int, et qui renvoie en sortie la liste de tous les nombres premiers 
inférieurs ou égaux à x
3 : Écrire une fonction qte_premiers(x:int)->int qui accepte en entrée un entier x et qui renvoie en sortie la quantité de nombres premiers inférieurs ou égaux à x

4 : Grâce au module matplotlib, tracer la courbe représentant la fonction qte_premiers :
On pourra commencer par créer, par compréhension de liste, les deux listes suivantes:
x = [50, 100, 150, ..., 1000]
y = [qte_premiers(50), qte_premiers(100), qte_premiers(150), ..., qte_premiers(1000),]
"""

#1

def est_premier(n:int)->bool:
    lower = 0
    checking = 0
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]:
        if n <= i:
            break
        else:
            lower += 1
            if n%i != 0:
                checking += 1
    if checking == lower:
        return True
    else:
        return False

print(est_premier(169))

#2

def premiers(x:int)->list:
    i = 13
    l = []
    if x >= 13:
        l = [2,3,5,7,11]
    while i <= x:
        if est_premier(i) == True:
            l.append(i)
        i += 1
    return l
i = 1000
print(premiers(i))

#3

def qte_premiers(x:int)->int:
    s = premiers(x)
    return len(s)

print(qte_premiers(i))

#4

x = np.array([50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000])
y = np.array([qte_premiers(i) for i in x])

plt.plot(x, y,'o')
plt.show()