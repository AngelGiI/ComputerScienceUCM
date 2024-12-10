# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:03:01 2021

@author: Angel
"""

from PIL import Image

gris = Image.new("L", (1000,1000), 80)
roja = Image.new("RGB",(200,800),(255,0,0))

def UKflag_bien(img,color):
    width, height = img.size
    if width >= height:
        for x in range(width):
            img.putpixel((x,height//2),color)
            img.putpixel((x,(x*height)//width),color)
            img.putpixel((x,height-(x*height)//width-1),color)
    else:
        for x in range (height):
            img.putpixel(((width*x)//height,height-x-1),color)
            img.putpixel(((width*x)//height,x),color)
        for x in range(width):
            img.putpixel((x,height//2),color)
    img.save('rellenamos_alta.png')
    return img.show()