#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 15:56:08 2025

@author: codewalker
"""

import numpy as np


mat = np.array([[2,3], [10, 4], [3, 5], [12, 9]])

print(mat, '\n')


#lista built-in python

l = [[1, 2], [14, 23], [7, 9], [5, 3]]
m = []

m = [8, 4, 2, 1, 5, 2]

print(m, "\n")

print()
print(l[2:3:2], "\n")
print(m[1:6:2])
print()



mylist1 = [] # Creates an empty list
print("mylist1:   ->", mylist1)
mylist2 = [10, 23]
print("mylist2:   ->", mylist2)
mylist3 = [x * x for x in mylist2]
print("mylist3   ->", mylist3)

# mylist3 and mylist4 point to the same list
mylist3 = []
mylist4 = mylist3

print()
print("len di l: ", len(l), "\n")



#indicizzazione e slicing logici

"""
domanda 7: Si considerino i due array a=np.array([1,2,3]) e b=np.array([5,2,4]).
Si utilizzi l’indicizzazione logica per estrarre i numeri in a che si trovano 
in posizioni contenenti valori pari in b
"""

a = np.array([1, 2, 3, 9, 10, 85])
b = np.array([5, 2, 4, 7, 12, 99])

try:
    print(a[b%2==0])  #soluzione alla domanda 7
except:
    print("len(Arr1) != len(Arr2)\n")


print("\n\n")
M = np.random.randint(1, 20, (3, 3), dtype='int')
print(M, '\n')

print(M.T) #matrice trasposta di M, M^T


"""
Ciò avviene in quanto numpy confronta le dimensioni dei due operandi (e
) e adatta l’operando con shape più piccola a quello con shape più grande,
replicandone gli elementi lungo la dimensione unitaria (la prima). Il
broadcasting in pratica generalizza le operazioni tra scalari e vettori/matrici

"""