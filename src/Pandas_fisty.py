#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 19 13:35:29 2025

@author: codewalker
"""

import pandas as pd
import numpy as np

#pandas implementa le strutture dati Serie e Dataframe


inflation = pd.Series((3.0, 1.3, 2.0, 1.6, 2.5, 7.5, 2.2, 5.4, 4.1, -2.7, -1.2,
                       1.4))

print(inflation, "\n")

i = 0
while i < (int)(len(inflation)/2):
    print(inflation.values[i])
    i += 1

print("\n\n")
print(inflation.values[-2], "\n") #stampa il penultimo elemento della serie

print()
inflation.index.name = "stocks"
inflation.name = "%"

print(inflation)


"""nel Dataframe (generica tabella) le righe e le colonne sono identificate con
etichette anczichè con indici interi. Un dataframe può essere visto come una
tabella SQL o un foglio Excel, formati quindi da righe e colonne. """

#A differenza di un array Numpy un Dataframe può gestire dati eterogenei

#Con un Dataframe possiamo gestire pure tipi di dati non numerici (unstructured
#data).

#data è un dizionario. Così sto stampando gli elementi del dizionario come insiemi di tuple 
fruits = {
        "Basket":["Pera", "Arancia", "Fragola"],
        "Quantita": [9, 8, 6]
    }

print('\n')
print(fruits.items())

df = pd.DataFrame(fruits) #carica i dati in un dataframe
print("\n")
print(df)


df_recipes = pd.read_csv('gz_recipe.csv') #legge file CSV, qui è nella stessa DIR

print("\n\n")
print(df_recipes, "\n")


seasons = ['Autunno', 'Inverno', 'Primavera']
df_season = pd.DataFrame(seasons)
print(df_season, "\n")

#concatenazione di più dataframe
print("\n")
M = np.random.randint(0,9,(3, 3))
print(M)
print("\n")

df2 = pd.DataFrame(M)


df_combine = pd.concat([df, df2])
print(df_combine.fillna(0))  #fillna(0) mette 0 a posto di NaN
print("\n")


df_season_fruits = pd.concat([df, df_season])
print(df_season_fruits, '\n')

print(df.describe())
