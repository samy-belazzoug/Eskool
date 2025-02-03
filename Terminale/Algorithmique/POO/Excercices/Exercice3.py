"""Exercice 3. Classe chaîne étendue"""

class myString:
    def __init__(self,string:str=""):
        self.string = string

    def append(self,string):
        self.string += string

    def pop(self,i:int):
        if i > len(self.string):
            raise TypeError ("Index out of Range.")
        copy = ""
        for j in range(len(self.string)):
            if j != i:
                copy += self.string[j]
        self.string = copy
                
    def __repr__(self):
        return f"{self.string}"

if __name__ == "__main__":
    s1 = myString("Hello")
    s2 = myString("Bonjour")
    s1.append(" World !")
    s2.pop(2)
    print(s1)
    print(s2)