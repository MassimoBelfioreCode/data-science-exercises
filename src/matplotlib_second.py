#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 11:31:01 2025

@author: codewalker
"""

from matplotlib import pyplot as plt
import numpy as np


#y = x^2

x = np.linspace(-100, 100, 300)  #vettore arbitrario di valori x estratti dal dominio della funzione
y = x ** 2                        #il massimo di y è 10000 xkè y = 100^2 = 10000, xmax=100
plt.plot(x, y)                           
plt.xlabel('x')
plt.ylabel('y')
plt.title("My plot")
plt.grid() #griglia
plt.show()


plt.plot(x, y, 'g')
plt.xlim([-30, 30])
plt.ylim([0, 900])               # y = x^2   , se x = 30 al max,  y = 900
plt.xticks([-30, 0 , 30])
plt.yticks([1000, 2000])
plt.show()



plt.figure(figsize=(12, 10))
x = np.linspace(10, 100, 200)
y = np.log(x)
plt.subplot(1, 2, 1)
plt.plot(x, y, '--+y', linewidth = 2)
plt.xlabel('x')
plt.ylabel('y')
plt.title("log(x)")


x = np.linspace(1, 100, 200)
y = np.log(x)/x**2
plt.subplot(1, 2, 2)
plt.plot(x, y, '.')
plt.xlabel('x')
plt.ylabel('y')
plt.title("log(x)/x**2")
plt.grid()

plt.show()


x = np.linspace(-2*np.pi,2*np.pi,50)
y = np.sin(x)
plt.plot(x, y, 'o-r')
plt.title("sin(x)")

plt.show()



#plt.figure() default figure size is 6.4 x 4.8 in inches, so 6.4 width and 4.8 height  
