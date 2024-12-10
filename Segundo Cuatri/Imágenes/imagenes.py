# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:41:15 2021

@author: Angel
"""

from PIL import Image
i = Image.open('beach.png')
def line_h_gruesa(img, color, grosor):
    """
    Draw an horizontal line in the middle of the image 'img' of color 'color'
    @type img: PIL.Image
    @type color: either a number between 0..255 (gray) or a 3-tuple (r,g,b)
    """
    width, height = img.size
    for x in range(width):
        for g in range(-grosor//2,grosor//2,1):
            img.putpixel((x,height//2+g),color)
        

def  cuadricula(img,color,numverticales,numhorizontales):
    width, height = img.size
    v = width // numverticales
    h = height // numhorizontales
    for y in range(height):
        for x in range(v,numverticales*v,v):
            img.putpixel((x,y),color)
    for x in range(width):
        for y in range(h,numhorizontales*h,h):
            img.putpixel((x,y),color)