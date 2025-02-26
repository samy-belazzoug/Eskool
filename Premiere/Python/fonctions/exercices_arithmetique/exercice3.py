"""
1 : Écrire une fonction div_par(a:int,b:int)->bool qui teste la divisibilité de l'entier a par l'entier b, autrement dit:

    Si a est divisible par b, alors la fonction renvoie True
    sinon, elle renvoie False

2 : Écrire une fonction diviseur(a:int,b:int)->bool qui teste si l'entier a divise l'entier b, c'est-à-dire que b est un multiple de a, 
(on pourra, si le souhaite, utiliser la fonction de la question precédente div_par(a,b))

3 : En déduire une fonction diviseurs(n:int)->list qui accepte en entrée un entier n, et qui renvoie en sortie la liste de tous les entiers p qui sont des diviseurs de n

4 : Écrire une fonction sigma(n) qui accepte en entrée un entier n, et qui renvoie en sortie la somme de tous les diviseurs de n

5 : Écrire une fonction diviseurs_stricts(n:int)->list qui accepte en entrée un argument entier n, et qui renvoie en sortie la liste de tous les diviseurs stricts de n

(Un diviseur strict d'un entier n est un diviseur de n qui soit différent de 1 et de n.)
"""

#1

def div_par(a:int,b:int)->bool:
    return a % b == 0

#2

def diviseur(a:int,b:int)->bool:
    return div_par(b,a)

#3

def diviseurs(n:int)->list:
    diviseurs = []
    for i in range(1,n):
        if div_par(n,i):
            diviseurs.append(i)
        else:
            pass
    diviseurs.append(n)
    return diviseurs

print(diviseurs(169))

#4 

def sigma(n):
    somme = 0
    diviseur = diviseurs(n)
    for i in diviseur:
        somme += i
    return somme

#5 

def diviseurs_stricts(n:int)->list:
    diviseur = diviseurs(n)
    diviseur.pop(0)
    diviseur.pop(-1)
    return diviseur