# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 19:54:05 2021

@author: Angel
"""
import math
from PIL import Image

def sinusoide(img,color,loops):
    width, height = img.size
    for x in range(width):
        y = int(height*math.sin(x*loops/height))
        img.putpixel((x,y),color)
    img.show()