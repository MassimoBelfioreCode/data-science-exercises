#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 17 17:40:37 2025

@author: codewalker
"""

#sottoarray in numpy

import numpy as np


x = np.array([[8, 4, 2], [4, 3, 1], [5, 5, 0]]) #sta in una parte di memoria, 3x3 arr
x2_sub = x[:2, :2].copy() #sottoarray 2x2

"""
    ↓  ↓
  [[8, 4, 2],
 → [4, 3, 1],
   [5, 5, 0]]

"""

print(x)
print('\n')
print(x2_sub)
print("\n")




x2_sub[1][1] = 18 #x e x2_sub vanno a riferirsi alla stessa area di memoria e quindi
                  #la modifica ad un array viene applicata ad entrambi, sia a quello
                  #principale che al sottoarray tranne se usiamo la copy()
print(x)
print('\n')
print(x2_sub)
print("\n")


"""per risolvere questo problema, visto che io volevo modificare soltanto il valore
di una cella del sottoarray e non di quello principale... posso fare la copia
utilizzando la funzione copy() al momento della definizione del sottoarray. Se
non avessi usato la copy() avrei avuto quindi questo problema della stessa area di
memoria e una modifica a un array veniva applicata anche all'altro. Posso constatarlo
togliendo la funzione copy() per rendermene conto"""

#adesso creo un altro sottoarray di x, senza fare la copia
x3_sub = x[:2][:2]
x3_sub[0][0] = 9

print(x)
print('\n')
print(x3_sub)
print("\n")

#come vedete la modifica si è applicata sia ad x che a x3 (sottoarray di x)

y = np.ones(4, dtype = "int16")
y2 = y.reshape((2,2))
#devono essere della stessa dimensione, 9 e 3x3 = 9 per esempio

print("y: ",y)
print()
print("y2:\n ", y2, "\n")

y2[1][0] = 97
#stessa cosa di prima, qui il reshape comunque non evita il fatto che si applica
#ad array e sottoarray la modifica
print("y: ",y , "\n")
print("y2: ", y2, "\n")

"""
       Numpy Array
      _____________
     |PyObject_HEAD|
     |_____________|     __
     |    data     |--->|  |
     |_____________|    |__|
     |  dimensions |    |  |
     |_____________|    |__|
     |   strides   |    |  |
     |_____________|    |__|
                        |  |
                        |__|
                        |  |
                        |__|
"""

z = np.arange(4)
print()
print(z)
print(abs(-5)) #visualizza il valore assoluto di -5 restituito dall funzione abs(v)

from Numpy_first import vec

avg = np.mean(vec)
print("vec avg: ", avg)
print("vec max: ", np.max(vec))

"""
numpy ci permette anche di sommare tra loro array con array di qualsiasi dimensione
ed il risultato sarà un nuovo array/matrice num righe x num colonne
"""

u = np.array([1, 2, 3, 4, 5])
print(np.count_nonzero(u < 6)) #5 elementi di u sono < 6


largearr = np.random.ranf(80)
print(largearr, "\n")


print()
np.random.seed(100)
print(np.random.rand(6))


x = np.array(([3, 2, 1], [0, 4, 2]))

x[1][2] = 7

print()
print(x[1:])
print(x[x>2])

u = np.resize(u, 3)
print(u[np.array([True,False,True])])
