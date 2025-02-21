from math import sqrt
"""Résoudre une équation du second degré"""

def second_degre(a,b,c):
    delta = b**2-(4*a*c)
    if delta > 0:
        print("Delta > 0, il existe 2 solutions :")
        x1 = (-b-sqrt(delta))/2*a
        x2 = (-b + sqrt(delta))/2*a
        return x1,x2
    if delta == 0:
        print("Delta = 0, il existe une solution :")
        x0 = -b/2*a
        return x0
    if delta < 0:
        return "Delta < 0, il n'existe pas de solution réelle."

print(second_degre(3,9,1))
print(second_degre(1,9,5))