"""Créer un script Python qui :

-crée une variable phrase="une phrase qui vous plaît" (on dit "coder en dur")
-demande en entrée une (sous-)chaîne de caractères
-affiche en sortie, si OUI ou NON la (sous-)chaîne appartient à la phrase initiale.
"""

def souschaine(chaine:str)->bool:
    phrase = "Une phrase s'il vous plait"
    return chaine in phrase

print(souschaine("phrase"))
print(souschaine("vousplait"))