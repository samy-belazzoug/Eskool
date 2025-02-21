from random import randint
"""Dans cet exercice, on poura importer la fonction randint du module random de la bibliothèque standard de Python.
Une mouche est se déplace aléatoirement sur un axe à une dimension, en effectuant des sauts aléatoires (d'une longueur aléatoire, entre 0 et 10 pas, 
vers la gauche et/ou vers la droite, aléatoirement). Initialement, la mouche se situe sur la position 0 de l'axe horizontal.
Écrire une fonction marche() qui simule le déplacement de la mouche durant 5 sauts. La fonction marche() est telle que :

-elle ne prend aucun argument en entrée
-elle affiche la nouvelle position de la mouche (un entier) après chacun des 5 sauts
-elle renvoie en sortie le nombre entier vérifiant la position finale (après 5 sauts)
"""

def marche():
    x = 0
    saut = 0
    while not saut == 5:
        longueur = randint(-10,10) #Si on va a gauche dans un axe horizontal, on derive vers les nombres négatifs
        x = longueur
        print(x)
        saut += 1
    return f"Position finale : {x}"

print(marche())