#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANGEL RICARDO LOPEZ JIMENEZ
DESCRIPCION: ejemplo de la pagina 48 del libro metodos numericos
para ingenieros



"""

from math import factorial,exp
import math

def Imprimir(i,ex,Et,Ea):
    print('term: ',i,'resultado: {:.9f}'.format(ex),'Et: {:.5f}'.format(Et)
              ,'Ea: {:.4f}'.format(Ea))

def EcuEt(ex):
    return (exp(0.5)-ex)/exp(0.5)*100

def EcuEa(ex,ant):
    tam = len(ant)
    return ((ex - ant[tam - 2])/ex)*100

cifras = int( input('# cifras significativas: '))
Es = (0.5*pow(10,2-cifras))
print('criterio de error: ',Es)
i = 0
ant = []

while True:
    
    if i == 0:
        ex = 1
        Et = EcuEt(ex)
        ant.append(ex)        
        Ea = EcuEa(ex, ant)
        i += 1   
        Imprimir(i, ex, Et, Ea)
        
    elif i == 1:
        ex +=  0.5
        Et = EcuEt(ex)
        ant.append(ex)
        Ea = EcuEa(ex, ant)
        i += 1   
        Imprimir(i, ex, Et, Ea)
        
        if Ea < Es:
            break
    elif i > 1:
        ex += math.pow(0.5, i)/ factorial(i)
        Et = EcuEt(ex)
        ant.append(ex)        
        Ea = EcuEa(ex, ant)
        i += 1   
        Imprimir(i, ex, Et, Ea)
        
        if Ea < Es:
            break
    