# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x=49
aprox=0.0
epsilon=0.005
step=epsilon**2
c=0
while abs(aprox**2-x)>=epsilon and aprox<=x:
    aprox+=step
    c+=1
if aprox>x:
    print('No se encontró la raíz cuadrada de',x)
else:
    print(aprox,'está cerca de la raíz cuadrada de',x)