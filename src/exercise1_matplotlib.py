#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 18:42:53 2025

@author: codewalker
"""

from matplotlib import pyplot as plt
import numpy as np

#esercizio 1

x = np.linspace(-2*np.pi,2*np.pi, 50)
y = np.cos(x)

plt.plot(x, y, '.--'+'r', linewidth = 1)
plt.show()