from math import sqrt
"""
Dans chacune des situations suivantes, dans chaque fonction considérée, écrire l'assertion demandée:

1 : On se donne la fonction racine_carre(x:float)->float qui calcule la racine carrée d'un nombre x. 
Assertion/Vérification demandée : x doit être positif (ou nul)

2 : On se donne la fonction inverse(x:float)->float qui calcule l'inverse d'un nombre x. 
Assertion/Vérification demandée : x doit être non nul

3 : On se donne la fonction divise_par_7(x:int)->int qui calcule la division par 7 d'un nombre x. 
Assertion/Vérification demandée : x doit être un multiple de 7

4 : On se donne la fonction divise_par(x:int,n:int)->int qui calcule la division par n d'un nombre x. 
Assertion/Vérification demandée : x doit être un multiple de n

5 : On se donne la fonction note(x:float)->None qui reçoit une note x, (et qui par la suite, sera par exemple amenée à la stocker dans une Base de Donnée). 
Assertion/Vérification demandée : x doit être comprise entre 0 et 20 inclus

6 : On se donne la fonction repartition(n:int)->bool qui vérifie si OUI (True) ou Non (False) le nombre n contient autant de 1 que de 2
"""

#1

def racine_carre(x:float)->float:
    assert x > 0, "On ne peut calculer la racine carré d'un nombre négatif."
    return sqrt(x)

#2

def inverse(x:float)->float:
    assert x != 0, "0 n'a pas d'inverse."
    return -x
#3

def divise_par_7(x:int)->int:
    assert x%7 == 0, "x doit être un multiple de 7"
    return x/7

#4

def divise_par_(x:int,n:int)->int:
    assert x%n == 0, "x doit être un multiple de n"
    return x/n

#5

def note(x:float)->None:
    assert 0 < x < 20, "x doit être compris entre 0 et 20"
    return

#6

def repartition(n:int)->bool:
    s = str(n)
    count1 = 0
    count2 = 0
    for i in s:
        if i == "1":
            count1 += 1
        if i == "2":
            count2 += 1
    return count1 == count2

print(repartition(111222))