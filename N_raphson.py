#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

ANGEL RICARDO LOPEZ JIMENEZ

DESCRIPCION: metodo de newton-raphson


"""
import sympy as sp
import math


def err(ant, act):
    return abs(act-ant)/act *100


def raiz(xi, fx, fxd):
    return xi - (fx/fxd)


def impresion(i, fx, fxd,error, f,fd,xiant,xiact):
    
    print('ite:',i,' f:',fx,' fd:',fxd,
          ' fx:{:.5f}'.format(f),'fd(x):{:.5f}'.format(fd),
          'val ante:{:.3f}'.format(xiant),'val act:{:.3f}'.format(xiact),'error:{:.6f}'.format(error))

x = sp.Symbol('x')
e = sp.Symbol('e')
fx = (1/math.e**(x))-x
fxp = sp.diff(fx,x)
x0 = 0
error = float(input('valor de error aceptado: '))
print(error,'\n')

print('funcion original', fx)
print('funcion derivada', fxp)
print()
r = []
i = 0 
r.append(x0)
while True:
    
    #evaluacion
    r.append(raiz(r[i],fx.subs(x,r[-1]) , fxp.subs(x,r[-1])))
    #print('raiz ',r)
    e = err(r[i], r[-1])
    #print(e)
    
 
    i+=1
        
    impresion(i, fx, fxp, e, fx.subs(x,r[-1]), fxp.subs(x,r[-1]), r[-2], r[-1])
    if e < error:
        
        print('proceso terminado')
        break
    

    
    











