# -*- coding: utf-8 -*-
"""
Hoja 2: Condicionales

@author: Angel Amando Gil Álamo
"""


# Ejercicio 1: Mínimo de 4 números.
def minimo(a,b,c,d):
    if a <= b and a <= c and a <= d:
        return a 
    elif b <= a and b <= c and b <= d:
        return b
    elif c <= a and c <= b and c <= d:
        return c
    else:
        return d
    
    # Apartado b) minimo con solo 3 comparaciones.
def min3(a,b,c,d):
    if a < b:
        m = a
    else:
        m = b
    if c < m:
        m = c
    if d < m:
        m = d
    return m

# Ejercicio 2: Encuentra la actividad adecuada.
def act_adecuada(temp):
    if temp > 30:
      print ('La actividad adecuada para esta temperatura es Natación.')  
    elif 20 < temp <= 30 :
      print ('La actividad adecuada para esta temperatura es Tenis.')
    elif 10 < temp <= 20 :
      print ('La actividad adecuada para esta temperatura es Golf.') 
    elif 5 < temp <= 10 :
      print ('La actividad adecuada para esta temperatura es Esquí.')
    else:
      print ('La actividad adecuada para esta temperatura es Parchís.') 
    
# Ejercicio 3: Posición de un punto en un cuadrante.
def cuadrante(x,y):
    if x>0 and y>0:
        print ('Este punto se encuentra en el primer cuadrante.')
    elif x<0 and y>0:
        print ('Este punto se encuentra en el segundo cuadrante.')
    elif x<0 and y<0:
        print ('Este punto se encuentra en el tercer cuadrante.')
    elif x>0 and y<0:
        print ('Este punto se encuentra en el cuarto cuadrante.')
    elif x==0 and y==0:
        print ('Este punto se encuentra en el origen.')
    elif x==0:
        print ('Este punto se encuentra en el eje de abcisas.')
    else:
        print('Este punto se encuentra en el eje de ordenadas.')

# Ejercicio 4: Rotación del alfabeto.

    # Hallé una solución que me pareció bonita y simple con listas.
def rotacion_abc(inicio,n):
    ABC = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
         'Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    aux = ABC.index(inicio)
    if aux + n >= len (ABC):
        return ABC[aux + n - len(ABC)]   
    else:
        return ABC[aux + n]
    
    # Como en clase.
def rotar (c,n):
    rot = ord('A') + ((ord(c) + n - ord ('A')) % 26)    
    return chr(rot)
    
# Ejercicio 5: ¿Me puede decir la hora?
def hora_correcta(h,m,s):
    if (type(h) != int) or (type(m) != int) or (type(s) != int):
        print ('¡La hora tiene que venir dada en enteros!')
    elif (0 <= h <= 23) and (0 <= m <= 59) and (0 <= s <= 59):
        print ('Son las',h,end='h ')
        print (m,end='m ')
        print (s,end='s')
    else:
        print ('¡Esa no es una hora válida!')
    
# Ejercicio 6: Ser o no ser bisiesto.
def es_bisiesto(n):
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                print (n,'es año bisiesto (a pesar de ser divisible por 100).')
            else:
                print (n,'no es año bisiesto (divisible por 100 pero no por 400).')
        else:
            print (n,'es año biesiesto (divisible por 4 y no por 100).')
    else:
        print (n,'no es año bisiesto (no es divisible por 4).')
        
# Ejercicio 7: Días del mes.
def dias_del_mes(n):
    if type(n) != int or n < 1 or n > 12:
        print ('¡El número del mes tiene que ser entero del 1 al 12!')
    elif n % 2 == 0:
        if n == 2:
            return 28
        if n < 7:
            return 30
        else:
            return 31
    else:
        if n < 7:
            return 31
        else:
            return 30
    
# Ejercicio 8: Facturación por tramos.
def tarifa(m3):
    if m3 <= 100:
        total = 0.15 * m3
    elif 100 < m3 <= 500:
        total = 15 + (m3 - 100) * 0.2
    elif 500 < m3 <= 1000:
        total = 95 + (m3 - 500) * 0.35
    else:
        total = 270 + (m3 - 1000) * 0.8
    return total
 
# Ejercicio 9: Capicúas de tres cifras.
def capicua3(n):
    if type(n) != int or n < 100 or 999 < n:
        print('¡El número no es entero de tres cifras!')
    else:
        tercera = n % 10
        primera = n // 100
        if tercera == primera:
            print (n,'es capicua.')
        else:
            print (n,'no es capicua.')