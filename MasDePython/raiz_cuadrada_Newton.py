# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 11:54:11 2020

@author: Angel
"""
x = 23
epsilon=10**(-12)
m=x/2.0
while abs(m*m-x)>epsilon:
    m = m - (((m**2)-x)/(2*m))
print('La raiz de',x,'está cerca de',m)