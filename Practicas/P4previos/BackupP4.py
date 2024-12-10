# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:51:39 2021

@author: Angel
"""

# -*- coding: utf-8 -*-
"""
Práctica 4 - Metro.

@author: Ángel Gil

En esta práctica haremos uso de clases para representar la red de metro de Madrid. 
Actualmente, la red de metro de Madrid se compone de 302 estaciones, 12 líneas 
convencionales y el ramal que une Ópera y Príncipe Pío. Además, existen tres 
líneas de metro ligero que suman un total de 27,78 km y cuentan con 38 estaciones.

De las 302 estaciones actuales, por 201 pasa una línea, en 27 transbordan dos 
líneas, en 10 tienen parada tres líneas y en la estación de Avenida de América 
coinciden cuatro líneas.
"""

f = open('metro_costes.txt','r')
contenido = f.readlines()

lineas, estaciones, tiempos = [], [], []
for i in range(len(contenido)):
    if i % 2 == 0:
        lineas.append(contenido[i].split())
    else:
        recorrido = contenido[i].split('->')
        estaciones.append([]),tiempos.append([])
        for j in range(len(recorrido)):
            if j % 2 == 0:
                estaciones[i//2].append(recorrido[j])
            else:
                tiempos[i//2].append(int(recorrido[j]))
                

class LineException(Exception):
    pass

class MetroException(Exception):
    pass

###   Parte 1 - Clase 'Line'   ###

class Line(object):
    """
    """
    def __init__(self, estaciones, tiempos):
        self.s:list = estaciones
        self.t:list = tiempos
        
    def __str__(self)->str:
        total = ''
        for i in self.s:
            if i != self.s[len(self.s)-1]:
                total = total + f'{i} --> '
            else:
                total = total + f'{i}'
        return total
        
    def contains_station(self,e):
        if e in self.s:
            return True
        else:
            return False
        
    def previous_e(self,e):
        try:
            if e not in self.s:
                raise LineException(str(e)+' no se encuentra en la linea dada.')
            i = self.s.index(e)
            if i == 0:
                raise LineException(str(e)+' es la primera parada de la linea')
            return self.s[i-1]
        except LineException as k:
            print(k)
        except:
            return None
            
    def next_e(self,e):
        try:
            if e not in self.s:
                raise LineException(str(e)+' no se encuentra en la linea dada.')
            i = self.s.index(e)
            if i == len(self.s) - 1:
                raise LineException(str(e)+' es la ultima parada de la linea')
            return self.s[i+1]
        except LineException as k:
            print(k)
        except:
            return None

    def cost_origin2destination(self,start, finish):
        try:
            if not (start in self.s and finish in self.s):
                raise LineException('Alguna de estas estaciones no se encuentra en la linea dada.')
            a,b = self.s.index(start),self.s.index(finish)
            suma = 0
            if a > b:
                for i in range(b,a):
                    suma = suma + self.t[i]
            elif a < b:
                for i in range(a,b):
                    suma = suma + self.t[i]
            return suma
        except LineException as k:
            print(k)

Linea=[]
for i in range(len(tiempos)):
    Linea.append(Line(estaciones[i],tiempos[i]))

###   Parte 2 - Clase 'Metro'   ###

class Metro(object):
    """
    """
    def __init__(self):
        self.vals = {}
        self.tbd  = {}
        
    def __str__(self)->str:
        print('Hola mundo')
        
    def add_line(self,line_name, line):
        try:
            for i in range(len(self.vals)):
                if line_name in self.vals.keys():
                    raise MetroException
            self.vals[line_name]=line
            add_connections(line_name,line)
        except MetroException:
            print('Esta linea ya se encuentra en la red de metro')
        except:
            print('Error desconocido')

    def add_connections(self,line_name, line):
        for i in line.s:
            if i in self.tbd.keys():
                self.tbd[i].append(line_name)
            else:
                for j in self.vals.keys():
                    if i in self.vals[j].s:
                        self.tbd[i] = [j,line_name]
            
    def load_metro(file_name):
        f = open(file_name,'r')
        contenido = f.readlines()

        for i in range(len(contenido)):
            if i % 2 == 1:
                recorrido = contenido[i].split('->')
                estaciones, tiempos = [],[]
                for j in range(len(recorrido)):
                    if j % 2 == 0:
                        estaciones.append(recorrido[j])
                    else:
                        tiempos.append(int(recorrido[j]))
                Metro.add_line(nombre_linea,Line(estaciones,tiempos))
                
            else:
                nombre_linea = contenido[i]
                    
    def get_connections(self,e, line_name):
        
    def cost_origin2destination_transfer(start, finish):
    def close_station(line_name, e):
    def open_station(line_name, e):
    def close_section(line_name, start, finish):
    def open_section(line_name):
    def cost_origin2destination_transferN(start, finish, n):