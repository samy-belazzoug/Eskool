from random import randint
"""Dans cet exercice, on poura importer la fonction randint du module random de la bibliothèque standard de Python.
Écrire une fonction alea5(a,b) telle que :

-elle prend en entrée deux nombres entiers a et b
-et qui renvoie en sortie une liste de 5 nombres entiers aléatoires entre a et b
"""

def alea5(a:int,b:int):
    return [randint(a,b),randint(a,b),randint(a,b),randint(a,b),randint(a,b)]