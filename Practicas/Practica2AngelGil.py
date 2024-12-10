# -*- coding: utf-8 -*-
"""
Practica 2 - Juego del NIM.

@author: Angel Amando Gil Alamo
"""

#Ejercicio 1.

def hacer_jugada(mts, m, p):
    if len(mts) == 0 or m > len(mts)-1 or mts[m] < p:
        return mts            # Si esta vacia, queremos trabajar en un monton
    else:                     # que no existe o queremos quitar mas fichas         
        mts[m] = mts[m] - p   # de las que hay, devolvemos la lista intacta. 
        return mts

#Ejercicio 2.
def cifra_i_base2(n,i):
    for j in range(i+1):
        if n % 2 == 0:
            n = n/2
            cifra=0          # 'Cifra' se va actualizando con la cifra i-esima
        else:                # de la descomposicion hasta llegar a la posicion
            n = (n - 1)/2    # deseada.
            cifra=1
    return cifra
        
#Ejercicio 3.
def desc_bin(n): # funcion auxiliar que devuelve un numero (<32) en base 2
    l=[]         # como lista (ordenada).
    if n > 31:
        raise Exception("No se admiten montones de mas de 31 piezas.")
    while n > 0:
        if n % 2 == 0:
            n = n/2
            l.insert(0,0)   # Añadimos la nueva cifra al principio de la lista
        else:               # para que la factorizacion se devuelva ordenada.
            n = (n - 1)/2
            l.insert(0,1)
    while len(l) < 5:
        l.insert(0,0)       # Añadimos 0's hasta llegar a longitud 5.
    return l

def sumas(mts):
    suma=[0,0,0,0,0]
    for i in range(len(mts)):    # Llamamos a 'desc_bin' para cada monton.
        l = desc_bin(mts[i])     # y vamos calculando la suma acumulada en 
        for j in range(len(l)):  # modulo 2 sin llevadas.
            suma[j] = (suma[j] + l[j]) % 2
    return suma

#Ejercicio 4.
def terminada(mts):
    acabada = True
    for i in range(len(mts)): # Recorremos 'mts' comprobando si vale 0 en
        if mts[i] != 0:       # todas las posiciones. De lo contrario,
            acabada = False   # devolvemos 'False'.
    return acabada

#Ejercicio 5.
def ganadora(mts):
    ganamos = False
    veamos = sumas(mts)          # Llamando a 'sumas(mts)' obtenemos la suma
    for i in range(len(veamos)): # deseada, solo queda comprobar si hay algun
        if veamos[i] != 0:       # elemento distinto de 0.
            ganamos = True
    return ganamos
            
#Ejercicio 6.
def jugada_ganadora(mts):
    i = 0; a = sumas(mts)
    while a[i] == 0:          # Primero encontramos en que posicion de la suma
        i = i + 1             # sin llevadas esta el 1 "mas a la izquierda".
    j = 0; b = mts[j]; c = desc_bin(b)
    while c[i] == 0 and j < len(mts) - 1:      # Encontramos un monton (el 1º
        j = j + 1; b = mts[j]; c = desc_bin(b) # de hecho) que tenga un 1 en 
                                               # dicha posicion.
    d = 0                                   
    while i < len(a):                   # Evaluamos desde el primer '1' de la
        if a[i] == 1:                   # suma en adelante, acumulando en 'd'
            if c[i] == 1:               # el numero de fichas a sustraer.
                d = d + 2 ** (4 - i)
            else:
                d = d - 2 ** (4 - i)
        i = i + 1
    return j,b,d

#Ejercicio 7.
# He buscado en internet como generar numeros aleatorios, viene de perlas para
# que el juego se sienta un poco mas 'vivo'.

# Por lo visto basta con importar la funcion randint que, como su nombre
# sugiere, genera enteros aleatorios entre dos extremos, ambos incuidos.
def jugada_perdedora(mts):
    from random import randint                # Importamos randint.
    monton = randint(0,len(mts)-1)            # Elegimos un monton aleatorio.
    fichas_monton = mts[monton]     
    cuantas_cojo = randint(1,fichas_monton)   # Cogemos un numero aleatorio de
    return monton,fichas_monton,cuantas_cojo  # fichas (minimo 1).

#Ejercicio 8.
def juega_maquina(mts):
    if ganadora(mts):                  # Hacemos uso de las funciones que 
        b = jugada_ganadora(mts)       # hemos ido construyendo. Si estamos en
    else:                              # posicion ganadora, jugamos para ganar.
        b = jugada_perdedora(mts)      # Si no, hacemos una jugada aleatoria
    return hacer_jugada(mts,b[0],b[2]) # pero valida.
