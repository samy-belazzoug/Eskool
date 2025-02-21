"""Créer un script Python qui :

-crée une variable phrase="une phrase qui vous plaît" (on dit "coder en dur")
-demande en entrée une (sous-)chaîne de caractères
-affiche en sortie, si OUI ou NON la (sous-)chaîne appartient à la phrase initiale.
"""

phrase = "Une phrase s'il vous plait"
souschaine = str(input("Entrez une sous-chaine : "))
print(souschaine in phrase)