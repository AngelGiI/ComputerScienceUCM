# -*- coding: utf-8 -*-
"""
Practica 1 - Cuadrado magico.

@author: Angel Amando Gil Alamo
"""

#Ejercicio 1.
def distinct_numbers(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    if (2**a11 + 2**a12 + 2**a13 + 2**a21 + 2**a22 + 2**a23 + 2**a31 + 2**a32 + 2**a33 == 2**10 - 2):
        return (True)
    else:
        return (False)
    
#Ejercicio 2.
def sum_row(a11, a12, a13, a21, a22, a23, a31, a32, a33, i):
    total = 0
    if i == 1:
        total =  a11 + a12 + a13
    elif i == 2:
        total = a21 + a22 + a23
    else:
        total = a31 + a32 + a33
    return total
                  
#Ejercicio 3.
def sum_column(a11, a12, a13, a21, a22, a23, a31, a32, a33, c):
    total = 0
    if c == 1:
        total =  a11 + a21 + a31
    elif c == 2:
        total = a12 + a22 + a32
    else:
        total = a13 + a23 + a33
    return total

#Ejercicio 4.
def sum_diagonal(a11, a12, a13, a21, a22, a23, a31, a32, a33, d): 
    total = 0
    if d == 1:
        total = a11 + a22 + a33
    else:
        total = a13 + a22 + a31
    return total

#Ejercicio 5.
def magic_square(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    if (distinct_numbers(a11, a12, a13, a21, a22, a23, a31, a32, a33) and 
                (sum_row(a11, a12, a13, a21, a22, a23, a31, a32, a33, 1) ==
                 sum_row(a11, a12, a13, a21, a22, a23, a31, a32, a33, 2) ==
                 sum_row(a11, a12, a13, a21, a22, a23, a31, a32, a33, 3) ==
                 sum_column(a11, a12, a13, a21, a22, a23, a31, a32, a33, 1) ==
                 sum_column(a11, a12, a13, a21, a22, a23, a31, a32, a33, 2) ==
                 sum_column(a11, a12, a13, a21, a22, a23, a31, a32, a33, 3) ==
                 sum_diagonal(a11, a12, a13, a21, a22, a23, a31, a32, a33, 1) ==
                 sum_diagonal(a11, a12, a13, a21, a22, a23, a31, a32, a33, 2))):
        return (True,sum_row(a11, a12, a13, a21, a22, a23, a31, a32, a33, 1))
    else:
        return (False,0)