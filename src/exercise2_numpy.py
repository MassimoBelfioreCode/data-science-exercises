#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 16:11:08 2025

@author: codewalker
"""

"""
esercizio #2

Si generi un array di numeri compresi tra 2 e 4 e si calcoli la somma degli
elementi i cui quadrati hanno un valore maggiore di 8.

"""

import numpy as np

arr = np.random.randint(2, 4, (1, 100))

print(arr)
print()

#si calcoli la somma degli elementi i cui quadrati hanno un valore maggiore di 8
print("somma: ", arr[(arr**2) > 8].sum())


