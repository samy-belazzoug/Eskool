from exercice3 import sigma
"""
1 : Écrire une fonction parfait(n:int)->bool qui accepte en entrée un entier n, et qui renvoie en sortie:
    True si n est un nombre parfait
    False sinon

2 : Écrire une fonction parfaits(x:int)->list qui accepte en entrée un entier x et qui renvoie en sortie la liste de tous les nombres entiers parfaits inférieurs ou égaux à x
"""

#1

def parfait(n:int)->bool:
    return sigma(n) == 2*n

def parfaits(x:int)->list:
    l = []
    i = 1
    while i <= x:
        if parfait(i) == True:
            l.append(i)
        i += 1
    return l