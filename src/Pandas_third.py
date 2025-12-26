#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 15:40:29 2025

@author: codewalker
"""

import pandas as pd
import numpy as np

# Pandas  Dataframe

df = pd.DataFrame(np.random.randint(-5, 10, (3, 5)), columns=['A', 'B', 'C', 'D', 'E'])
print(df, "\n")


print("lunghezza del dataframe df, (#osservazioni): ", len(df), "\nshape di df: ", df.shape)
print()

"""
un DataFrame è in fondo una collezione di Series, ognuna rappresentante una 
colonna) che ha come nome il nome della colonna considerata

"""
dfB = df['B']
print(dfB)
print("type dfB: ", type(dfB), "\n")
print()



dfCD = df[['C', 'D']]
print(dfCD, "\n")
print("type dfCD: ", type(dfCD), "\n")

print(len(dfCD), '\n')


#se voglio sapere la media dei valori di ogni colonna del dataframe faccio:
print(df.mean())
print()
#se invece volessi le statistiche per ogni colonna posso fare:
print(df.describe(), "\n")

#N.B. è possibile applicare il metodo apply() a colonne del dataframe perchè esse
#sono delle Series, ogni colonna è una Series
df['A']=df['A'].apply(lambda x: "Numero: "+str(x))
print(df, "\n")

#ordinamento
df = df.sort_values('C') #ordina i valori della colonna C
print(df, "\n")


"""
Domanda 7: Si utilizzi l’indicizzazione logica per selezionare le righe in cui
la somma dei valori di ‘C’ ed ‘A’ sia maggiore di 1.

"""
d = pd.DataFrame({'A':[1,2,3,4],'B':[3,2,6,7],'C':[0,2,-1,12]})
print(d, "\n")
print(d[(d['A'] + d['C']) > 1])
print()


"""
Domanda 8: Si inserisca nel Dataframe dato una nuova colonna 'D' che contenga
il valore 1 in tutte le righe in cui il valore di B è superiore al valore di C.
Hint: si usi “astype(int)” per trasformare i booleani in interi.
"""

e8df = pd.DataFrame({'A': [1,2,3,4], 'B': [3,2,6,7], 'C': [0, 2, -1, 12]})

e8df['D'] = (e8df['B'] > e8df['C']).fillna(1).astype(int)
print(e8df, '\n')


"""
Domanda 9: Dato il seguente Dataframe si trasformi la colonna “B” in modo che i
nuovi valori siano:

    uguali a zero se precedentemente pari;

    uguali a -1 se precedentemente dispari.

"""
#credo che devo usare il metodo apply
e9df = pd.DataFrame({'A':[1,2,3,4],'B':[3,2,6,7],'C':[0,2,-1,12]})

print(e9df)
print()

def func():
    s = e9df['B']
    for i in range(0, len(e9df['B'])):
        if s[i] % 2 == 0:
            s[i] = 0
        else: s[i] = -1

func()
print(e9df, "\n")


