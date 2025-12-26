#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 17:02:57 2025

@author: codewalker
"""

import numpy as np

"""
Esercizio 3
Si generi la seguente matrice scrivendo la minore quantità di codice possibile

0 1 2
3 4 5
6 7 8


Si ripeta l’esercizio generando una matrice 25 x 13 dello stesso tipo.

"""


mtx = np.arange(9).reshape(3, 3)
print('mtx', mtx)

print()
print("mtx type: ", mtx.dtype, mtx.dtype)

m1 = np.random.randint(0, 9, (25, 13))

print(m1, "\n")
