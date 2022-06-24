#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ALUMNO: ANGEL RICARDO LOPEZ JIMENEZ

DESCRIPCION: metodo de la secante



"""
#import math 
def err(ant, act):
    return abs((act-ant)/act) *100

def raiz(fxi,fxi1,xi,xi1):
    return xi - ((fxi*(xi1-xi)) / (fxi1 - fxi) )

def impresion(i, x1, x0,error, fx,fx1,r):
    
    print('ite:',i,' x1: {:.3f}'.format(x1),' x0: {:.3f}'.format(x0),
          ' fx:{:.3f}'.format(fx),'fx1:{:.3f}'.format(fx1),'x2: {:.6f}'.format(r),
          'error:{:.6f}'.format(error))
    


#x = 0
fx = lambda x: x**2 - 3*x - 4
#fx = lambda x : (1/math.e**(x))-x
#fx = lambda x: x**3 + x +16

x0 = 5
x1 = 7

error = float(input('error aproximado: '))
#error = 0.001

i = 0
while True:
        
    fxi = fx(x1)
    fxi1 = fx(x0)
    
    r = raiz(fxi, fxi1, x1, x0)

    e = err(x1, r)

    impresion(i+1, x1, x0, e, fxi, fxi1, r)
    x0 = x1
    x1 = r
    
    i+=1
    if e < error:
        print('proceso terminado')
        break













