"""Créer un script Python qui demande en entrée un nombre (flottant) x et qui affiche en sortie le signe de x :"
-Si x<0, Alors afficher "Strictement Négatif"
-Si x=0, Alors afficher "Nul"
-Si x>0, Alors afficher "Strictement Positif"
"""

def signe(x:float):
    if x < 0:
        return "Strictement Négatif"
    elif x == 0:
        return "Nul"
    else:
        return "Strictement positif"

print(signe(-1))
print(signe(0))
print(signe(3))