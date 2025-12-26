#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 13:33:12 2025

@author: codewalker
"""

import pandas as pd
import numpy as np


#input/output con Pandas, file.csv, dataset, r, w
d = pd.read_csv('http://iplab.dmi.unict.it/furnari/downloads/students.csv')

print(d.head(), "\n")
print(d.info(), "\n")


d.to_csv('File.csv')

d.to_csv('File.csv', index=True)

print(pd.read_csv('File.csv').head())
print()
print(d.dtypes, "\n") #stampa i tipi delle variabili/colonne del dataset

print()
d = pd.read_csv('File.csv', index_col='Unnamed: 0')
print(d.head())


data = pd.read_csv('googleplaystore.csv')
print(data.head())


df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')
print(df[df['Ticket']=='345779'], '\n')

"""
Domanda 12: Visualizzare il numero medio di review per tipo (variabile Type).
"""
data = data.dropna(subset=['Type', 'Reviews'])

data["Reviews"] = pd.to_numeric(data["Reviews"], errors='coerce')

# si usa la colonna Reviews, e anche il metodo mean(), e anche la groupby, e la var "Type"
print()
print(data.groupby("Type")["Reviews"].mean().reset_index(drop=True))
