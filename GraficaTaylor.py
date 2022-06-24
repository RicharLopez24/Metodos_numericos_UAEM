#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UANGEL RICARDO LOPEZ JIMENEZ

DESCRIPCION:

"""

# ----------------importaciones necesarias--------------------
import numpy as np
import sympy as sp
import math
import matplotlib.pyplot as plt
from math import factorial

# -----------variables necesarias de la funcion--------------------
x = sp.Symbol('x')
e = sp.Symbol('e')
y = math.e**(((x**2)/2))  # la funcion puede cambiar
#y = -x**3 - 0.1*x**2 - 0.15*x+1

# --------------simbolos y colores------------------------

simbolos = ['o', 'v', '^', '<', '>', 's', 'p', '*', '+', 'x', 'D', 'd']
colores = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']

# -----------------inicio de programa
print('tu funcion a evaluar es la siguiente: e**(x**2/2)')
print('va del rango desde -1 a 3')
x0 = int(input('valor de x0: ')) 
n = int(input('valor de n: '))

# ------------------varibales y listas a usar
dr = []
dr.append(y)
d = []
aux = []
d.append(y.subs(x, x0))

i = np.arange(-1, 3.2, 0.2)

y1 = []
for ran in range(len(i)):

    y1.append(d[0])

# ------------sacar derivadas y el resultado --------------
for al in range(n+1):
    aux1 = sp.diff(dr[al], x)
    aux2 = aux1.subs(x, x0)
    dr.append(aux1)
    d.append(aux2)

    print(d)
    if al == 0:
        print('iteracion ', al + 1, ': ')

        aux.append(d[al])

        plt.plot(i, y1, simbolos[al],
                 linewidth=3, color=colores[al],
                 label='k '+str(al))
        print(aux)
        print()    
    elif al > 0:
        print('iteracion ', al + 1, ': ')
        a = 0        

        y1 = aux[a] + d[al]*pow((i-x0), al)/factorial(al)
        aux[a] = y1
        plt.plot(i, y1, simbolos[al],
                 linewidth=3, color=colores[al],
                 label='k '+str(al))
        print(aux)
        print()

y = math.e**(((i**2)/2))
#y = -i**3-0.1*i**2-0.15*i+1
plt.plot(i, y, 'D', linewidth=2,
         color='k', label='funcion original')
print(y)

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
