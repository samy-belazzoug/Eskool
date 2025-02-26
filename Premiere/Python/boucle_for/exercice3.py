"""
1 : On se donne une chaîne de caractères s="bonjour maman il fait beau aujourd'hui" Écrire un algorithme qui compte le nombre de caractères "a" dans la chaîne s

2 : Modifier l'algorithme précédent de sorte qu'on définisse une fonction compte(c:str,s:str)->int telle que:
    cette fonction recoive en entrée deux variables : un caractère c et une chaîne s
    qui renvoie en sortie le nombre de caractères c inclus dans la chaîne s

3 : Ecrire une fonction voyelles(s:str)->int qui :
    reçoit en entrée une chaîne de caractères s
    renvoie en sortie le nombre de voyelles incluses dans s
"""

#1

s="bonjour maman il fait beau aujourd'hui"
count = 0
for i in s:
    if i == "a":
        count += 1

#2

def compte(c:str,s:str)->int:
    count = 0
    for i in s:
        if i == c:
            count += 1
    return count

#3

def voyelles(s:str)->int:
    count = 0
    for i in s:
        if i in "aeiouy":
            count += 1
    return count