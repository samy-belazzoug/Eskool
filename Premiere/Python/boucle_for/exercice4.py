"""
1 : Écrire une fonction mot_de_passe_OK(mdp:str)->bool qui :

    reçoit en entrée une chaîne/string mdp représentant un mot de passe
    renvoie en sortie :
        True si le mot de passe contient au minimum 

        8 caractères
        False sinon

2 : Modifier l'algorithme précédent afin que la fonction mot_de_passe_OK(mdp:str)->bool renvoie :

    True lorsque:
        le mot de passe contient au minimum 8 caractères (ET)
        le mot de passe contient au minimum 1 chiffre
    False sinon

3 : Modifier l'algorithme précédent afin que la fonction mot_de_passe_OK(mdp:str)->bool renvoie :

    True lorsque:
        le mot de passe contient au minimum 8 caractères (ET)
        le mot de passe contient au minimum 1 majuscule
        le mot de passe contient au minimum 1 chiffre
False sinon
"""

#1
def mot_de_passe_OK(mdp:str)->bool:
    return len(mdp) >= 8

#2
def mot_de_passe_OK_evo(mdp:str)->bool:
    valide = False
    if len(mdp) >= 8:
        for i in mdp:
            if i in "0123456789":
                valide = True
            else:
                pass
    else:
        valide = False
    return valide

#3
def mot_de_passe_OK_evo2(mdp:str)->bool:
    nb_valide = False
    maj_valide = False
    if len(mdp) >= 8:
        for i in mdp:
            if i in "0123456789":
                nb_valide = True
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                maj_valide = True
            else:
                pass
        return maj_valide == True and nb_valide == True
    else:
        return False