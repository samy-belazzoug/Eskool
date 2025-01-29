"""Exercice 1. Encapsulation  + Accesseurs / Mutateurs"""

class CompteBancaire:
    def __init__(self,numeroCompte:str="112233",nom:str="DUPOND",solde:float=0):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.__solde = solde
    
    def getSolde(self):
        return self.__solde

    def setSolde(self,valeur:float):
        self.__solde = valeur

    def depot(self,montant:float):
        self.__solde += montant
        print(f"Vous avez dépôser {montant}€.\nVotre solde est de {self.__solde}€.\n")
    
    def retrait(self,montant:float):
        self.__solde -= montant
        print(f"Vous avez retirer {montant}€.\nVotre solde est de {self.__solde}€.\n")

    def agios(self,p:float):
        if self.__solde < 0:
            self.__solde *= p
    
    def infos(self):
        print(f"Numéro de compte : {self.numeroCompte}\nTitularire du compte : {self.nom}\nSolde actuel : {self.__solde}€")

if __name__ == "__main__":
    dupond = CompteBancaire()
    dupond.depot(40)
    dupond.depot(35)
    dupond.retrait(26.5)
    dupond.infos()