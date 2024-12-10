# -*- coding: utf-8 -*-
"""
Created on Thu May 13 13:55:25 2021

@author: Angel
"""

class Recta(object):
    def __init__(self,p1,p2):
        self.vertical=(p1.x==p2.x)
        if self.vertical:
            self.a=p1.x
        else:
            self.pend=(p1.y-p2.y)/(p1.x-p2.x)
            self.b=p1.y-self.pend*p1.x