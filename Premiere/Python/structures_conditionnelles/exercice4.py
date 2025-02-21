from math import sqrt
"""Résoudre une équation du second degré"""

a = 3 
b = 5
c = 2

delta = b**2-(4*a*c)
if delta > 0:
    print("Delta > 0, il existe 2 solutions :")
    x1 = (-b-sqrt(delta))/2*a
    x2 = (-b + sqrt(delta))/2*a
    print("S :",x1,x2)
if delta == 0:
    print("Delta = 0, il existe une solution :")
    x0 = -b/2*a
    print("S :",x0)
if delta < 0:
    print("Delta < 0, il n'existe pas de solution réelle.")
