# -*- coding: utf-8 -*-
"""
Hoja 4: Listas

@author: Angel Amando Gil Álamo
"""


# Ejercicio 1: Communitary.
def divisor(d,l):
    lista=[]
    for i in range(len(l)):
        if l[i] % d == 0:
            lista.append(True)
        else:
            lista.append(False)
    return all(lista)
        
def communitary(lst):
    n = 2
    encontrado = False
    while n <= min(lst) and not encontrado:
        if divisor(n,lst):
            encontrado = True
            print('La lista es comunitaria y',n,'es un divisor común.')
        else:
            n = n + 1
    if not encontrado:
        print ('La lista NO es comunitaria')
        
# Ejercicio 2: Barroca.
def  is_baroque(l):
    lista=[]
    for i in range(len(l)):
        if i % 2 == 0:
            if l[i] % 2 == 0:
                lista.append(True)
            else:
                lista.append(False)
        else:
            if l [i] % 2 == 1:
                lista.append(True)
            else:
                lista.append(False)
    if all(lista):
        print('La lista es barroca.')
    else:
        print('La lista NO es barroca.')
            
# Ejercicio 3: Menores.
def menores(v,m):
    i = 0; l=[]
    while v > m[i]:
        l.append(m[i])
        i = i + 1
    return l
        
# Ejercicio 4: Enteros libres de cuadrados.
def es_libre(n):
    p = 2
    while n % (p ** 2) != 0 and p ** 2 <= n:
        p = p + 1
    if p ** 2 > n:
        return True
    else:
        return False

def libres(lim):
    i = 1; l=[]
    while i <= lim:
        if es_libre(i):
            l.append(i)
        i = i + 1
    return l
            
    
# Ejercicio 5: Piritiguay.
def piritiguay(n):
    a = 0; b = 0
    control = True
    while control:
        if n % 2 == 0:
            a = a + 1
            n = n / 2
        elif n % 3 == 0:
            b = b + 1
            n = n / 3
        else:
            control = False
    if b > a:
        return False
    else:
        return True
    
def piritilista(l):
    m = 0
    while m + 1 <= len(l):
        if piritiguay (l[m]) == True:
            m = m + 1
        else:
            break
    if m + 1 <= len(l):
        print('La lista NO es piritiguay.')
    else:
        print('La lista es piritiguay.')

