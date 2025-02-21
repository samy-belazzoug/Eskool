"""Créer un script Python qui demande en entrée un nombre entier x, et qui affiche en sortie, si ce nombre est pair, ou pas (impair)"""

def pair(x:int)->bool:
    return x % 2 == 0

print(pair(5))
print(pair(26))