#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANGEL RICARDO LOPEZ JIMENEZ

DESCRIPCION: ejercico del metodo de biseccion y de la regla falsa



"""
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


a = int(input('Valor de a del intervalo: '))
b = int(input('Valor de b del intervalo: '))
tole = float(input('Valor de tolerancia: '))

print('intervalos = [', a, ',', b, ']')
tabla = []
tramo = abs(b-a)
#tole = 0.0001
fx = lambda x: x**3 + 4*(x**2) -10
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
    
    x_r = x_r_regla_falsa(fa, fb, a, b)
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




