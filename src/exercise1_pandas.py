#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 11:51:26 2025

@author: codewalker
"""

import pandas as pd
import numpy as np


"""
Esercizio 1

Si carichi il dataset disponibile al seguente 
URL: https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv
in modo da utilizzare i valori della colonna “PassengerId” come indici e si applichino
le seguenti trasfromazioni:
    
        Si rimuovano le righe che contengono dei valori NaN;

        Si modifichi il DataFrame sostituendo nella colonna “Sex” ogni occorrenza di “male” con “M” e ogni occorrenza di “female” con “F”;

        Si inserisca una nuova colonna “Old” con valore pari a “1” se Age è superiore all’età media dei passeggeri e “0” altrimenti;

        Si convertano i valori della colonna “Age” in interi.
    
"""

df_titanic = pd.read_csv("https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv", index_col='PassengerId')
print(df_titanic.info(), "\n")

df_titanic = df_titanic.dropna()

print(df_titanic.head(), "\n")

df_titanic['Sex'] = df_titanic['Sex'].replace({'male':'female'})
print(df_titanic['Sex'].head(), "\n")


df_titanic['Old'] = (df_titanic['Age'] > df_titanic['Age'].mean()).astype(int)
print(df_titanic['Old'], '\n')

print()
print(df_titanic.info(), "\n")

df_titanic['Age'] = df_titanic['Age'].astype(int)
print(df_titanic.info(), "\n")
print()

print(df_titanic['Age'].head(10), "\n")

print(df_titanic.head())


"""
Esercizio 2: Si consideri il dataset caricato e modificato nell’esercizio precedente.
Si trovi il nome del passeggero con ticket dal codice “345779”.
"""
print()
#df2 = pd.read_csv("https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv", index_col='PassengerId')
print((df_titanic[df_titanic['Ticket'] == '345779']['Name']).values, '\n')
#non mi trova nessuno perchè abbiamo tolto la riga suddetta che conteneva un valore NaN in Cabin


"""
Esercizio 3: Quali sono i nomi dei 5 passeggeri più giovani?
"""
#ci serve Name, ci serve Age, e ci serve credo qualcosa per confrontare i passeggeri

print(df_titanic.info, '\n')
print(df_titanic['Name'].head())
print()
print(df_titanic.groupby('Age')['Name'].min().loc[:5], "\n")


"""
Esercizio 4: Si consideri il dataset caricato e modificato nell’esercizio
precedente. Si selezionino tutte le osservazioni relative a passeggeri di età
compresa tra 20 e 30 anni.
"""

print(df_titanic[df_titanic["Age"].between(20, 30, inclusive='neither')]['Age'], "\n")

