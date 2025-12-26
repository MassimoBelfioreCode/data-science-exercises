#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 23:59:19 2025

@author: codewalker
"""

import pandas as pd
import numpy as np


#Pandas  Series

sr1 = pd.Series([2, 3, 5, 5, 5, 1, 9], name="pieces")
print(sr1)
print()


np.random.seed(123)

labels = ['Blue', 'Green', 'Red', 'Yellow', 'Brown', 'Orange', 'Pink', 'Purple']
print("labels length: ", len(labels))

sr2 = pd.Series(np.random.randint(1, 10, 8), index = labels, dtype="int64", name="color-code")
print(sr2, "\n")



#posso creare serie di dati tramite un dizionario

dict = {'y' : 50.5, 'x' : 20.4, 'z' : 8.6}
print(pd.Series(dict), "\n")


print()
print(sr2['Pink']) #indicizzazione tramite label, ammessa anche sr2[3], restituisce il val

#è possibile modificare i valori di una serie perchè è una struttura dati Pandas mutabile


print()
print()
s=pd.Series([1,2,3,4,6])
print(s[s%2])
#perchè da questo output? Praticamente il risultato è una nuova serie che ha per
#indici i risultati dei valori di s modulo 2 e per valori invece?


#tipi di dato

sd = pd.Series(np.array([3.2, 3, np.nan, 1, 6, 'b']))
print()
print()
print(sd.astype(str))

print()
sd2 = pd.Series(['r', 'bb', '21'])
print(sd2)

print()
print(sd2.apply(str.upper), "\n")
#il metodo apply prende una funzione come argomento e la applica a tutti gli elementi della serie


sd2[3] = 'r'
print(sd2, "\n")

sd2 = sd2.replace({'r':'v'})
print(sd2)
print()

"""
Domanda 5: Come si può ottenere un array di Numpy da un Series in modo che
le due entità siano indipendenti?  Risposta: con il metodo copy()
"""
a = sd.values.copy()
print(sd, "\n")
a[0]=-1
print(sd, "\n")
print(a, '\n')

