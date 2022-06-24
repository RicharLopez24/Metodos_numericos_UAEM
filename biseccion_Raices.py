#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

ALUMNO: ANGEL RICARDO LOPEZ JIMENEZ
PROFESOR:
DESCRIPCION: biseccion con varias raices


"""
import numpy as np
import matplotlib.pyplot as plt

import numpy as np
#------------funcion para determinar el error porcentual---------#
def error(x_actual, x_anterior):
    return  abs((x_actual-x_anterior)/x_actual)*100

#-------------funcion para calcular x_r con biseccion------------#
def x_r_Biseccion(a,b):
    return (a+b)/2

#-------------funcion para calcular x_r con regla falsa----------#
def x_r_regla_falsa(fa,fb,a,b):
     return  b - fb*(a-b)/(fa-fb)


x = np.arange(0, 4, 0.1)
f = x**2-4*x+3
tole = 0.0001
plt.plot(x, f, '-', color='b',label='fx = x**2-4*x+3')

raiz = []
valoresx = []
for i in range(len(f)):
    
    
    if f[i] == 0:
        print(i)
        valoresx.append(i/10)
        raiz.append(f[i])

print()

x1 = []
x2 = []

for i in range(len(valoresx)):
    #print(valoresx[i])
    x1.append(valoresx[i]-0.75)
    x2.append(valoresx[i]+0.75)
    
    a = x1[i]
    b = x2[i]
    print('intervalos = [', a, ',', b, ']')
    tabla = []
    tramo = abs(b-a)
    #tole = 0.0001
    fx = lambda x: x**2-4*x+3
    #f_a = pow(a, 3)+4*pow(a, 2)-10
    #f_b = pow(b, 3)+4*pow(b, 2)-10
    fa = fx(a)
    fb = fx(b)
    tabla=[]
    
    print('X_r biseccion = ',x_r_Biseccion(a, b))
    print('X_r regla falsa = ',x_r_regla_falsa(fa, fb, a, b))
    print('f(a) = ',fa,' f(b) = ',fb)
    print(tramo)
    
    while True:
        
        x_r = x_r_Biseccion(a, b)
        fx_r = fx(x_r)
        tabla.append([a,x_r,b,fa,fx_r,fb,tramo])
        
        cambio = np.sign(fa)*np.sign(fx_r)
        if cambio>0:
            tramo = abs(x_r-a)
            a = x_r
            fa = fx_r
        else:
            tramo = abs(b-x_r)
            b = x_r
            fb = fx_r
        
        if tramo <= tole:
            break
        
    tabla = np.array(tabla)
    print('it \t |\t\t [a,c,b] \t\t|\t\t [fa,fc,fb] \t\t|\t\t tramo')
    for i in range(len(tabla)):
        print(i,'\t', tabla[i,0:3],'  \t\t    ', tabla[i,3:6],'\t\t', tabla[i,6])
#print(x1,x2)    
print()



plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()