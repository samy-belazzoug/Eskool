class Temps:
    """Initialise Temps (entre 1 à 4), et Valeur (entre 1 à 13)"""
    def __init__(self, h, m, s):
        self.heures = h
        self.minutes = m
        self.secondes = s

    def ajouterMinutes(self, mins):
        """incrémente les minutes de la valeur mins passée en paramètre"""
        self.minutes = self.minutes + mins
        while self.minutes > 59 :
            self.heures += 1
            self.minutes = self.minutes - 60                

    def ajouterSecondes(self, secs):
        """incrémente les secondes de la valeur secondes passée en paramètre"""
        self.secondes = self.secondes + secs
        while self.secondes > 59 :
            self.minutes += 1
            self.secondes = self.secondes - 60

    def __str__(self):
        """renvoie une chaine de caractères sous la forme hh : mm : ss"""
        return str(self.heures)+" : "+str(self.minutes)+" : "+str(self.secondes)

    def enSecondes(self):
        """Convertie un temps en heures/minutes/secondes en secondes"""
        return (self.heures*3600) + (self.minutes*60) + self.secondes

    def estplusPetit (self, tps) :
        """Compare deux temps entre eux. Renvoie True si l'objet est plus petit que l'objet tps passé en paramètre"""
        return tps.enSecondes() > self.enSecondes()

t1 = Temps(6,10,5)
t2 = Temps(5,10,3)
t1.ajouterSecondes(20)
t1.enSecondes()
print(t1)
print(t1.estplusPetit(t2))