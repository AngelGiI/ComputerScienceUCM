# -*- coding: utf-8 -*-
"""
Ampliacion práctica 3: filtros de imágenes en color.

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
     Código de la práctica. Propósito: aplicar un filtro a una imagen en color.
    
    Parámetros de entrada:
        img   : imagen a tratar. Debe ser tipo 'RGB' (color) y en formato '.png'
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
        x, y, i, j : variables auxiliares para recorrer la imagen
        r, g, b    : imagenes tipo 'I' asociadas a la intensidad de 'R', 'G' y 'B' en las
                     que introduciremos los pixeles recalculados
        k          : variable auxiliar para pivotar entre las 3 imagenes
        final      : imagen tipo 'RGB' donde reuniremos 'r','g' y 'b', es decir, la imagen
                     original con el filtro ya aplicado
        suma       : lista de tres elementos, uno por color, asociada al valor total del
                     pixel una vez aplicado el filtro
    """
    w, h = img.size
    n = len(kernel) // 2
    r,g,b = Image.new('I',img.size),Image.new('I',img.size),Image.new('I',img.size)
    for x in range (w): # recorremos la imagen pixel a pixel
        for y in range (h):
            
            if x in range(n,w-n):       # aplicamos el filtro solo si el pixel está
                if y in range(n,h-n):   # lo suficientemente alejado del borde
                
                    suma = [0,0,0]
                    for i in range(-n,n+1):     # el filtro se aleja 'n' posiciones del
                        for j in range(-n,n+1): # pixel tanto horizontal como verticalmente
                        
                            for k in range(3): # Pivotamos entre cada imagen, tomando el
                                               # valor 'k' de la tupla asociada a cada pixel
                                               
                                suma[k] = suma[k] + int(img.getpixel((x+i,y+j))[k]) * kernel[n+i][n+j]
                                
                    r.putpixel((x,y),suma[0]) # añadimos el nuevo valor a cada imagen
                    g.putpixel((x,y),suma[1])
                    b.putpixel((x,y),suma[2])
                    
                else: # No tratamos los pixeles a los que no podemos aplicar el filtro completo
                    r.putpixel((x,y),img.getpixel((x,y))[0])
                    g.putpixel((x,y),img.getpixel((x,y))[1])
                    b.putpixel((x,y),img.getpixel((x,y))[2])
                    
            else: # No tratamos los pixeles a los que no podemos aplicar el filtro completo
                r.putpixel((x,y),img.getpixel((x,y))[0])
                g.putpixel((x,y),img.getpixel((x,y))[1])
                b.putpixel((x,y),img.getpixel((x,y))[2])

    R,G,B = convert_to_L(r), convert_to_L(g), convert_to_L(b)
    final = Image.new('RGB',img.size)
    
    for x in range (w):     # Una vez aplicado el filtro y devueltas las imagenes
        for y in range (h): # a tipo 'L', las reunimos en una imagen tipo 'RGB'.
        
            final.putpixel((x,y),(R.getpixel((x,y)),G.getpixel((x,y)),B.getpixel((x,y))))
            
    return final