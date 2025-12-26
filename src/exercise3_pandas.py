#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 12:42:07 2025

@author: codewalker
"""

import pandas as pd

"""
Esercizio 7: Si consideri il dataset caricato e modificato negli esercizi 
precedenti.
Si costruisca una crosstab che permetta di rispondere alle seguenti domande:

    Quanti passeggeri di sesso maschile sono sopravvisuti in prima classe?

    Quanti passeggeri di sesso femminile sono sopravvisuti in terza classe?

    Quanti passeggeri di sesso maschile sono sopravvisuti in terza classe?

"""

df = pd.read_csv("https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv")

print(pd.crosstab(df['Sex'], [df['Survived'], df['Pclass']]), "\n")


"""
Esercizio 8: Si consideri il seguente Dataframe ...

Si costruisca un nuovo DataFrame che contenga le stesse colonne del DataFrame
considerato e che per ogni riga di esso contenga NumberOfElements nuove
righe con categoria uguale a Category di cui CheckedElements con valore di
CheckedElements pari a uno e le restanti con valore di CheckedElements pari
a zero.
"""

data = pd.DataFrame({'Category':[1,2,3], 'NumberOfElements':[3,2,3], 'CheckedElements':[1,2,1]})
print(data.info(), '\n')
print(data.shape, "\n")

print(data.NumberOfElements)
print()

newdf = []
for i, row in data.iterrows():
    for j in range(row['NumberOfElements']):
        newrow = data.copy()
        
        
print(pd.DataFrame(newdf), "\n")


