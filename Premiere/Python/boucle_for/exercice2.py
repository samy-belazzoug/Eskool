"""Suites de valeurs
1 : Écrire un algorithme qui calcule la somme S = 1-1000
2 : Écrire un algorithme qui calcule la somme S = 1**2-1000**2
3 : Écrire un algorithme qui calcule la somme S = 1/1-1/1000
4 : crire un algorithme qui calcule la somme S = 1/1**2-1/1000**2
"""

#1
s = 0
for i in range(1,1001):
    s += i

#2
s = 0
for i in range(1,1001):
    s += i**2

#3
s = 0
for i in range(1,1001):
    s += (1/i) 

s = 0
for i in range(1,1001):
    s += (1/i**2)

print(s)