# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:39:35 2020

@author: Angel
"""

x=23
epsilon=0.0000000000001
low=0.0
high=x
aprox=(high+low)/2.0
while abs(x-aprox**2)>=epsilon and x>aprox:
    if aprox**2 < x:
        low = aprox
    else:
        high=aprox
    aprox=(high+low)/2.0
if aprox>x:
    print('Error en el calculo de la raiz de',x)
else:
    print(aprox,'está cerca de la raíz cuadrada de',x)
