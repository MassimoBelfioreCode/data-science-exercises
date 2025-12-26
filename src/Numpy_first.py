#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 15 23:38:16 2025

@author: codewalker

Numpy è una libreria di Python che permette creare e lavorare con array
multidimensionali e matrici in python
"""
from __future__ import print_function
import numpy as np


#modo semplice per creare una matrice in Python
M = np.array([[4, 1, 0, 5],
              [0, 0, 2, 3],
              [7, 1, 0, 4]])

print(M[0][2], "\n")
print(M[1][:], "\n")
print(M[:][:], "\n")  #equivalent of the instruction under
print(M, "\n")


A = np.array([0.2, 1, 4, 2], dtype = "int32")
print(A, "\n")

#np.random.seed(0) # seed for reproducibility (dà sempre gli stessi valori ad ogni run)

print(np.random.random((2, 2)))

print('\n')
arr = np.array([0.3, 0.6, 0.9, 1.2, 1.5, 1.8], dtype = 'float32')
print(arr, "\n")


p = 6
mtx = np.full((p, p), 0)
print("mtx =", mtx, "\n")


for i in range(0, p):
    for j in range(0, p):
        if i == j:
            mtx[i][j] = 1
        j = j + 1
    i += 1
print(mtx)

#questa ultima cosa fatta si può fare anche con la funzione eye() se passo dtype ="int"
print('\n')
print(np.eye(6), '\n\n')


bm = np.random.randint(0, 2, (4, 8))
print(bm)

#funzione che stampa il valore assocciato alle righe di 0 e 1 della matrice binaria
def f(bm):
    sum = 0
    for i in range(0,4):
        for k in range(0,8):
            if bm[i][k] == 1:
                sum += pow(2, 7-k)
        print("\nr"+(str(i)), sum)
        sum = 0
        

f(bm)


print()
x1 = np.random.randint(10, size=6)
print(x1)
print()
print(x1[-1])  #stampa l'ultimo elemento di x1
x3 = np.random.randint(-5, 5, size=(3, 4, 5)) #3x4x5 , Three-dimensional
print("\n",x3) #visualizza 3 matrici 4x5
x = np.arange(9).reshape((3, 3))
print("\n", x, "\n\n")


#reverse a list
vec = [1, 3, 8, 6, 5, 10]
print("Lista vec: ", vec)
vec = vec[::-1]
print("Lista vec invertita: ", vec)

print()

#splitting di array in sottoarray
# ....|...|......|....  → 3 split points = 3+1 sub arrays

arr_sub1, arr_sub2, arr_sub3 = np.split(arr, [2, 4])
print("arr_sub1:", arr_sub1, "arr_sub2:", arr_sub2, "arr_sub3", arr_sub3)

v =  np.array([1, 8, 3 , 8, 9, 6])
print(np.hsplit(v, [2, 4]))

print("\nM not sorted= ")
print(M)
print("\nM sorted=")
print(np.sort(M)) #ordinamento per riga della matrice di default

print("\n")
v.sort()  #ordinamento in loco(place)
print(v, "\n")

print(np.sort(M, axis= 0)) # ordina tutte le colonne di M, ordinamento per colonna
print("\n")
print(np.sort(M, axis = 1))#ordina tutte le righe di M, ordinamento per riga
print("\n")
print(M) #la matrice originale resta uguale


print()
print(np.empty(4)) 
"""restituisce dei valori che giù erano presenti in quelle locazioni quindi l'array
non è creato non inizializzato come dovrebbe essere in realtà"""

