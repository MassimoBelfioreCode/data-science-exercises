#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 19 19:16:32 2025

@author: codewalker
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.array([0, 8])
y = np.array([0, 10])
#un punto sarà p1(0,0) e l'altro punto sarà p2(8,10)

print("x:",x)
print()
print("y:",y)


plt.rcParams['figure.figsize'] = [6, 3]

plt.plot(x, y, '--+r', marker = '*', mfc = 'green', linestyle = "dashed")

plt.show()



w1 = np.array([0, 5, 30])
w2 = np.array([18, 24, 25])

plt.subplot(1, 2, 1)
plt.plot(w1)

plt.subplot(1, 2, 2)
plt.plot(w2)

plt.show()

w3 = np.array([14, 15, 2, 0])
w4 = np.array([20, 3, 9, 5])

plt.ylabel('car model sold')
plt.xlabel('year')
plt.title('My plot')
#vabeh è sbagliato ma è tanto per farlo

#plottiamo due linee differenti nel grafico
plt.plot(w3)
plt.plot(w4)
plt.legend(["w3", "w4"])

plt.show()


"""
    Creare la figura e le sottotrame:


   fig, axs = plt.subplots(nrows=2, ncols=2)  # Crea una griglia 2x2

fig è l'oggetto figura, mentre axs è un array di oggetti asse (subplot). 

    Accedere alle sottotrame: 

Si può accedere a ciascun subplot utilizzando gli indici dell'array axs.
Ad esempio, axs[0, 0] si riferisce al subplot in alto a sinistra, axs[1, 0] al
subplot in basso a sinistra, e così via.

"""