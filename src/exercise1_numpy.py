#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 10:58:58 2025

@author: codewalker
"""

"""
Esercizio #1

Definire una matrice 3x4, poi:

    Stampare la prima riga della matrice;

    Stampare la seconda colonna della matrice;

    Sommare la prima e l’ultima colonna della matrice;

    Sommare gli elementi lungo la diagonale principale;

    Stampare il numero di elementi della matrice.
"""

import numpy as np


M = np.array([[3, 4, 1, 5],
     [9, 2, 0, 1],
     [9, -6, 8, 4]])

print("M\n", M)
print()

print("M dtype: ", M.dtype)
print("M shape: ", M.shape)

#stampa della prima riga della matrice
print('prima riga della matrice M:   ->', M[0])
print()
#print(M[0][:])      modo alternativo di stampare la prima riga della matrice


#stampa della seconda colonna della matrice
print('seconda colonna della matrice M:   ->', M[:, 1])
print()


#somma della prima e dell'ultima colonna della matrice
print("somma della prima e dell'ultima colonna della matrice: ", (M[:,0] + M[:,-1]))
print()

#somma dei valori della prima e dell'ultima colonna della matrice
def sum(s):
    for x in M[:, 0]:
        s = s + x
    for x in M[:,-1]:
        s = s + x 
    return s

somma = 0

print("Somma degli elementi di colonna I e len(M)-1 : ", sum(somma))
print()


#sommare gli elementi della diagonale principale
mat = M.copy()
mat.resize(3,3)
print(mat)
print()

def sommadiag(mtx, s):
    for i in range(mtx.shape[0]):
        s = s + mtx[i][i]
    return s


print("sommare gli elementi della diag principale: ", sommadiag(mat, somma), "\n")


#Stampare il numero di elementi della matrice.
print('#elemnti M: ', len(M[0]) * len(M.T[0]))

