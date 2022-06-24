
"""
 ANGEL RICARDO LOPEZ JIMENEZ
DESCRIPCION:
    obtener la digonal de una matriz usando gauss
"""

import numpy as np

# datos a evaluar
A = np.array([[1,4,-5],
              [3,-1,1],
              [2,3,1]])    

B = np.array([[-17],
              [10],
              [-2]] )

#matriz aumentada
AB = np.concatenate((A,B),axis=1)
AB0 = np.copy(AB)

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

# eliminacion hacia adelante
for i in range(0,n-1,1):
    pivote = AB[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor
AB2 = np.copy(AB)

# elimina hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = AB[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = AB[k,i]/pivote
        AB[k,:] = AB[k,:] - AB[i,:]*factor

    AB[i,:] = AB[i,:]/AB[i,i]
X = np.copy(AB[:,ultcolumna])
X = np.transpose([X])


# SALIDA
print('Matriz:\n',AB0)
print('eliminacion hacia adelante:\n',AB2)
print('eliminación hacia atrás:\n',AB)
print('solución de X:\n',X)