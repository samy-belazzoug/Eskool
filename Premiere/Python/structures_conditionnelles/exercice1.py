"""Créer un script Python qui demande en entrée un nombre (flottant) x et qui affiche en sortie le signe de x :"
-Si x<0, Alors afficher "Strictement Négatif"
-Si x=0, Alors afficher "Nul"
-Si x>0, Alors afficher "Strictement Positif"
"""

x = float(input("Entrez un nombre flottant : "))
if x < 0:
    print("Strictement Négatif")
elif x == 0:
    print("Nul")
else:
    print("Strictement positif")
