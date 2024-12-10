# -*- coding: utf-8 -*-
"""
Hoja 1

@author: Angel Amando Gil Álamo
"""


# Ejercicio 1
    # Apartado (a). Sucesion 3, 8, 13, 18, 23,... S(n)= 3 + 5*(n-1)
n = 1
total_iter = 10

while (n < total_iter):
    print(3 + 5*(n-1),end=',')
    n = n + 1
print(3 + 5*(n-1),end='.')

    # Apartado (b). Sucesion 1, −1, 1, −1, 1, −1,... S(n)= (-1)**n
n = 1
total_iter = 10

while (n < total_iter):
    print((-1)**n,end=',')
    n = n + 1
print((-1)**n,end='.')
    
    # Apartado (c). Sucesion 1, 1, 2, 3, 5, 8,... S(n)= S(n-1)+S(n-2)
def fib(total_iter):
    n = 3
    n1 = 1
    n2 = 1

    if (total_iter == 1):
        print(n1,end='.')
    elif (total_iter == 2):
        print(n1,end=',')
        print(n2,end='.')
    else:
        print(n1,end=',')
        print(n2,end=',')
        while (n < total_iter):
            sig = n1 + n2
            n1 = n2
            n2 = sig
            print(sig,end=',')
            n = n + 1
        sig = n1 + n2
        print(sig,end='.')
    
    # Apartado (d). Sucesion 1, 2, 3, 4, 1, 2, 3, 4, 1,... Periodo 4.
def recur4(total_iter):
    n = 1
    while (n < total_iter):
        if (n%4 == 1):
            print(1,end=',')
        elif (n%4 == 2):
            print(2, end=',')
        elif (n%4 == 3):
            print(3, end=',')
        else:
            print(4, end=',')
        n = n + 1
    if (n%4 == 1):
        print(1,end='.')
    elif (n%4 == 2):
        print(2, end='.')
    elif (n%4 == 3):
        print(3, end='.')
    else:
        print(4, end='.')
    
    # Apartado (e). Sucesion −1, 0, 1, −1, 0, 1, −1,... Periodo 3.
def recur3(total_iter):
    n = 1
    while (n < total_iter):
        if (n%3 == 1):
            print(-1,end=',')
        elif (n%3 == 2):
            print(0, end=',')
        else:
            print(1, end=',')
        n = n + 1
    if (n%3 == 1):
        print(-1,end='.')
    elif (n%3 == 2):
        print(0, end='.')
    else:
        print(1, end='.')

    


# Ejercicio 2
    # Apartado (a).
m_aux = input('Peso en kg: ')
m = float(m_aux)
m_gr = m * 1000
print (m_aux,'kg equivalen a',m_gr,'gramos.')  
    # Inverso de (a).
m_aux = input('Peso en gramos: ')
m = float(m_aux)
m_kg = m / 1000
print (m_aux,'gramos equivalen a',m_kg,'kg.')

    # Apartado (b).
m_aux = input('Peso en kg: ')
m = float(m_aux)
m_lb = m * 2.20462
print (m_aux,'kg equivalen a',m_lb,'libras.')  
    # Inverso de (b).
m_aux = input('Peso en libras: ')
m = float(m_aux)
m_lb = m / 2.20462
print (m_aux,'libras equivalen a',m_lb,'kg.') 
    
    # Apartado (c).
f_aux = input('Grados Farenheit: ')
farenheit = float(f_aux)
celsius = 5/9 * (farenheit - 32)
print (farenheit,'grados farenheit equivalen a',celsius,'grados celsius.')
    # Inverso de (c).
c_aux = input('Grados Celsius: ')
celsius = float(c_aux)
farenheit = 9/5 * celsius +32
print (celsius,'grados celsius equivalen a',farenheit,'grados farenheit.')


# Ejercicios 3 y 4

from math import sqrt

a_aux = input('Longitud lado a: ')
b_aux = input('Longitud lado b: ')
c_aux = input('Longitud lado c: ')

a = int(a_aux)
b = int(b_aux)
c = int(c_aux)

s = (a + b + c) / 2
Area = sqrt(s*(s-a)*(s-b)*(s-c))

esTriangulo = (a + b > c) and (a + c > b) and (b + c > a)
esEscaleno = (a != b) and (a != c) and (b != c)
esEquilatero = (a == b) and (a == c) and (b == c)

if esTriangulo: 
    if esEscaleno:
        print('Estos lados forman un triangulo escaleno')
    elif esEquilatero:
        print('Estos lados forman un triangulo equilatero')
    else:
        print('Estos lados forman un triangulo isosceles')
    print('El area del triangulo es:',Area)
else:
    print('Estos lados no pueden formar un triangulo.')


# Ejercicio 5
    #Apartado (a).
from math import sqrt

m_aux = input('Candidato a cuadrado perfecto: ')
m = int(m_aux)
def es_perfecto(m):
    
    return int(sqrt(m)) == sqrt(m)
    
print ('¿Es',m,'un cuadrado perfecto?',es_perfecto(m))

### Apartado (a) version Sonia ###
"""
from math import sqrt

m_aux = input('Candidato a cuadrado perfecto: ')
m = int(m_aux)
def es_perfecto2(m):
    
    num = sqrt(m)
    return m == num * num

print ('¿Es',m,'un cuadrado perfecto?',es_perfecto(m))
"""
# Apartado (b).
def cuadrado_perfecto_previo(m):
    num= int(sqrt(m))
    return num**2
print ('El cuadrado perfecto previo de',m,'es',cuadrado_perfecto_previo(m))