# -*- coding: utf-8 -*-
"""
Hoja 3: Bucles While

@author: Angel Amando Gil Álamo
"""


# Ejercicio 1: Reverso de un número.
def reverso(n):
    if type(n) != int:
        print ('¡El número tiene que ser entero!')
    else:
        m = 0
        while n > 0:
            m = 10*m + (n % 10) 
            n = n // 10
        return m

# Ejercicio 2: Media de los dígitos de un número entero.
def media_digitos(n):
    if type(n) != int or n < 0:
        print ('¡El número tiene que ser entero positivo!')
    else:
        m = 0
        i = 0
        while n > 0:
            m = m + (n % 10) 
            n = n // 10
            i = i + 1
        return m/i
    
# Ejercicio 3: Dígitos ordenados.
def ordenados(n):
    if type(n) != int or n < 0:
        print ('¡El número tiene que ser entero positivo!')
    else:
        evaluacion = True
        m = 9
        while n > 0:
            r = m
            m = n % 10 
            n = n // 10
            if r < m:
                evaluacion = False
        if evaluacion:
            print ('Los dígitos SÍ están ordenados crecientemente.')
        else:
            print ('Los dígitos NO están ordenados crecientemente.')

# Ejercicio 4: Palíndroma.
def palindroma(palabra):
    if type(palabra) != str:
        print ('¡Tiene que ser una palabra (de tipo str, con comillas)!')
    else:
        palindromo = True
        i = 0
        j = len(palabra) - 1
        while i < j:
            if palabra[i] != palabra[j]:
                palindromo = False
            i = i + 1
            j = j - 1
        if palindromo:
            print ('La palabra SÍ es palíndroma.')
        else:
            print ('La palabra NO es palíndroma.')
        