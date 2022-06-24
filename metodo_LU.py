#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ANGEL RICARDO LOPEZ JIMENEZ

DESCRIPCION: metodo de lu


"""

# -----------importaciones necesarias
from sympy import symbols, Eq, solve
import numpy as np


# ------------ingresar datos de las ecuaciones
a = []
print('ingresa los valores de las ecuaciones en forma de matriz')
for i in range(3):
    a.append([])
    for j in range(3):
        val = float(input('valor [{},{}]: '.format(i+1, j+1)))
        a[i].append(val)

print('\n', np.array(a))
r = []
print('\n valores de la filas igualadas')

for i in range(3):
    val = float(input('fila [{}] es igual a : '.format(i+1)))
    r.append(val)
print('\nvalores de las filas \n', r)
# ------------transponer los datos y unirlos
B = np.transpose([r])
AB = np.concatenate((a, B), axis=1)
AB1 = np.copy(AB)

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# -----------obtenemos una matriz identidad para usarla posteriormente
L = np.identity(n, dtype=float)

# -----------ciclo para obtener la matriz U y L
for i in range(0, n-1):
    piv = AB[i, i]
    for k in range(i + 1, n):
        val = AB[k, i]/piv
        AB[k, :] = AB[k, :] - AB[i, :]*val
        L[k, i] = val

U = np.copy(AB[:, :m-1])
#print('matriz original \n', AB1)
print('\nmatriz U \n', U)
print('\nmatriz L \n', L)

print('\n')
# print(np.dot(L,U))

# ----resolver ecuaciones con para obtener a,b y c
a, b, c = symbols("a b c")

equation_1 = Eq((L[0, 0]*a), r[0])
print(equation_1)
sa = solve(equation_1, (a))
#print(sa[0])
sa = sa[0]

equation_2 = Eq((L[1, 0]*sa + L[1, 1]*b), r[1])
sb = solve(equation_2, (b))
# print(np.array(sb[0]))

sb = sb[0]

equation_3 = Eq((L[2, 0]*sa + L[2, 1]*sb + L[2, 2]*c), r[2])

sc = solve((equation_3), (c))
# print(np.array(sc[0]))
sc = sc[0]

# --------obtenemos los valores de x,y y z

x, y, z = symbols('x y z')

ez = Eq((U[2, 2]*z), sc)
sz = solve(ez, (z))
#print('z = {:.2}'.format(sz[0]))
sz = sz[0]

ey = Eq((U[1, 1]*y + U[1, 2]*sz), sb)
sy = solve(ey, (y))
#print('y = {:.2}'.format(sy[0]))
sy = sy[0]

ex = Eq((U[0, 0]*x + U[0, 1]*sy + U[0, 2]*sz), sa)
sx = solve(ex, (x))
sx = sx[0]
print('x = {:.2f}'.format(sx),'y = {:.2f}'.format(sy),'z = {:.2}'.format(sz))
