#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 20:59:11 2025

@author: codewalker
"""

import pandas as pd
import numpy as np

df1 = pd.DataFrame({'X': [8, 2, 3, 1], 'Y': [7, 7, 4, 5], 'Z': [9, 2, 1, np.nan]})
print(df1, "\n")

df1.drop(3, inplace=True)  #rimuove la riga 3 persistentemente da df
print(df1, "\n")


df1 = df1.drop('Z', axis=1)
print(df1, "\n")


df2 = pd.DataFrame({'Name': ['Banana', 'Peach', 'Apple', 'Tomato', 'Lemon'],
                    'Color': ['Y', 'P', 'G', 'R','Y'], 'Unit': [100, 33, 150, 599, 40]})

print(df2, type(df2))
print()


print(df2.groupby('Color').count(), "\n")
print(df2.groupby('Color').describe().transpose(), "\n\n")

print("concatenazione di df1 con df2 per righe è:\n")
print(pd.concat([df1, df2]))
print()
print("concatenazione di df1 con df2 per colonne è:\n")
print(pd.concat([df1, df2], axis=1))

"""
Si può fare anche il Natural Join tra dataframe, un po' come nei DB, sulla base
di un attributo/variabile/colonna in comune, che si fa tramite il metodo merge in pandas.

si fa così pd.merge(dfA, dfB, on= 'colonna uguale') 

se questi hanno una colonna con nome uguale e stesso tipo si può fare il merge/NJ
"""
print()
print("merge di df1 e df4\n")
dati = np.random.randint(1, 10, (6, 2)) # matrice 6x2
df4 = pd.DataFrame(dati, columns=["X", 'W'])

print(pd.merge(df1, df4, on = 'X'), '\n')

#esiste anche il metodo join in pandas ma fa un'altra cosa rispetto al merge, e
#usa per farlo gli indici(etichette di riga) in comune dei due dataframe da joinare



"""
Domanda 10: Considerando il DataFrame precedentemente creato, si usi groupby per
ottenere la somma dei redditi dei dipendenti di una data compagnia.
"""

print()

df=pd.DataFrame({'income':[10000,11000,9000,3000,1000,5000,7000,2000,7000,12000,8000],
                 'age':[32,32,45,35,28,18,27,45,39,33,32],
                 'sex':['M','F','M','M','M','F','F','M','M','F','F'],
                 'company':['CDX','FLZ','PTX','CDX','PTX','CDX','FLZ','CDX','FLZ','PTX','FLZ']},
                index= ['e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10', 'e11'])


print(df, "\n\n")
print('soluzione domanda dieci:\n')
print(df.groupby('company')['income'].sum(), '\n') #soluzione


"""
Domdanda 11: Si costruisca una crosstab che, per ogni compagnia, riporti il numero
di dipendenti di una data età.
"""
print("soluzione domanda undici\n")
print(pd.crosstab(df['age'], df['company']), '\n') #soluzione
