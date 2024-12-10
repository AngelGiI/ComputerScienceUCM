# -*- coding: utf-8 -*-
"""
Práctica 3: filtros de imágenes.

@author: Ángel Gil
"""

from PIL import Image

def min_max(img):
    w,h = img.size
    minimo,maximo = img.getpixel((0,0)), img.getpixel((0,0))
    for x in range(w):
        for y in range(h):
            minimo = min(img.getpixel((x,y)),minimo)
            maximo = max(img.getpixel((x,y)),maximo)
    return minimo, maximo


def convert_to_L(img):
    """
    Devuelve img, de modo I, convertida a modo L.
    El valor mínimo de img pasa a ser 0, el máximo 255 y los valores
    intermedios se interpolan linealmente.
    """
    w,h = img.size
    result = Image.new('L',img.size)
    minimo,maximo = min_max(img)
    interval = float(maximo-minimo)
    for x in range(w):
        for y in range(h):
            result.putpixel((x,y),round(((img.getpixel((x,y))-minimo)/interval)*255))
    return result


def filter_kernel(img, kernel):
    """
    Código de la práctica. Propósito: aplicar un filtro a una imagen en escala de grises.
    
    Parámetros de entrada:
        img   : imagen a tratar. Debe ser tipo 'L' (escala de grises) y en formato '.png'
        kernel: filtro a aplicar. Lista de listas (matriz cuadrada de orden impar)
    
    Librería utilizada
        Image: importada desde PIL, nos permite trabajar con imagenes.
            size    : devuelve una tupla con el tamaño de la imagen asociada (ancho,alto)
            new     : crea una nueva imagen
            getpixel: devuelve el valor (como str!) asociado al color de un pixel
            putpixel: establece el valor numérico (color) deseado a un pixel

    Funciones llamadas:
        convert_to_L(img): Transforma una imagen tipo 'I' a tipo 'L', reescalando
                           el valor de los pixeles de la imagen
    Variables locales:
        w,h        : anchura y altura (respectivamente) de la imagen
        n          : variable que determina cuanto nos alejaremos del centro respecto 
                     al pixel al que estamos aplicando el filtro
        x, y, i, j : variables auxiliares que usaremos en los bucles
        retoque    : nueva imagen tipo 'I' en la que introduciremos los pixeles recalculados
        suma       : valor total del pixel una vez aplicado el filtro
    """
    w, h = img.size
    n = len(kernel) // 2
    retoque = Image.new('I',img.size)
    for x in range (w):                 # recorremos la imagen pixel a pixel
        for y in range (h):
            
            if x in range(n,w-n):       # aplicamos el filtro solo si el pixel está
                if y in range(n,h-n):   # lo suficientemente alejado del borde
                
                    suma = 0
                    for i in range(-n,n+1):     # el filtro se aleja 'n' posiciones del
                        for j in range(-n,n+1): # pixel tanto horizontal como verticalmente
                            suma = suma + int(img.getpixel((x+i,y+j))) * kernel[n+i][n+j]
                            
                    retoque.putpixel((x,y),suma) # añadimos el nuevo valor a la imagen tipo 'I'
                    
                else: # No tratamos los pixeles a los que no podemos aplicar el filtro completo 
                    retoque.putpixel((x,y),img.getpixel((x,y)))
                    
            else: # No tratamos los pixeles a los que no podemos aplicar el filtro completo 
                retoque.putpixel((x,y),img.getpixel((x,y)))
                
    return convert_to_L(retoque)