#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANGEL RICARDO LOPEZ JIMENEZ

DESCRIPCION:
descomposicion en L U


"""


import numpy as np

# INGRESO
A = np.array([[1.,4.,-2.],
              [ 3.,-2.,5.],
              [ 2.,3.,1.]], dtype=float)

B = np.array([3.,14.,11.], dtype=float)

B  = np.transpose([B])
AB = np.concatenate((A,B),axis=1)
AB1 = np.concatenate((A,B),axis=1)
AB = np.copy(AB)


tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]


L = np.identity(n,dtype=float)
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i+1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
        L[k,i] = factor

U = np.copy(AB[:,:m-1])

# SALIDA
print('Matriz original')
print(AB1)
print('eliminación hacia adelante')
print('Matriz U: ')
print(U)
print('matriz L: ')
print(L)

M = np.dot(L,U)
print('comprobacion de multiplicacion\n',M)