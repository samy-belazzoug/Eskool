"""Écrire un algorithme qui affiche les valeurs suivantes (en orange) dans le Terminal"""

#1

i = 30
while i < 37:
     #print(i)
     i += 1

#2

i = 37
while i > 31:
     #print(i)
     i -= 1

#3

i = 34
while i < 47:
     #print(i)
     i += 2

#4

i = 52
while i > 41:
     #print(i)
     i -= 2
     #1
#5

i = 1
j = 0
iteration = 0 
print(1)
while iteration < 6:
     if i > 1:
          print(i)
     if j > 34:
          break
     if j > 1:
          print(j)
     result = i
     i = i + j
     j += i
     iteration += 1

#6

i = 30
while i < 37:
     print(1/i)
     i += 1