# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 09:27:53 2020

@author: Angel Gil
"""

# PRINT VS RETURN


def func_print():
    print('Estoy imprimiendo')
    

def func_return():
    return 'Esto es un retorno'

f1 = func_print()
f2 = func_return()

###############

def suma_print(x,y):
    print(x+y)

def suma_return(x,y):
    return x + y

s1 = suma_print(2,3)
s2 = suma_return(4,3)