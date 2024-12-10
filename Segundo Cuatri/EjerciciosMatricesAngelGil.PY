# -*- coding: utf-8 -*-
"""
Ejercicios propuestos del fichero 'Matrices'.

@author: Angel Gil
"""

# EJERCICIO 1: Define y prueba tu función intercCols(m,c1,c2) que ha de
#              intercambiar dos columnas.

def intercFilas(m,f1,f2):              # Definimos intercFilas y trasponer
    if f1 != f2:                       # como en los apuntes.
        if f1 > f2:
            f1,f2 = f2,f1
        fila1=m.pop(f1)
        m.insert(f1,m[f2-1])
        m[f2]=fila1
    return m

def trasponer(m):
    tm=[]
    for i in range(len(m[0])):
        tm.append([])
    for i in range(len(m)):
        for j in range(len(m[i])):
            tm[j].append(m[i][j])
    return tm

def intercCol(m,c1,c2):                # Trasponemos para operar por filas.
    tras = trasponer(m)                # Una vez hechos los cambios, volvemos
    cambio = intercFilas(tras,c1,c2)   # a trasponer.
    M = trasponer(cambio)
    return M

# Ejercicios adicionales:
# 1. Escribe una función que dada una matriz CUADRADA detecte si es TRIANGULAR
#    INFERIOR ( o sea tiene todo 0´s ) por ENCIMA de la diagonal.
def esTinf(m):
    todoCeros = True
    for i in range(len(m)):
        for j in range(i+1,len(m)):    # Nos interesan solo los indices que
            if m[i][j] != 0:           # esten por encima de la diagonal.
                todoCeros = False 
    return todoCeros

# 2. Idem TRIANGULAR SUPERIOR.
def esTsup(m):
    todoCeros = True
    for i in range(len(m)):
        for j in range(0,i):           # Nos interesan solo los indices que
            if m[i][j] != 0:           # esten por debajo de la diagonal.
                todoCeros = False 
    return todoCeros

# 3. Escribe una función que dada una matriz CUADRADA nos diga si su DIAGONAL
#    PRINCIPAL es todo 1´s.
def UnosDiagonal(m):
    todoUnos = True
    for i in range(len(m)):            # Sea m[i][j] el elemento de la i-esima
            if m[i][i] != 1:           # fila y la j-esima columna, nos
                todoUnos = False       # interesan aquellos donde i = j.
    return todoUnos

# 4. Escribe una función que dada una matriz CUADRADA nos diga si es la
#    correspondiente matriz IDENTIDAD.
def esIdentidad(m):
    if esTinf(m) and esTinf(m) and UnosDiagonal(m):
        I = True                       # m sera la matriz identided si y solo
    else:                              # si se cumplen simultaneamente las 3
        I = False                      # condiciones de los ejs anteriores.
    return I

# 5. Escribe una función que dadas dos matrices CUADRADAS nos diga si son
#    inversas la una de la otra.

def prodEscalar(v1,v2):                # Definimos la multiplicacion de
    pr=0                               # matrices de la segunda forma mostrada
    for i in range(len(v1)):           # en los apuntes.
        pr=pr+v1[i]*v2[i]
    return pr

def multMatVectorial(m1,m2):
    m2Tras=trasponer(m2)
    mr=[]
    for i in range(len(m1)):
        mr.append([])
        for j in range(len(m2Tras)):
            mr[i].append(prodEscalar(m1[i],m2Tras[j]))
    return mr

def sonInversas(m1,m2):                # Multiplicamos las dos matrices. Si la
    m = multMatVectorial(m1,m2)        # matriz resultante es suficientemente
    tol = 10**(-10)                    # cercana (por eso la tolerancia) a la
    esIden = True                      # identidad termino a termino, entonces
    for i in range(len(m)):            # devolveremos True.
        for j in range(len(m[0])):
            if i < j or j < i:         
                if abs(m[i][j]) > tol:
                    esIden = False
            else:
                if abs(m[i][j] - 1) > tol:
                    esIden = False
    return esIden