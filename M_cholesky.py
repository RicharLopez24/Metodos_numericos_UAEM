#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 ANGEL RICARDO LOPEZ JIMENEZ
DESCRIPCION: metodo de cholesky



"""
from sympy import symbols, Eq, solve
import numpy as np 


def determinantes(arr, tam):

 
    d1 = []
    for i in range(tam):        
        d2 = arr[0:i+1,0:i+1]
        det = np.linalg.det(d2)
        d1.append(det)    
    return d1
            
def descomposicion(tam):
    
    letras = symbols("a b c d e f g h i j k l m n o p q r ")
    
    tam = 3
    a = []
    cont = 0
    for i in range(tam):
        a.append([])
        for j in range(tam):            
            if (i == 0 and j == 0) or (i == 0 and j > 0) or (i >= 1 and i <= j):    
                a[i].append(letras[cont])
                cont += 1            
            else:
                a[i].append(0)
                
    at = np.transpose(a)      
    multi = np.dot(at,a)
    a = np.array(a)    
    return np.array(multi), letras, at,a 
    
def calc_variables(mdvar,mdata, letras):
    
    valor = []
    
    equation_1 = Eq( (mdvar[0, 0]), mdata[0,0])    
    a = solve(equation_1, letras[0])
    valor.append(int(a[1]))
    
    equation_1 = Eq( a[1]*letras[1], mdata[0,1])
    b = solve(equation_1, letras[1])
    valor.append(int(b[0]))
    
    equation_1 = Eq( a[1]*letras[2], mdata[0,2])
    c = solve(equation_1, letras[2])
    valor.append(int(c[0]))
    
    equation_1 = Eq( (pow(b[0],2)+pow(letras[3],2) ), mdata[1,1])
    d = solve(equation_1, letras[3])
    valor.append(int(d[1]))
    
    equation_1 = Eq( ( b[0]*c[0] + d[1]*letras[4]), mdata[1,2])
    e = solve(equation_1, letras[4])
    valor.append(int(e[0]))
    
    equation_1 = Eq( ( pow(c[0], 2)+pow(e[0], 2)+pow(letras[5], 2) ), mdata[2,2])
    f = solve(equation_1, letras[5])
    valor.append(int(f[1]))
    
    return valor

def Remplazar(mL, mLT, variables):
    
    letras = symbols("a b c d e f g h i j k l m n o p q r ")
    cont = 0
    cont1 = 0
    for i in range(tam):
        
        for j in range(tam):    
            if mLT[i,j] == letras[cont] :
                mLT[i,j] = variables[cont]
                cont+=1
            if mL[j,i] == letras[cont1] :
                mL[j,i] = variables[cont1]
                cont1+=1    
    return mL, mLT

def valores_y(mL, mva,mLT):
    
    a, b, c = symbols("a b c")

    equation_1 = Eq((mL[0, 0]*a), int(mva[0]))    
    sa = solve(equation_1, (a))
    print('y1:',sa[0])
    sa = sa[0]
    
    equation_2 = Eq((mL[1, 0]*sa + mL[1, 1]*b), int(mva[1]))
    sb = solve(equation_2, (b))
    print('y2:',np.array(sb[0]))
    
    sb = sb[0]    
    equation_3 = Eq((mL[2, 0]*sa + mL[2, 1]*sb + mL[2, 2]*c), int(mva[2]))    
    sc = solve((equation_3), (c))
    print('y3:',np.array(sc[0]))
    sc = sc[0]
    
    #-------valores de xyz    
    x, y, z = symbols('x y z')

    ez = Eq((mLT[2, 2]*z), sc)
    sz = solve(ez, (z))
    sz = sz[0]
    
    ey = Eq((mLT[1, 1]*y + mLT[1, 2]*sz), sb)
    sy = solve(ey, (y))
    sy = sy[0]
    
    ex = Eq((mLT[0, 0]*x + mLT[0, 1]*sy + mLT[0, 2]*sz), sa)
    sx = solve(ex, (x))
    sx = sx[0]
    print('x = ',sx,'y = ',sy,'z = ',sz)

    
# ------------ingresar datos de las ecuaciones
a = []
tam = 3


#--- se pude descomentar esta parte de codigo para qingresar lo valores que desea
#y comentar los arreglos a y b 
'''print('ingresa los valores de las ecuaciones en forma de matriz')
for i in range(tam):
    a.append([])
    for j in range(tam):
        val = float(input('valor [{},{}]: '.format(i+1, j+1)))
        a[i].append(val)

print('\n', np.array(a))
r = []
print('\n valores de la filas igualadas')

for i in range(3):
    val = float(input('fila [{}] es igual a : '.format(i+1)))
    r.append(val)
print('\nvalores de las filas \n', r)

r = np.transpose(r)

'''

#comentar desde qui    
a = np.array([[1,-1,1],
              [-1,5,-5],
              [1,-5,6]])    

b = np.array([[3],
              [-18],
              [21]] , dtype=int)
at = np.transpose(a)

a1 = np.concatenate((a, b), axis=1)
#hasta aca

print('matriz original\n', a1,'\nmatriz transpuesta\n',at)
a = np.array(a)

if ((a == at).all()) == True:
    print('son iguales')
    
    deter = determinantes(a, tam)
    print(deter)
    
    if deter[0] > 0 and deter[1] > 0 and deter[2] > 0:        
        print('los determinantes son {:.0f}, {:.0f}, {:.0f}'
              .format(deter[0], deter[1],deter[2]))
        mdvar, letras, mL , mLT = descomposicion(tam)
        variables = calc_variables(mdvar, a,letras)
        print('\n valor de las variables\n',variables)
        
        print('matriz L:\n',mL,'\nmatriz transpuesta:\n',mLT)
        print()
        mL, mLT = Remplazar(mL, mLT, variables)

        print('valores finales: \n')
        valores_y(mL, b,mLT)
    
else:
    print('no lo son \n !findel programa')  
    
