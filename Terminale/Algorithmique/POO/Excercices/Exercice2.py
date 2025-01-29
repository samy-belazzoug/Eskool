"""Exercice 2. Héritage"""

class Personnage:
    # contructeur = méthode __init__ avec 2 arguments (sans compter self !) le nombre de vies et le nom du personnage
    def __init__(self, nbreDeVie, nomDuPerso):
        self.vie = nbreDeVie
        self.nom = nomDuPerso

    def setPointsVie(self,nombre:int):
        """Setter de la vie de la classe Personnage."""
        self.vie = nombre

    def affichePointVie(self):
        """Méthode qui affiche le nombre de vies du personnage."""
        print('Il reste '+str(self.vie)+' points de vie à '+self.nom)
    
    def perdVie(self):
        """Méthode qui fait perdre 1 point de vie au personnage qui a subi une attaque."""
        print(self.nom+' subit une attaque, il perd une vie')
        self.vie = self.vie-1

    def perdVies(self,nombre:int):
        """Méthode qui fait perdre un nombre donné de point de vie au personnage qui a subi une attaque."""
        print(self.nom+' subit une attaque, il perd des vies')
        self.vie -= nombre


# la classe Magicien hérite de la classe Personnage
class Magicien(Personnage):
    # dans def __init__ on retrouve nbreDeVie et nomDuPerso comme dans le def __init__ de la classe Personnage
    def __init__(self, nbreDeVie, nomDuPerso, pointMagie):
        # la ligne suivante est très importante dans le cas d'héritage, il faut systématiquement faire ce genre d'appel :
        # classeparente.__init__(self,arg1,arg2.....) pour hériter de tous les attributs et méthodes de la classe Personnage
        Personnage.__init__(self, nbreDeVie, nomDuPerso)
        # le seul nouvel attribut est self.magie, tous les autres sont hérités de la classe Personnage
        self.magie = pointMagie
    # une méthode uniquement disponible pour les instances de magiciens
    def faireMagie(self):
        print (self.nom+' fait de la magie')
        self.magie = self.magie - 1
        print('Il reste '+str(self.magie)+' points de magie à '+self.nom+'.')
    
    def creeVie(self):
        """Méthdode qui ajoute 1 point de vie au personnage."""
        print(self.nom+" a gagné une vie")
        self.vie += 1
    
    def creeVies(self,nombre:int):
        """Méthdode qui ajoute un nombre donné de points de vie au personnage."""
        print(self.nom+" a gagné des vies")
        self.vie += nombre

class Archer(Personnage):
    def __init__(self, nbreDeVie, nomDuPerso,nbArcs:int=1,nbFleches:int=10):
        Personnage.__init__(self,nbreDeVie,nomDuPerso)
        self.__nbArcs = nbArcs
        self.__nbFleches = nbFleches

    def get_arcs(self):
        print(self.__nbArcs)
    
    def get_fleches(self):
        print(self.__nbFleches)

    def set_arcs(self,valeur:int):
        self.__nbArcs = valeur
    
    def set_fleches(self,valeur:int):
        self.__nbFleches = valeur

    def tirerFleche(self):
        self.__nbFleches -= 1
        print(self.nom+' a tirer une flèche...')
    
    def __repr__(self):    
        return f"Voici le seul est unique archer {self.nom} !"

    # les autres méthodes des instances de magicien sont héritées de la classe personnage


if __name__ == "__main__":
    # on crée une instance de Magicien
    gandalf = Magicien(20,'Gandalf',15)
    # applique la méthode affichePointVie à gandalf, cette méthode est héritée de la classe personnage
    gandalf.affichePointVie()
    # applique la méthode faireMagie à gandalf, cette méthode est uniquement applicable aux instances de la classe magicien
    gandalf.faireMagie()

    merlin = Magicien(30,"Merlin l'enchanteur",17)
    merlin.affichePointVie()
    merlin.perdVie()

    greenArrow = Archer(20,"GreenArrow",1,10)
    greenArrow.setPointsVie(30)
    greenArrow.affichePointVie()
    greenArrow.tirerFleche()
    print(greenArrow)
    greenArrow.affichePointVie()
    greenArrow.perdVies(6)