# -*- coding: utf-8 -*-
"""
Práctica 4 - Metro.

@author: Ángel Gil

    Partes 1 y 2 funcionales.
"""


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
        self.est = []
        
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

###   Parte 2 - Clase 'Metro'   ###

class Metro(object):
    """
    """
    def __init__(self):
        self.vals = {}
        self.tbd  = {}
        self.cdo  = []
    def __str__(self)->str:
        print('Hola mundo')
        
    def add_line(self,line_name,line):
        try:
            if line_name in self.vals.keys():
                raise MetroException
            self.vals[line_name]=line
            print('todo ok')
            self.add_connections(line_name,line)
            
        except MetroException:
            print('Esta linea ya se encuentra en la red de metro')

    def add_connections(self,line_name, line):
        for i in line.s:
            print('final')
            if i in self.tbd.keys():
                self.tbd[i].append(line_name)
            else:
                for j in self.vals.keys():
                    if i in self.vals[j].s and j != line_name:
                       self.tbd[i] = [j,line_name]
            
    def load_metro(self,file_name):
        f = open(file_name,'r')
        contenido = f.readlines()

        for i in range(len(contenido)):
            if i % 2 == 0:
                print('par')
                nombre_linea = contenido[i].rstrip()
            else:
                print('impar')
                recorrido = contenido[i].split('->')
                estaciones, tiempos, estados = [],[], []
                for j in range(len(recorrido)):
                    if j % 2 == 0:
                        estaciones.append(recorrido[j].strip('\n'))
                        estados.append(True)
                    else:
                        tiempos.append(int(recorrido[j]))
                print(nombre_linea, Line(estaciones,tiempos))
                self.add_line(nombre_linea, Line(estaciones,tiempos))
        return self.vals
                    
    def get_connections(self,e, line_name):
        try:
            if line_name not in self.vals.keys():
                raise MetroException('Esta linea no se encuentra en la red de metro')
            elif e not in self.vals[line_name].s:
                raise MetroException('La estacion no pertenece a la linea dada')
            cnt = []
            if e in self.tbd.keys():
                for lin in self.tbd[e]:
                    if lin != line_name:
                        cnt.append(lin)
            return cnt
        except MetroException as k:
            print(k)

    def cost_origin2destination_transfer(self,start, finish):
        cost_min = 9999
        for key in self.vals.keys():
            if start in self.vals[key].s:
                if finish in self.vals[key].s:
                    cost = self.vals[key].cost_origin2destination(start,finish)
                    print(cost)
                    if cost < cost_min:
                        cost_min = cost
                else:
                    for e in self.vals[key].s:
                        for lin in self.get_connections(e,key):
                            if finish in self.vals[lin].s:
                                cost = self.vals[key].cost_origin2destination(start,e) + \
                                       300 + self.vals[lin].cost_origin2destination(e,finish)
                                print(cost)
                                if cost < cost_min:
                                    cost_min = cost
        if cost_min == 9999:
            return None
        else:
            return cost_min
        
    # def close_station(self,line_name, e):
    #     try:
    #         if line_name not in self.vals.keys():
    #             raise MetroException('Esta línea no se encuentra en la red de metro')
    #         if e not in self.vals[line_name].s:
    #             raise MetroException('Esta estación no pertenece a la línea dada')
            
    #         self.cdo.append((line_name,e))
            
    # def open_station(line_name, e):
    # def close_section(line_name, start, finish):
    # def open_section(line_name):
    # def cost_origin2destination_transferN(start, finish, n):

"""

    Integramos la parte 3 a la práctica

"""

