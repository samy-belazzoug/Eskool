"""
Soit nom_fichier(filename:str)->None une fonction qui reçoit en entrée une variable filename contenant le nom d'un fichier. Assertions demandées :

filename doit être le nom d'un fichier finissant par ".txt"
filename doit contenir au moins 4 caractères en plus de l'extension ".txt"
filename doit contenir au moins 2 chiffres
"""

def nom_fichier(filename:str)->None:
    assert filename[-4:] == ".txt", "L'extension du fichier doit être .txt"
    assert len(filename) >= 8, "Le nom du fichier doit contenir au moins 4 caractères."
    numcount = 0
    for i in filename:
        if i in "1234567890":
            numcount += 1
    assert numcount >= 2, "Le nom du fichier doit contenir au moins 2 chiffres"