#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 09:56:10 2025

@author: codewalker
"""

import pandas as pd
import numpy as np
from exercise1_pandas import df_titanic

print("dataframe importato\n")
print(df_titanic.info(), '\n')


"""
Esercizio 5: Si consideri il dataset caricato e modificato negli esercizi
precedenti. Si calcoli la tariffa media pagata dai passeggeri di sesso 
femminile in seconda classe.
"""

print(df_titanic['Cabin'].head(10), "\n")
print(df_titanic['Pclass'].head(10), "\n")
print(df_titanic.groupby('Pclass')['Fare'].mean(), "\n")

print("tariffa media donne II classe: ")
print(df_titanic[df_titanic['Pclass'] == 2]['Fare'].mean(), "\n")
#siccome stiamo operando sul dataframe con solo donne si fa così

"""
Esercizio 6: Si consideri il dataset caricato e modificato negli esercizi
precedenti. Si costruisca una crosstab che permetta di rispondere alle seguenti
domande:

    Quanti passeggeri di sesso maschile sono sopravvisuti?

    Quanti passeggeri di sesso femminile non sono sopravvisuti?

"""
print(pd.crosstab(df_titanic['Sex'], df_titanic['Survived'], normalize=True), "\n")

#df = pd.read_csv("https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv")
#print(pd.crosstab(df['Sex'], df['Survived'], normalize=True), "\n")

"""
Esercizio 7: Si consideri il dataset caricato e modificato negli esercizi 
precedenti.
Si costruisca una crosstab che permetta di rispondere alle seguenti domande:

    Quanti passeggeri di sesso maschile sono sopravvisuti in prima classe?

    Quanti passeggeri di sesso femminile sono sopravvisuti in terza classe?

    Quanti passeggeri di sesso maschile sono sopravvisuti in terza classe?

"""

